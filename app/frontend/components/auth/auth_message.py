import reflex as rx
from ...state.auth_state import AuthState

def AuthMessage():
    
    return rx.cond(
        AuthState.auth_message_text,            # solo se muestra si hay texto
        rx.text(
            AuthState.auth_message_text,        # texto reactivo
            color=AuthState.auth_message_color  # color reactivo
        ),
        rx.fragment(),  # nada si es None
        
        # Limpiar mensaje después de 3 segundos si es éxito
        # rx.interval(
        #     3000,
        #     AuthState.clear_success_message.temporal
        # )
    )