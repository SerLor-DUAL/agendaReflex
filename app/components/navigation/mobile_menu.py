import reflex as rx
from ...utils.styles import colors, spacing, typography
from ...state.page_state import PageState
from ...state.auth_state import AuthState

# Colors now imported directly from design system

def MobileMenu() -> rx.Component:
    """
    Mobile menu component with responsive design.
    
    Returns:
        rx.Component: Mobile menu for tablet and phone screens
    """
    
    return rx.menu.root(
        rx.menu.trigger(
            rx.button(
                rx.icon("menu", size=20, color=colors["text_primary"]),
                variant="ghost",
                style={
                    "background": "transparent",
                    "border": f"1px solid {colors['glassBorder']}",
                    "border_radius": "10px",
                    "padding": "10px",
                    "transition": "all 0.2s ease",
                    "color": colors["text_primary"],
                    "_hover": {
                        "background": colors["surface"],
                        "border_color": colors["border_light"],
                        "box_shadow": f"0 4px 12px {colors['focusRing']}",
                    }
                }
            )
        ),
        rx.menu.content(
            rx.cond(
                AuthState.is_authenticated,
                rx.fragment(
                    rx.menu.item(
                        rx.hstack(
                            rx.icon("users", size=16, color=colors["primary"]),
                            rx.text("Clients", color=colors["text_primary"]),
                            spacing="2"
                        ),
                        on_click=lambda: PageState.show_form("clientes")
                    ),
                    rx.menu.item(
                        rx.hstack(
                            rx.icon("shopping-bag", size=16, color=colors["primary"]),
                            rx.text("Orders", color=colors["text_primary"]),
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
                ),
                rx.fragment(
                    rx.menu.item(
                        rx.hstack(
                            rx.icon("log-in", size=16, color=colors["primary"]),
                            rx.text("Sign In", color=colors["text_primary"]),
                            spacing="2"
                        ),
                        on_click=lambda: PageState.show_form("login")
                    ),
                    rx.menu.item(
                        rx.hstack(
                            rx.icon("user-plus", size=16, color=colors["primary"]),
                            rx.text("Sign Up", color=colors["text_primary"]),
                            spacing="2"
                        ),
                        on_click=lambda: PageState.show_form("register")
                    ),
                )
            ),
            style={
                "background": colors["surface"],
                "backdrop_filter": "blur(20px)",
                "border": f"1px solid {colors['glassBorder']}",
                "border_radius": "12px",
                "box_shadow": "0 8px 32px rgba(0, 0, 0, 0.3)",
                "min_width": "160px",
            }
        )
    )
