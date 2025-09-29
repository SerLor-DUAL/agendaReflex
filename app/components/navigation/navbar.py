import reflex as rx
from ...utils.styles.colorPallet import ColorPallet
from ...utils.styles.modern_styles import get_modern_navbar_styles
from ...state.auth_state import AuthState
from ...state.page_state import PageState
from .logo import Logo
from .auth_buttons import AuthButtons
from ..navigation.user_menu import UserMenu

colors = ColorPallet().colors

def Navbar(company_name: str = "IntegraQS") -> rx.Component:
    """Modern minimalist navbar with perfect alignment."""
    
    navbar_styles = get_modern_navbar_styles()
    
    # Desktop navbar
    desktop_nav = rx.flex(
        Logo(company_name, size="lg"),
        rx.spacer(),
        rx.cond(AuthState.is_authenticated, UserMenu(), AuthButtons()),
        justify="between",
        align="center",
        width="100%",
        max_width="1200px",
        margin="0 auto",
        padding="0 24px",
        height="100%",
        style={
            "display": "flex",
            "align_items": "center",
            "justify_content": "space-between"
        }
    )
    
    # Mobile navbar
    mobile_nav = rx.flex(
        Logo(company_name, size="sm"),
        rx.spacer(),
        rx.cond(AuthState.is_authenticated, UserMenu(), AuthButtons()),
        justify="between",
        align="center",
        width="100%",
        padding="0 16px",
        height="100%",
        style={
            "display": "flex",
            "align_items": "center",
            "justify_content": "space-between"
        }
    )
    
    return rx.box(
        rx.desktop_only(desktop_nav),
        rx.mobile_and_tablet(mobile_nav),
        style=navbar_styles,
        width="100%",
        height="72px"
    )