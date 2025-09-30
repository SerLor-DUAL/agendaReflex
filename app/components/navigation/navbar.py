import reflex as rx
from ...utils.styles import colors, spacing, typography, get_card_styles, get_button_styles
from ...state.auth_state import AuthState
from ...state.page_state import PageState
from .logo import Logo
from .auth_buttons import AuthButtons
from ..navigation.user_menu import UserMenu

# Colors now imported directly from design system

def Navbar(company_name: str = "IntegraQS") -> rx.Component:
    """Modern minimalist navbar with perfect alignment."""
    
    # Create navbar styles using available style functions
    navbar_styles = {
        **get_card_styles(variant="outline", padding="0"),
        "position": "fixed",
        "top": "0",
        "left": "0",
        "right": "0",
        "z_index": "1000",
        "backdrop_filter": "blur(10px)",
        "background": colors["surface"],
        "border_bottom": f"1px solid {colors['border']}",
        "border_radius": "0"  # Override card border radius for navbar
    }
    
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