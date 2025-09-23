import reflex as rx
from ...state.auth_state import AuthState
from ..shared.ui import Button, Card
from .form_field import FormField
from .alert import AuthAlert
from ...utils.colorPallet.colorPallet import ColorPallet

colors = ColorPallet().colors

def LoginForm() -> rx.Component:
    """Clean modern login form."""
    
    return Card(
        rx.vstack(
            # Header
            rx.vstack(
                rx.heading(
                    "Welcome Back",
                    size="6",
                    style={
                        "color": colors["text"],
                        "text_align": "center",
                        "font_weight": "700",
                        "margin_bottom": "8px"
                    }
                ),
                rx.text(
                    "Sign in to continue",
                    style={
                        "color": colors["textSecondary"],
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
                placeholder="Enter your username",
                value=AuthState.nickname,
                on_change=AuthState.set_nickname,
                type_="text",
                icon_left="user",
                required=True
            ),
            
            # Password field
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Password*",
                        style={
                            "font_size": "14px",
                            "font_weight": "500",
                            "color": colors["text"]
                        }
                    ),
                    rx.link(
                        "Forgot password?",
                        href="#",
                        style={
                            "font_size": "13px",
                            "color": colors["primary"],
                            "text_decoration": "none",
                            "_hover": {
                                "text_decoration": "underline"
                            }
                        }
                    ),
                    justify="between",
                    align="center",
                    width="100%"
                ),
                FormField(
                    label="",
                    placeholder="Enter your password",
                    value=AuthState.password,
                    on_change=AuthState.set_password,
                    type_="password",
                    icon_left="lock",
                    required=True
                ),
                spacing="1",
                width="100%",
                align="start"
            ),
            
            # Login button
            Button(
                "Sign In",
                variant="primary",
                size="lg",
                width="100%",
                loading=AuthState.loading,
                on_click=AuthState.login,
                icon_left="log-in"
            ),
            
            # Register link
            rx.center(
                rx.hstack(
                    rx.text(
                        "Don't have an account?",
                        style={
                            "color": colors["textSecondary"],
                            "font_size": "14px"
                        }
                    ),
                    rx.link(
                        "Sign up",
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
