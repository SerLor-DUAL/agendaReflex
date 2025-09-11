# app/frontend/state/auth_state.py
import reflex as rx
import httpx

class AuthState(rx.State):
    
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    # VARIABLES                                                                                                                          #
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    
    # State variables
    # ----------------------------------------------------------------------------------------- #
    nickname: str = ""
    password: str = ""
    loading: bool = False
    error_msg: str = ""
    is_authenticated: bool = False
    current_user: dict | None = None

    # Server-side variables
    # ----------------------------------------------------------------------------------------- #
    _access_token: str | None = None
    _refresh_token: str | None = None
    
    # Reactive variables
    # ----------------------------------------------------------------------------------------- #
    @rx.var
    def auth_message_text(self) -> str | None:
        if self.loading:
            return "Comprobando credenciales..."
        if self.error_msg:
            return f"Error: {self.error_msg}"
        if self.is_authenticated:
            return "Inicio de sesión exitoso"
        return None

    @rx.var
    def auth_message_color(self) -> str:
        if self.loading:
            return "gray"
        if self.error_msg:
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

    @rx.event
    def clear_success_message(self):
        self.is_authenticated = False
        self._access_token = None
        self._refresh_token = None
        self.error_msg = ""


    # REGISTER                 
    # ----------------------------------------------------------------------------------------- #
    @rx.event
    async def register(self):
        """Try to register user with frontend data. If successful, auto-login."""
        
        # Start loading and clear errors
        self.loading = True
        self.error_msg = ""
        
        # Send request to backend to register
        async with httpx.AsyncClient(follow_redirects=True) as client:
            try:
                response = await client.post(
                    "http://localhost:8000/register",
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
                    self.error_msg = e.response.json().get("detail")
                except Exception:
                    self.error_msg = f"Server error: {e}"
            
            # Reset loading state
            finally:
                self.loading = False


    # LOGIN                 
    # ----------------------------------------------------------------------------------------- #
    @rx.event()
    async def login(self):
        """Login using a JS fetch request.
        If the login is successful, it will retrieve cookies from backend into browser.
        Then it will update the state variables, depending on the response. """
        
        # Start loading and clear errors
        self.loading = True
        self.error_msg = ""
        
        # Fix possible problems with special characters
        safe_nickname = self.nickname.replace('"', '\\"').replace("'", "\\'")
        safe_password = self.password.replace('"', '\\"').replace("'", "\\'")
        
        # Send login request via JS
        return rx.call_script(
            f"""
            console.log('=== INICIANDO LOGIN FETCH ===');
            console.log('Nickname:', '{safe_nickname}');
            
            fetch("http://localhost:8000/loginJSON", {{
                method: "POST",
                headers: {{ 
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                }},
                credentials: "include",
                body: JSON.stringify({{
                    nickname: "{safe_nickname}",
                    password: "{safe_password}"
                }})
            }})
            .then(async response => {{
                console.log('Respuesta recibida:', {{
                    status: response.status,
                    ok: response.ok,
                    statusText: response.statusText
                }});
                
                // Log de headers de respuesta
                console.log('Headers de respuesta:');
                for (let [key, value] of response.headers.entries()) {{
                    console.log(key + ': ' + value);
                }}
                
                let data = null;
                const contentType = response.headers.get('content-type');
                
                if (contentType && contentType.includes('application/json')) {{
                    try {{
                        data = await response.json();
                        console.log('JSON parseado exitosamente:', data);
                    }} catch (parseError) {{
                        console.error('Error parseando JSON:', parseError);
                        data = {{ detail: "Error parseando respuesta JSON" }};
                    }}
                }} else {{
                    console.log('Respuesta no es JSON, content-type:', contentType);
                    const textData = await response.text();
                    console.log('Contenido de respuesta:', textData);
                    data = {{ detail: "Respuesta no es JSON válido" }};
                }}


                const result = {{
                    ok: response.ok,
                    status: response.status,
                    statusText: response.statusText,
                    data: data
                }};
                
                console.log('=== RESULTADO FINAL PARA CALLBACK ===');
                console.log(JSON.stringify(result, null, 2));
                console.log('=== ENVIANDO A CALLBACK ===');
                
                return result;
            }})
            .catch(error => {{
                console.error('=== ERROR EN FETCH ===');
                console.error('Tipo de error:', error.name);
                console.error('Mensaje:', error.message);
                console.error('Stack:', error.stack);
                
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
        
    def login_js_debug():
        result = "a"
    
    @rx.event
    async def login_callback(self, result: dict):
        """Callback which processes the JS fetch response and interacts with the state variables."""
        
        self.loading = False
        
        # Validar que tenemos un resultado válido
        if not isinstance(result, dict):
            print(f"ERROR: El resultado no es un diccionario: {type(result)}")
            self.error_msg = "Error interno: respuesta inválida"
            self.is_authenticated = False
            return

        # Verificar si la petición fue exitosa
        if not result.get("ok"):
            error_detail = result.get("data", {}).get("detail", "Error desconocido")
            if isinstance(result.get("data"), dict):
                error_detail = result["data"].get("detail", "Error desconocido")
            else:
                error_detail = str(result.get("data", "Error desconocido"))
                
            print(f"LOGIN FALLIDO: {error_detail}")
            self.error_msg = error_detail
            self.is_authenticated = False
            return

        # Check status code from result
        status_code = result.get("status", 0)
        
        # Status code is ok
        if status_code == 200:
            self.error_msg = ""
            
            # Cookies HTTPOnly were stored correctly by browser, so now we store the tokens values in our state privately
            self._access_token = result.get("data", {}).get("access_token")
            self._refresh_token = result.get("data", {}).get("refresh_token")
            
            # Check authentication
            return await self.check_auth()
        
        # Status code is not ok
        else:

            # Get error data
            error_data = result.get("data", {})
            
            # Get error detail
            if isinstance(error_data, dict):
                error_detail = error_data.get("detail", f"Error {status_code}")
            else:
                error_detail = f"Error {status_code}: {error_data}"
                
            # Login failed so, set error message and logout
            self.error_msg = error_detail
            await self.logout()

    # LOGOUT                 
    # ----------------------------------------------------------------------------------------- #
    @rx.event
    async def logout(self):
        """Logout user by clearing tokens and user info."""
        
        # Start loading
        self.loading = True
        
        return rx.call_script(
        """
        console.log('=== INICIANDO LOGOUT FETCH ===');
        
        fetch("http://localhost:8000/logout", {
            method: "POST",
            credentials: "include"
        })
        .then(async response => {
            console.log('Logout response status:', response.status);
            let data = {};
            const contentType = response.headers.get('content-type');
            
            if (contentType && contentType.includes('application/json')) {
                try {
                    data = await response.json();
                    console.log('JSON parseado logout:', data);
                } catch (parseError) {
                    console.error('Error parseando JSON logout:', parseError);
                }
            }
            
            const result = {
                ok: response.ok,
                status: response.status,
                data: data
            };
            
            console.log('=== RESULTADO LOGOUT PARA CALLBACK ===', result);
            return result;
        })
        .catch(error => {
            console.error('Error en logout fetch:', error);
            return {ok: false, status: 0, data: {detail: error.message}};
        })
        """,
            callback=AuthState.logout_callback
        )

    @rx.event
    def logout_callback(self, result):

        self.loading = False
        self.is_authenticated = False
        self.current_user = None
        self._access_token = None
        self._refresh_token = None


    # AUTH RELATED                 
    # ----------------------------------------------------------------------------------------- #
    @rx.event
    async def check_auth(self):
        """Check if the user is authenticated by validating the access token with the backend."""
        self.loading = True
        
        return rx.call_script(
            f"""
            console.log('=== INICIANDO AUTH FETCH ===');
            
            fetch("http://localhost:8000/me-cookie", {{
                method: "GET",
                headers: {{ 
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                }},
                credentials: "include"
            }})
            .then(async response => {{
                console.log('Respuesta recibida:', {{
                    status: response.status,
                    ok: response.ok,
                    statusText: response.statusText
                }});
                
                // Log de headers de respuesta
                console.log('Headers de respuesta:');
                for (let [key, value] of response.headers.entries()) {{
                    console.log(key + ': ' + value);
                }}
                
                let data = null;
                const contentType = response.headers.get('content-type');
                
                if (contentType && contentType.includes('application/json')) {{
                    try {{
                        data = await response.json();
                        console.log('JSON parseado exitosamente:', data);
                    }} catch (parseError) {{
                        console.error('Error parseando JSON:', parseError);
                        data = {{ detail: "Error parseando respuesta JSON" }};
                    }}
                }} else {{
                    console.log('Respuesta no es JSON, content-type:', contentType);
                    const textData = await response.text();
                    console.log('Contenido de respuesta:', textData);
                    data = {{ detail: "Respuesta no es JSON válido" }};
                }}


                const result = {{
                    ok: response.ok,
                    status: response.status,
                    statusText: response.statusText,
                    data: data
                }};
                
                console.log('=== RESULTADO FINAL PARA CALLBACK ===');
                console.log(JSON.stringify(result, null, 2));
                console.log('=== ENVIANDO A CALLBACK ===');
                
                return result;
            }})
            .catch(error => {{
                console.error('=== ERROR EN FETCH ===');
                console.error('Tipo de error:', error.name);
                console.error('Mensaje:', error.message);
                console.error('Stack:', error.stack);
                
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
    async def check_auth_callback(self, result):
        
        data = result.get("data", {})

        # Si la respuesta fue ok y contiene datos de usuario
        if result.get("ok") and data.get("is_authenticated"):
            self.is_authenticated = True
            self.current_user = data
        else:
            await self.refresh_tokens()

        self.loading = False

    # --------------------------------------------- #
    
    @rx.event
    async def refresh_tokens(self):
        self.loading = True

        return rx.call_script(
            """
            console.log('=== INICIANDO REFRESH TOKENS ===');

            fetch("http://localhost:8000/refresh-token", {
                method: "POST",
                credentials: "include"
            })
            .then(async response => {
                console.log('Refresh response status:', response.status);
                let data = {};
                const contentType = response.headers.get('content-type');

                if (contentType && contentType.includes('application/json')) {
                    try {
                        data = await response.json();
                        console.log('JSON parseado refresh tokens:', data);
                    } catch (parseError) {
                        console.error('Error parseando JSON refresh:', parseError);
                    }
                }

                const result = {
                    ok: response.ok,
                    status: response.status,
                    data: data
                };

                console.log('=== RESULTADO REFRESH TOKENS PARA CALLBACK ===', result);
                return result;
            })
            .catch(error => {
                console.error('Error en refresh tokens fetch:', error);
                return {ok: false, status: 0, data: {detail: error.message}};
            })
            """,
            callback=AuthState.refresh_tokens_callback
        )

    @rx.event
    async def refresh_tokens_callback(self, result):
        
        if result.get("ok") and "access_token" in result["data"]:
            self._access_token = result["data"]["access_token"]
            self._refresh_token = result["data"].get("refresh_token", self._refresh_token)
            print("Tokens actualizados:", self._access_token, self._refresh_token)
        else:
            print("Refresh tokens falló, forzando logout")
            await self.logout()
            
        self.loading = False