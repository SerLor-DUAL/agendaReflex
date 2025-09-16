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
    return rx.box(
        Navbar(),  
        rx.box(
            RegisterForm(),
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
