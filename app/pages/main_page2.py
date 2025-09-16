import reflex as rx
#from ..components.auth.login_form import LoginForm
#from ..components.auth.register_form import RegisterForm
from ..components.navbar.navbar import Navbar
from ..components.forms.login_form import LoginForm
from ..components.forms.register_form import RegisterForm
from ..state.page_state import PageState

# ColorPallet
from ..utils.colorPallet.colorPallet import ColorPallet

colors = ColorPallet().colors
def MainPage():
    PageState.show_form("login")
    return rx.box(
        Navbar(),  
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
            on_mount=PageState.show_form("login"), # Show login form by default when the component mounts
            display="flex",
            align_items="center",
            justify_content="center",
            height="calc(100vh - 6em)",
            padding="2rem",
            background_color=colors["generalBackground"],
        ),
        background_color=colors["generalBackground"],
        width="100%",
        margin="0 auto",
    )


