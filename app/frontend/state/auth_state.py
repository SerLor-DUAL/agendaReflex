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
    # _access_token: str | None = None
    # _refresh_token: str | None = None
    
    # Cookies Reflex (serán persistentes en navegador)
    access_token: str = rx.Cookie(name="access_token", secure=False, same_site="strict")
    refresh_token: str = rx.Cookie(name="refresh_token", secure=False, same_site="strict")

    # ----------------- #
    # Events for UI use #
    # ----------------- #
    
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
        return "black"  # por defecto


    @rx.event
    def clear_success_message(self):
        self.is_authenticated = False
        self.access_token = ""
        self.refresh_token = ""
        
    @rx.event
    async def login(self):
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

                # Save backend tokens retrieved from login
                self.access_token = data.get("access_token")
                self.refresh_token = data.get("refresh_token")

                # Console tokens debug
                print("Access token:", self.access_token)
                print("Refresh token:", self.refresh_token)

                # Loads user auth info
                await self.check_auth()
            
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

                # Get cookies from the current client
                cookie_header = self.router.headers.cookie or ""
                cookies = {}
                for pair in cookie_header.split(";"):
                    if "=" in pair:
                        k, v = pair.strip().split("=", 1)
                        cookies[k] = v

                # If using cookie-based auth, the client will handle cookies automatically
                response = await client.get(
                    "http://localhost:8000/me-cookie",
                    cookies=cookies,
                    timeout=10
                )
                
                # Check response status
                response.raise_for_status()
                
                # Save current user info
                self.current_user = response.json()
                self.is_authenticated = True
                
            except httpx.HTTPStatusError as e:
                print("respuesta: ", e.response.status_code)
                
                if e.response.status_code == 401:
                    # Access token expired → try refresh
                    await self.refresh_tokens()
                    
                    # Try again again if refresh was successful
                    await self.check_auth()
                
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
                # Actualiza cookies
                self.access_token = data.get("access_token", self.access_token)
                self.refresh_token = data.get("refresh_token", self.refresh_token)
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
                self.access_token = ""
                self.refresh_token = ""
                self.current_user = None
                self.is_authenticated = False

                # Clear session cookie in backend
                # await client.post("http://localhost:8000/logout")
                return rx.remove_cookie("access_token"), rx.remove_cookie("refresh_token")
                
            # Reset loading state    
            finally:
                self.loading = False