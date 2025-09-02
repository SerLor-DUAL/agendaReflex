# src/frontend/pages/main_page.py

import reflex as rx
from ..components.header import header
from ..components.user_list import user_list
from ..state.user_state import UserState

def main_page():
    return rx.container(
        rx.vstack(
            header(),
            rx.cond(
                UserState.message != "",
                rx.callout(
                    UserState.message,
                    icon="info",
                    color_scheme="blue"
                )
            ),
            user_list(),
            spacing="6",
            align="center"
        ),
        max_width="1200px",
        padding="2rem"
    )
