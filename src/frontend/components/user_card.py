import reflex as rx

def user_card(user: dict):
    return rx.card(
        rx.vstack(
            rx.heading(user["nickname"], size="4"),
            rx.text(f"ID: {user['id']}", color="gray.500"),
            align="start",
            spacing="2"
        ),
        width="300px"
    )