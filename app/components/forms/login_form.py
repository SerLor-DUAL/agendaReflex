import reflex as rx
from ...state.auth_state import AuthState
from ..auth.auth_message import AuthMessage
from ..shared.button import Button
from .form_field import FormField
from .form_container import FormContainer
from ..shared.text import Text
from ...utils.styles import colors, spacing, typography

# Colors now imported directly from design system

def LoginForm(show_logo: bool = False) -> rx.Component:
    """Modern login form using new component architecture."""
    
    return FormContainer(
        # Auth message
        AuthMessage(),
        
        # Username field
        FormField(
            label="Nombre",
            placeholder="Introduce tu nombre de usuario",
            value=AuthState.nickname,
            on_change=AuthState.set_nickname,
            type_="text",
            icon_left="user",
            required=True
        ),
        
        # Password field with forgot password link
        rx.vstack(
            rx.hstack(
                Text("Contraseña", variant="small", color="primary", weight="medium"),
                rx.link(
                    "¿Has olvidado tu contraseña?",
                    href="#",
                    style={
                        "font_size": "13px",
                        "color": colors["primary"],
                        "text_decoration": "none",
                        "transition": "color 0.2s ease",
                        "_hover": {
                            "color": colors["primary_hover"],
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
                placeholder="Introduce tu contraseña",
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
            "Inicia sesión",
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
                Text("¿No tienes cuenta?", variant="body", color="secondary"),
                rx.link(
                    "Sign up",
                    href="#",
                    style={
                        "color": colors["primary"],
                        "font_weight": "500",
                        "text_decoration": "none",
                        "transition": "color 0.2s ease",
                        "_hover": {
                            "color": colors["primary_hover"],
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
        
        title="Bienvenido",
        subtitle="Inicia sesión en tu cuenta para continuar",
        max_width="420px"
    )
