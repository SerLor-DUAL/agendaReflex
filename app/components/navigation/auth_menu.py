import reflex as rx
from ...utils.styles.colorPallet import ColorPallet
from ...state.page_state import PageState
from ...state.auth_state import AuthState

colors = ColorPallet().colors

def AuthMenu() -> rx.Component:
    """
    Authenticated user menu with dropdown.
    
    Returns:
        rx.Component: Menu component for authenticated users
    """
    
    return rx.menu.root(
        rx.menu.trigger(
            rx.button(
                rx.hstack(
                    rx.icon("menu", size=18, color=colors["text"]),
                    rx.text("Menu", font_weight="500", color=colors["text"]),
                    spacing="2",
                    align="center"
                ),
                variant="ghost",
                style={
                    "background": "transparent",
                    "border": f"1px solid {colors['glassBorder']}",
                    "border_radius": "12px",
                    "padding": "10px 16px",
                    "transition": "all 0.2s cubic-bezier(0.4, 0, 0.2, 1)",
                    "color": colors["text"],
                    "_hover": {
                        "background": colors["surface"],
                        "border_color": colors["borderLight"],
                        "transform": "translateY(-1px)",
                        "box_shadow": f"0 4px 12px {colors['focusRing']}",
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
                on_click=lambda: PageState.show_form("clientes")
            ),
            rx.menu.item(
                rx.hstack(
                    rx.icon("shopping-bag", size=16, color=colors["primary"]),
                    rx.text("Orders", color=colors["text"]),
                    spacing="2"
                ),
                on_click=lambda: PageState.show_form("pedidos")
            ),
            rx.menu.separator(style={"background": colors["border"]}),
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
