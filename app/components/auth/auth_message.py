import reflex as rx
from ...state.auth_state import AuthState
from ..shared.alert import Alert

def AuthMessage() -> rx.Component:
    """
    Modern auth message component using Alert UI component.
    
    Returns:
        rx.Component: Alert component showing auth messages
    """
    
    return rx.cond(
        AuthState.auth_message_text,
        Alert(
            AuthState.auth_message_text,
            variant=rx.cond(
                AuthState.auth_message_color == "green",
                "success",
                rx.cond(
                    AuthState.auth_message_color == "red",
                    "error", 
                    "info"
                )
            ),
            size="md",
            dismissible=True,
            style={
                "margin_bottom": "16px",
                "animation": "fadeIn 0.3s ease-out"
            }
        ),
        rx.fragment()  # Nothing if no message
    )
