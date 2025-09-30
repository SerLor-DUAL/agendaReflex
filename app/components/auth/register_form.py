import reflex as rx
from ...state.auth_state import AuthState
from ..shared import Button, Card
from .form_field import FormField
from .alert import AuthAlert
from ...utils.styles import colors, spacing, typography

# Colors now imported directly from design system

def RegisterForm() -> rx.Component:
    """Clean modern register form."""
    
    return Card(
        rx.vstack(
            # Header
            rx.vstack(
                rx.heading(
                    "Create Account",
                    size="6",
                    style={
                        "color": colors["text_primary"],
                        "text_align": "center",
                        "font_weight": "700",
                        "margin_bottom": "8px"
                    }
                ),
                rx.text(
                    "Join us and start managing your business",
                    style={
                        "color": colors["text_secondary"],
                        "text_align": "center",
                        "font_size": "14px"
                    }
                ),
                spacing="1",
                align="center",
                width="100%",
                margin_bottom="24px"
            ),
            
            # Alert
            AuthAlert(),
            
            # Username field
            FormField(
                label="Username",
                placeholder="Choose a username",
                value=AuthState.nickname,
                on_change=AuthState.set_nickname,
                type_="text",
                icon_left="user",
                required=True
            ),
            
            # Password field
            FormField(
                label="Password",
                placeholder="Create a secure password",
                value=AuthState.password,
                on_change=AuthState.set_password,
                type_="password",
                icon_left="lock",
                required=True
            ),
            
            # Register button
            Button(
                "Create Account",
                variant="primary",
                size="lg",
                width="100%",
                loading=AuthState.loading,
                on_click=AuthState.register,
                icon_left="user-plus"
            ),
            
            # Login link
            rx.center(
                rx.hstack(
                    rx.text(
                        "Already have an account?",
                        style={
                            "color": colors["text_secondary"],
                            "font_size": "14px"
                        }
                    ),
                    rx.link(
                        "Sign in",
                        href="#",
                        style={
                            "color": colors["primary"],
                            "font_weight": "500",
                            "text_decoration": "none",
                            "font_size": "14px",
                            "_hover": {
                                "text_decoration": "underline"
                            }
                        }
                    ),
                    spacing="2",
                    align="center"
                ),
                width="100%",
                margin_top="16px"
            ),
            
            spacing="5",
            width="100%",
            align="start"
        ),
        size="lg",
        style={"max_width": "400px"}
    )
