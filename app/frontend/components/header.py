import reflex as rx
from ..state.user_state import UserState

def header():
    return rx.hstack(
        rx.heading("agendaReflex", size="6"),
        rx.spacer(),
        rx.button(
            "Cargar Usuarios",
            on_click=UserState.load_users,
            loading=UserState.loading
        ),
        width="100%",
        padding="1rem",
        bg="blue.50",
        border_radius="md",
    )
