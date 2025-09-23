import reflex as rx
from ...state.auth_state import AuthState
from ..auth.auth_message import AuthMessage
from ..shared.button import Button
from .form_field import FormField
from .form_container import FormContainer
from ..shared.text import Text

def RegisterForm(show_logo: bool = False) -> rx.Component:
    """Modern register form using new component architecture."""
    
    return FormContainer(
        # Auth message
        AuthMessage(),
        
        # Username field
        FormField(
            label="Username",
            placeholder="Choose a username",
            value=AuthState.nickname,
            on_change=AuthState.set_nickname,
            type_="text",
            icon_left="user",
            required=True,
            helper_text="Choose a unique username for your account"
        ),
        
        # Email field (optional - you might want to add this to your state)
        # FormField(
        #     label="Email",
        #     placeholder="Enter your email",
        #     value=AuthState.email,
        #     on_change=AuthState.set_email,
        #     type_="email",
        #     icon_left="mail",
        #     required=True
        # ),
        
        # Password field
        FormField(
            label="Password",
            placeholder="Create a secure password",
            value=AuthState.password,
            on_change=AuthState.set_password,
            type_="password",
            icon_left="lock",
            required=True,
            helper_text="Password should be at least 8 characters long"
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
                Text("Already have an account?", variant="body", color="secondary"),
                rx.link(
                    "Sign in",
                    href="#",
                    style={
                        "color": "#0099CC",
                        "font_weight": "500",
                        "text_decoration": "none",
                        "transition": "color 0.2s ease",
                        "_hover": {
                            "color": "#0088BB",
                            "text_decoration": "underline"
                        }
                    },
                    on_click=lambda: rx.redirect("/login")  # You might want to use your page state instead
                ),
                spacing="2",
                align="center"
            ),
            width="100%",
            margin_top="16px"
        ),
        
        title="Create Account",
        subtitle="Join us and start managing your business",
        max_width="420px"
    )
