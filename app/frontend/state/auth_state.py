# app/frontend/state/auth_state.py
import reflex as rx
import httpx
from ...backend.config import app_settings as aps

class AuthState(rx.State):
    
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    # VARIABLES                                                                                                                          #
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    
    # State variables
    # ----------------------------------------------------------------------------------------- #
    nickname: str = ""
    password: str = ""
    message: str | dict | list = ""
    loading: bool = False
    is_authenticated: bool = False
    current_user: dict | None = None

    # Server-side variables
    # ----------------------------------------------------------------------------------------- #
    _debug_mode: bool = aps.DEBUG_MODE
    _access_token: str | None = None
    _refresh_token: str | None = None
    
    # Reactive variables
    # ----------------------------------------------------------------------------------------- #
    @rx.var
    def auth_message_text(self) -> str | None:
        if self.loading:
            return "Comprobando credenciales..."
        if self.message:
            return f"Error: {self.message}"
        if self.is_authenticated:
            return "Inicio de sesión exitoso"
        return ""

    @rx.var
    def auth_message_color(self) -> str:
        if self.loading:
            return "gray"
        if self.message:
            return "red"
        if self.is_authenticated:
            return "green"
        return "black"
    
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    # EVENTS                                                                                                                             #
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    
    @rx.event
    def set_nickname(self, value: str):
        self.nickname = value


    @rx.event
    def set_password(self, value: str):
        self.password = value

    # REGISTER                 
    # ----------------------------------------------------------------------------------------- #
    @rx.event
    async def register(self):
        """Try to register the user with frontend data. If successful, auto-login."""
        
        # Start loading and clear errors
        self.loading = True
        self.message = ""
        
        # Send request to backend to register
        async with httpx.AsyncClient(follow_redirects=True) as client:
            try:
                response = await client.post(
                    "{aps.API_URL}/register",
                    json={"nickname": self.nickname, "password": self.password},
                    timeout=10
                )
                
                # Check response status
                response.raise_for_status()
    
                # Auto-login after successful registration
                await self.login()

            # Handle HTTP errors and show them into the UI
            except httpx.HTTPStatusError as e:
                try:
                    self.message = e.response.json().get("detail")
                except Exception:
                    self.message = {f"Server error: {e}"}
            
            # Reset loading state
            finally:
                self.loading = False


    # LOGIN                 
    # ----------------------------------------------------------------------------------------- #
    @rx.event()
    async def login(self):
        """Login using a JS fetch request.
        
        If the login is successful, it will retrieve cookies from backend into browser.
        Then it will update the state variables, depending on the response. 
        
        If debug mode is enabled it shows the logs in the browser console."""
        
        # Start loading and clear errors
        self.loading = True
        self.message = ""
        
        # Debug control and header to see console logs in browser.
        debug_header = await self._get_debug_script_header()
        
        # Send login request via JS
        return rx.call_script(
            f"""
            {debug_header}
            
            __log('Iniciando proceso de login...');
            __log('Usuario:', '{self.nickname}');
            
            fetch("{aps.API_URL}/loginJSON", {{
                method: "POST",
                headers: {{ 
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                }},
                credentials: "include",
                body: JSON.stringify({{
                    nickname: "{self.nickname}",
                    password: "{self.password}"
                }})
            }})
            .then(async response => {{
                
                __log('Respuesta recibida:', response.status, response.statusText);
                
                let data = {{}};
                const contentType = response.headers.get('content-type');
                
                __log('Content-Type:', contentType);
                
                if (contentType && contentType.includes('application/json')) {{
                    try {{
                        data = await response.json();
                        __log('JSON parseado correctamente:', data);
                    }} catch (parseError) {{
                        data = {{ detail: "Error parseando respuesta JSON" }};
                        __log('Error parseando JSON:', parseError);
                    }}
                }} else {{
                    const textData = await response.text();
                    __log('Respuesta como texto:', textData);
                    data = {{ detail: "Respuesta no es JSON válido" }};
                }}

                const result = {{
                    ok: response.ok,
                    status: response.status,
                    statusText: response.statusText,
                    data: data
                }}
                
                __log('Resultado final del login:', result);
                return result;
            }})
            .catch(error => {{
                __log('Error de red en login:', error);
                return {{
                    ok: false,
                    status: 0,
                    statusText: 'Network Error',
                    data: {{ detail: error.message }}
                }};
            }})
            """,
            callback=AuthState.login_callback,
        )

    @rx.event
    async def login_callback(self, result: dict):
        """Callback which processes the login JS fetch response and interacts with the state variables."""
        
        # Check if result has a key "ok"
        if result.get("ok"):
            
            # Cookies HTTPOnly were stored correctly by browser, so now we store the tokens values in our state privately
            self._access_token = result["data"].get("access_token")
            self._refresh_token = result["data"].get("refresh_token")
            
            # self._access_token = result.get("data", {}).get("access_token")
            # self._refresh_token = result.get("data", {}).get("refresh_token")
            
            # Checks if user is authenticated
            return await self.check_auth()
            
        # If result does not have a key "ok"
        else:
            self.message = result["data"].get("detail", "Login failed")

            # Makes sure the user is logged out
            return await self.logout()
            

    # LOGOUT                 
    # ----------------------------------------------------------------------------------------- #
    @rx.event
    async def logout(self):
        """Logout using a JS fetch request.
        
        If the logout is successful, it will remove cookies from the browser and server.
        Then it will update the state variables, depending on the response. 
        
        If debug mode is enabled it shows the logs in the browser console."""
        
        # Start loading
        self.loading = False

        # Debug control and header to see console logs in browser.
        debug_header = await self._get_debug_script_header()

        return rx.call_script(
            f"""
            {debug_header}
                
            __log('Iniciando proceso de logout...');
            __log('Usuario:', '{self.current_user}');
            
            fetch("{aps.API_URL}/logout", {{
                method: "POST",             
                headers: {{ 
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                }},
                credentials: "include",
            }})
            .then(async response => {{
                
                __log('Respuesta recibida:', response.status, response.statusText);
                
                let data = {{}};
                const contentType = response.headers.get('content-type');
                
                __log('Content-Type:', contentType);
                
                if (contentType && contentType.includes('application/json')) {{
                    try {{
                        data = await response.json();
                        __log('JSON parseado correctamente:', data);
                    }} catch (parseError) {{
                        data = {{ detail: "Error parseando respuesta JSON" }};
                        __log('Error parseando JSON:', parseError);
                    }}
                }} else {{
                    const textData = await response.text();
                    __log('Respuesta como texto:', textData);
                    data = {{ detail: "Respuesta no es JSON válido" }};
                }}

                const result = {{
                    ok: response.ok,
                    status: response.status,
                    statusText: response.statusText,
                    data: data
                }}
                
                __log('Resultado final del logout:', result);
                return result;
            }})
            .catch(error => {{
                __log('Error de red en logout:', error);
                return {{
                    ok: false,
                    status: 0,
                    statusText: 'Network Error',
                    data: {{ detail: error.message }}
                }};
            }})
            """,
            callback=AuthState.logout_callback
        )

    @rx.event
    async def logout_callback(self, result):
        """Callback which processes the logout JS fetch response and interacts with the state variables."""
        print("1")
        # If result does not have a key "ok"
        if not result.get("ok"):
            self.message = result["data"].get("detail", "Logout failed")
            print("2a")
        else:
            self.message = ""
            print("2b")
        
        print("3")
        # Reset state variables always when logout
        self.loading = False            
        self.is_authenticated = False
        self.current_user = None
        self._access_token = None
        self._refresh_token = None



    # AUTH RELATED                 
    # ----------------------------------------------------------------------------------------- #
    @rx.event
    async def check_auth(self):
        """Check user authorization using a JS fetch request.
        
        If the auth is successful, it will update the state variables, depending on the response.
        
        In case the tokens are expired, it will try to refresh them. 
        Otherwise it will make sure the user is logged out.
        
        If debug mode is enabled it shows the logs in the browser console."""
        
        # Start loading
        self.loading = True
        
        # Debug control and header to see console logs in browser.
        debug_header = await self._get_debug_script_header()
        
        return rx.call_script(
            f"""
            {debug_header}
            
            __log('Verificando autenticación...');
            __log('Usuario:', '{self.nickname}');
            __log('Cookies:', {{access_token: "{self._access_token}", refresh_token: "{self._refresh_token}"}});
            
            fetch("{aps.API_URL}/me-cookie", {{
                method: "GET",
                headers: {{ 
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                }},
                credentials: "include"
            }})
            .then(async response => {{
                __log('Respuesta recibida:', response.status, response.statusText);
                
                __log('Headers de respuesta:');
                    for (let [key, value] of response.headers.entries()) {{
                        __log(key + ': ' + value);
                    }}
                
                let data = {{}};
                const contentType = response.headers.get('content-type');
                
                if (contentType && contentType.includes('application/json')) {{
                    try {{
                        data = await response.json();
                        __log('JSON parseado exitosamente:', data);
                    }} catch (parseError) {{
                        __log('Error parseando JSON:', parseError);
                        data = {{ detail: "Error parseando respuesta JSON" }};
                    }}
                }} else {{
                    __log('Respuesta no es JSON, content-type:', contentType);
                    const textData = await response.text();
                    __log('Contenido de respuesta:', textData);
                    data = {{ detail: "Respuesta no es JSON válido" }};
                }}

                const result = {{
                    ok: response.ok,
                    status: response.status,
                    statusText: response.statusText,
                    data: data
                }};
                
                __log('Resultado final de la autenticación:', result);
                
                return result;
            }})
            .catch(error => {{
                __log('Error de red en la autenticación:', error);
                
                return {{
                    ok: false,
                    status: 0,
                    statusText: 'Network Error',
                    data: {{ detail: error.message }}
                }};
            }})
            """,
            callback=AuthState.check_auth_callback,
        )
        
    @rx.event
    async def check_auth_callback(self, result: dict):
        """Callback which processes the check auth JS fetch response and interacts with the state variables."""
        
        # Check if result has a key "ok" and the user is authenticated
        if result.get("ok") and result["data"].get("is_authenticated"):
            self.is_authenticated = True
            self.current_user = result["data"]
            self.loading = False
            self.message = ""
        
        # If expired or missing access token, try to refresh        
        elif result.get("status") == 401:
            # Access expirado → intentamos refresh
            return await self.refresh_tokens()
        
        # If result does not have a key "ok" or a status 401, then the user is not authenticated, so it logs out
        else:
            return await self.logout()  

    # --------------------------------------------- #
    
    @rx.event
    async def refresh_tokens(self):
        
        # Debug control and header to see console logs in browser.
        debug_header = await self._get_debug_script_header()
        
        return rx.call_script(
            f"""
            {debug_header}
            
            __log('Verificando cookie con token de refresh...');
            __log('refresh_token: "{self._refresh_token}");

            fetch("{aps.API_URL}/refresh-token", {{
                method: "POST",
                credentials: "include"
            }})
            .then(async response => {{
                __log('Respuesta recibida:', response.status, response.statusText);
                
                __log('Headers de respuesta:');
                    for (let [key, value] of response.headers.entries()) {{
                        __log(key + ': ' + value);
                    }}
                
                let data = {{}};
                const contentType = response.headers.get('content-type');
                
                if (contentType && contentType.includes('application/json')) {{
                    try {{
                        data = await response.json();
                        __log('JSON parseado exitosamente:', data);
                    }} catch (parseError) {{
                        __log('Error parseando JSON:', parseError);
                        data = {{ detail: "Error parseando respuesta JSON" }};
                    }}
                }} else {{
                    __log('Respuesta no es JSON, content-type:', contentType);
                    const textData = await response.text();
                    __log('Contenido de respuesta:', textData);
                    data = {{ detail: "Respuesta no es JSON válido" }};
                }}

                const result = {{
                    ok: response.ok,
                    status: response.status,
                    statusText: response.statusText,
                    data: data
                }};
                
                __log('Resultado final del refresco de tokens:', result);
                
                return result;
            }})
            .catch(error => {{
                __log('Error de red en el refresco:', error);
                
                return {{
                    ok: false,
                    status: 0,
                    statusText: 'Network Error',
                    data: {{ detail: error.message }}
                }};
            }})
            """,
            callback=AuthState.refresh_tokens_callback
        )

    @rx.event
    async def refresh_tokens_callback(self, result: dict):
        """Callback which processes the refresh tokens JS fetch response and interacts with the state variables."""
        
        # Check if result has a key "ok" and the refresh token exists
        if result.get("ok") and "refresh_token" in result["data"]:
            
            # Updates tokens
            self._access_token = result["data"]["access_token"]
            self._refresh_token = result["data"].get("refresh_token", self._refresh_token)
            
            return await self.check_auth()
        
        # If result does not have a key "ok" and the refresh token does not exist then logout
        else: 
            return await self.logout()
            

    # ---------------------------------------------------------------------------------------------------------------------------------- #
    # AUXILIAR                                                                                                                           #
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    async def _get_debug_script_header(self) -> str:
            """ Generates the JS header of the __log function depending on the debug mode. """
            
            # If debug mode is enabled, return the __log function as console.log, otherwise return an empty function
            if self._debug_mode:
                return "const __log = console.log;"
            else:
                return "const __log = () => {};" 