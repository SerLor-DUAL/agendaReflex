# app/frontend/state/auth_state.py
import reflex as rx
import httpx

class AuthState(rx.State):
    
    # ----------------------- #
    # Variables for the state #
    # ----------------------- #
    
    # UI
    nickname: str = ""
    password: str = ""
    loading: bool = False
    error_msg: str = ""
    is_authenticated: bool = False
    current_user: dict | None = None

    # # Server-side
    _access_token: str | None = None
    _refresh_token: str | None = None
    
    # Cookies Reflex (serán persistentes en navegador)
    # access_token: str = rx.Cookie(name="access_token", secure=False, same_site="strict")
    # refresh_token: str = rx.Cookie(name="refresh_token", secure=False, same_site="strict")
    
    # ----------------- #
    # Events for UI use #
    # ----------------- #
    
    # Debug info para mostrar en UI
    debug_info: str = ""
    callback_executed: bool = False

    @rx.event
    def set_nickname(self, value: str):
        self.nickname = value

    @rx.event
    def set_password(self, value: str):
        self.password = value

    # ------------------------- #
    # Computed var para UI
    # ------------------------- #
    
    # Texto del mensaje
    @rx.var
    def auth_message_text(self) -> str | None:
        if self.loading:
            return "Comprobando credenciales..."
        if self.error_msg:
            return f"Error: {self.error_msg}"
        if self.is_authenticated and self.access_token and self.refresh_token:
            return "Inicio de sesión exitoso"
        return None

    # Color del mensaje
    @rx.var
    def auth_message_color(self) -> str:
        if self.loading:
            return "gray"
        if self.error_msg:
            return "red"
        if self.is_authenticated and self.access_token and self.refresh_token:
            return "green"
        return "black"


    @rx.event
    def clear_success_message(self):
        self.is_authenticated = False
        self._access_token = ""
        self._refresh_token = ""

    @rx.event()
    async def login(self):
        """Login usando fetch del navegador para manejar cookies HTTPOnly correctamente."""
        
        self.loading = True
        self.error_msg = ""
        self.callback_executed = False
        self.debug_info = "Iniciando login..."
        
        # Escapar comillas en nickname y password para evitar problemas de JS
        safe_nickname = self.nickname.replace('"', '\\"').replace("'", "\\'")
        safe_password = self.password.replace('"', '\\"').replace("'", "\\'")

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
                credentials: "include", // CRÍTICO para cookies HTTPOnly
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
            callback=self.login_callback,
        )

    @rx.event
    def login_callback(self, result: dict):
        """Callback que procesa la respuesta del fetch de login."""
        
        print("=" * 50)
        print("CALLBACK DE LOGIN EJECUTADO")
        print("=" * 50)
        print(f"Resultado recibido: {result}")
        print(f"Tipo de resultado: {type(result)}")
        print("=" * 50)
        
        # Marcar que el callback se ejecutó
        self.callback_executed = True
        self.loading = False
        self.debug_info = f"Callback ejecutado: {str(result)[:200]}..."
        
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

        # Verificar el status code
        status_code = result.get("status", 0)
        print(f"Status code recibido: {status_code}")
        
        if status_code == 200:
            print("LOGIN EXITOSO - Status 200")
            self.is_authenticated = True
            self.error_msg = ""
            
            # Las cookies HTTPOnly ya están establecidas por el navegador
            # Ahora verificamos la autenticación
            print("Verificando autenticación...")
            return self.check_auth_with_cookies()
            
        else:
            # Manejar otros status codes
            error_data = result.get("data", {})
            if isinstance(error_data, dict):
                error_detail = error_data.get("detail", f"Error {status_code}")
            else:
                error_detail = f"Error {status_code}: {error_data}"
                
            print(f"LOGIN FALLIDO - Status {status_code}: {error_detail}")
            self.error_msg = error_detail
            self.is_authenticated = False


    @rx.event()
    async def login2(self):
        """Try to login user with frontend data and store retrieved tokens in server-side variables."""
        
        # Start loading and clear errors
        self.loading = True
        self.error_msg = ""
        # Send request to backend to login
        async with httpx.AsyncClient(follow_redirects=True) as client:
            try:
                response = await client.post(
                    "http://localhost:8000/loginJSON",
                    json={"nickname": self.nickname, "password": self.password},
                    timeout=10,
                )
                
                # Check response status
                response.raise_for_status()
                
                # Get response data
                data = response.json()

                _access_token = data.get("access_token")
                _refresh_token = data.get("refresh_token")
                
                # Save backend tokens retrieved from login
                #self.access_token = data.get("access_token")
                #self.refresh_token = data.get("refresh_token")

                # Loads user auth info
                #await self.check_auth()
            
            # Handle HTTP errors and show them into the UI
            except httpx.HTTPStatusError as e:
                try:
                    self.error_msg = e.response.json().get("detail")
                except Exception:
                    self.error_msg = str(e)
            
            # Reset loading state
            finally:
                self.loading = False

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

    @rx.event
    async def check_auth(self):
        """Check if the user is authenticated by validating the access token with the backend."""
        
        # Start loading
        self.loading = True
        
        # Send request to backend to get current user info
        async with httpx.AsyncClient(follow_redirects=True) as client:
            try:
            
                print(self._access_token)
                # If using cookie-based auth, the client will handle cookies automatically
                response = await client.get(
                    "http://localhost:8000/me-cookie",
                    cookies={"access_token": self._access_token, "refresh_token": self._refresh_token},
                    timeout=10
                )
    
                response.raise_for_status()
                
                # Save current user info
                self.current_user = response.json()
                self.is_authenticated = True

            except httpx.HTTPStatusError as e:
                print("respuesta: ", e.response.status_code)
                print("detalle: ", e.response.text)
                
                # if e.response.status_code == 401:
                #     # Access token expired → try refresh
                #     await self.refresh_tokens()
                    

                # Try again again if refresh was successful
                #     await self.check_auth()
                
                # else:
                #     print(e.response.status_code)
                #     self.current_user = None
                #     self.is_authenticated = False
                
            # Reset loading state
            finally:
                self.loading = False

                
                
    @rx.event
    async def refresh_tokens(self):
        async with httpx.AsyncClient(follow_redirects=True, verify=True) as client:
            try:
                response = await client.post(
                    "http://localhost:8000/refresh-token",
                    cookies={"refresh_token": self.refresh_token},
                    timeout=10
                )
                response.raise_for_status()
                data = response.json()
                # # Actualiza cookies
                # self.access_token = data.get("access_token", self.access_token)
                # self.refresh_token = data.get("refresh_token", self.refresh_token)
            except httpx.HTTPStatusError:
                # Refresh falló → forzar logout
                await self.logout()

    @rx.event
    async def logout(self):
        """Logout user by clearing tokens and user info."""
        
        # Start loading
        self.loading = True
        
        # Send request to backend to logout
        async with httpx.AsyncClient(follow_redirects=True) as client:
            try:
                # rx.remove_cookie(self.access_token)
                # rx.remove_cookie(self.refresh_token)
                self.current_user = None
                self.is_authenticated = False

                # Clear session cookie in backend
                # await client.post("http://localhost:8000/logout")
                # return rx.remove_cookie("access_token"), rx.remove_cookie("refresh_token")
                
            # Reset loading state    
            finally:
                self.loading = False