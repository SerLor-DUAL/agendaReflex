import reflex as rx
from ..state.user_state import UserState
from .user_card import user_card

def user_list():
    return rx.cond(
        UserState.loading,
        rx.spinner(size="3"),
        rx.vstack(
            rx.foreach(UserState.users, user_card),
            spacing="4"
        )
    )
