import reflex as rx
from ...state.page_state import PageState
from ..shared.button import Button

def AuthButtons() -> rx.Component:
    """
    Authentication buttons for unauthenticated users.
    
    Returns:
        rx.Component: Sign In and Sign Up buttons
    """
    
    return rx.hstack(
        Button(
            "Sign In",
            variant="outline",
            size="md",
            width="auto",
            on_click=lambda: PageState.show_form("login"),
            icon_left="log-in"
        ),
        Button(
            "Sign Up",
            variant="primary",
            size="md",
            width="auto",
            on_click=lambda: PageState.show_form("register"),
            icon_left="user-plus"
        ),
        spacing="3",
        align="center",
        justify="center"
    )
