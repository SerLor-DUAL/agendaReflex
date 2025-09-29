import reflex as rx
from ...utils.styles.colorPallet import ColorPallet
from ...state.auth_state import AuthState
from ...state.page_state import PageState

colors = ColorPallet().colors

def UserMenu() -> rx.Component:
    """User menu for authenticated users."""
    
    return rx.menu.root(
        rx.menu.trigger(
            rx.button(
                rx.hstack(
                    rx.icon("user", size=16),
                    rx.text("Menu", font_weight="500"),
                    spacing="2",
                    align="center"
                ),
                variant="ghost",
                style={
                    "background": "transparent",
                    "border": f"1px solid {colors['glassBorder']}",
                    "border_radius": "12px",
                    "padding": "8px 16px",
                    "transition": "all 0.2s ease",
                    "color": colors["text"],
                    "_hover": {
                        "background": colors["surface"],
                        "border_color": colors["borderLight"],
                    }
                }
            )
        ),
        rx.menu.content(
            rx.menu.item(
                rx.hstack(
                    rx.icon("users", size=16, color=colors["primary"]),
                    rx.text("Clients", color=colors["text"]),
                    spacing="2"
                ),
                on_click=lambda: PageState.show_form("clients")
            ),
            rx.menu.item(
                rx.hstack(
                    rx.icon("shopping-bag", size=16, color=colors["primary"]),
                    rx.text("Orders", color=colors["text"]),
                    spacing="2"
                ),
                on_click=lambda: PageState.show_form("orders")
            ),
            rx.menu.separator(),
            rx.menu.item(
                rx.hstack(
                    rx.icon("log-out", size=16, color=colors["error"]),
                    rx.text("Sign Out", color=colors["error"]),
                    spacing="2"
                ),
                on_click=AuthState.logout
            ),
            style={
                "background": colors["glassBackground"],
                "backdrop_filter": "blur(20px)",
                "border": f"1px solid {colors['glassBorder']}",
                "border_radius": "12px",
                "box_shadow": "0 8px 32px rgba(0, 0, 0, 0.3)",
                "min_width": "160px",
            }
        )
    )