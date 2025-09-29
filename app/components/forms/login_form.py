import reflex as rx
from ...state.auth_state import AuthState
from ..auth.auth_message import AuthMessage
from ..shared.button import Button
from .form_field import FormField
from .form_container import FormContainer
from ..shared.text import Text
from ...utils.styles.colorPallet import ColorPallet

colors = ColorPallet().colors

def LoginForm(show_logo: bool = False) -> rx.Component:
    """Modern login form using new component architecture."""
    
    return FormContainer(
        # Auth message
        AuthMessage(),
        
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
        
        # Password field with forgot password link
        rx.vstack(
            rx.hstack(
                Text("Password*", variant="small", color="primary", weight="medium"),
                rx.link(
                    "Forgot password?",
                    href="#",
                    style={
                        "font_size": "13px",
                        "color": colors["primary"],
                        "text_decoration": "none",
                        "transition": "color 0.2s ease",
                        "_hover": {
                            "color": colors["primaryHover"],
                            "text_decoration": "underline"
                        }
                    }
                ),
                justify="between",
                align="center",
                width="100%"
            ),
            FormField(
                label="",  # Empty since handled above
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
                Text("Don't have an account?", variant="body", color="secondary"),
                rx.link(
                    "Sign up",
                    href="#",
                    style={
                        "color": colors["primary"],
                        "font_weight": "500",
                        "text_decoration": "none",
                        "transition": "color 0.2s ease",
                        "_hover": {
                            "color": colors["primaryHover"],
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
        
        title="Welcome Back",
        subtitle="Sign in to your account to continue",
        max_width="420px"
    )
