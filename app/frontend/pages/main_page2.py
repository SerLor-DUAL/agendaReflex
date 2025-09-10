import reflex as rx
from ..components.auth.login_form import LoginForm
from ..components.auth.register_form import RegisterForm
from ..components.navbar.navbar_form import Navbar
from ..state.page_state import PageState

def MainPage():
    return rx.box(
        Navbar(),
        rx.hstack(
            rx.button("Iniciar sesión", on_click= PageState.show_form("login")),
            rx.button("Registro", on_click= PageState.show_form("register")),
            spacing="2",
            padding="1rem"
        ),
        rx.box(
            rx.cond(
                PageState.current_form == "login",
                LoginForm(),
                rx.cond(
                    PageState.current_form == "register",
                    RegisterForm(),
                    None
                )
            ),
            padding="2rem"
        ),
        width="100%",
        #max_width="500px",
        margin="0 auto",
        
        )
