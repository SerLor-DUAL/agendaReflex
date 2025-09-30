import reflex as rx
from ...state.auth_state import AuthState
from ...utils.styles import colors, spacing, typography

# Colors now imported directly from design system

def AuthAlert() -> rx.Component:
    """Simple auth alert component."""
    
    return rx.cond(
        AuthState.auth_message_text,
        rx.box(
            rx.hstack(
                rx.icon(
                    rx.cond(
                        AuthState.auth_message_color == "green",
                        "circle-check",
                        "circle-x"
                    ),
                    size=16,
                    color=rx.cond(
                        AuthState.auth_message_color == "green",
                        colors["success"],
                        colors["error"]
                    )
                ),
                rx.text(
                    AuthState.auth_message_text,
                    style={
                        "font_size": "14px",
                        "color": colors["text_primary"]
                    }
                ),
                spacing="2",
                align="center"
            ),
            style={
                "background": rx.cond(
                    AuthState.auth_message_color == "green",
                    f"{colors['success']}20",
                    f"{colors['error']}20"
                ),
                "border": rx.cond(
                    AuthState.auth_message_color == "green", 
                    f"1px solid {colors['success']}40",
                    f"1px solid {colors['error']}40"
                ),
                "border_radius": "8px",
                "padding": "12px",
                "margin_bottom": "16px",
                "animation": "fadeIn 0.3s ease-out"
            }
        )
    )
