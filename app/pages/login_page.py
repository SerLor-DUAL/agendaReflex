import reflex as rx
from ..components.forms.login_form import LoginForm
from ..components.templates.auth_page import LoginPageTemplate
from ..state.page_state import PageState

def LoginPage() -> rx.Component:
    """Modern login page using template system."""
    
    return LoginPageTemplate(
        LoginForm(),
        on_mount=lambda: PageState.show_form("login")
    )
