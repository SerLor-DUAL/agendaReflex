import reflex as rx

from app.backend.models.user.model import User

class UserState(rx.State):
    users: list[dict] = []
    loading: bool = False
    message: str = ""
    mounted: bool = False

    def on_mount(self):
        self.mounted = True
        
        # Cleaning values on mount
        self.users = []       
        self.message = ""     
        self.loading = False

    # Decorator that converts this into a valid EventHandler
    @rx.event  
    def load_users(self):
        if self.loading:
            return  # evita doble fetch
        self.loading = True
        self.message = ""
        self.users = []

        try:
            with rx.session() as session:
                users_query = session.exec(User.select())
                self.users = [{"id": u.id, "nickname": u.nickname} for u in users_query]

            self.message = f"{len(self.users)} usuario(s) cargado(s) correctamente."
            
        except Exception as e:
            self.users = []
            self.message = f"Error al cargar usuarios: {str(e)}"
            
        finally:
            self.loading = False