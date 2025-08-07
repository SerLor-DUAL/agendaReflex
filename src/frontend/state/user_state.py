import reflex as rx
from ..services.user_service import fetch_users

class UserState(rx.State):
    users: list[dict] = []
    loading: bool = False
    message: str = ""
    mounted: bool = False

    def on_mount(self):
        # Solo en cliente, inicializamos fetch
        self.mounted = True
        # Disparamos el evento (decorado) directamente
        UserState.load_users()

    @rx.event  # ← decorador que convierte esto en un EventHandler válido
    async def load_users(self):
        # Este código corre como coroutine, pero Reflex lo gestiona
        self.loading = True
        try:
            data, msg = await fetch_users()
            self.users = data
            self.message = msg
        except Exception as e:
            self.message = f"Error inesperado: {e}"
        self.loading = False
