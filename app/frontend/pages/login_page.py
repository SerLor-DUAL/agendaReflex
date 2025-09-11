import reflex as rx
# Import the needed components and state.
from ..components.navbar.navbar import Navbar
from ..components.forms.login_form import LoginForm
from ..state.page_state import PageState
# Import the ColorPallete class to access color definitions.
from ..components.colorPallet.colorPallet import ColorPallete

# Get colors from ColorPallete class
colors = ColorPallete().colors

def LoginPage():
    return rx.box(
        LoginForm(),
        width="100%",
        height="100vh", 
        display="flex",  
        align_items="center",  
        justify_content="center",  
        padding="2rem",
        background_color=colors["background"]
    )
