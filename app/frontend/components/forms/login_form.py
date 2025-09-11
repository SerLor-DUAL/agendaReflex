import reflex as rx
# Import state and needed functions
from ...state.auth_state import AuthState
from ..auth.auth_message import AuthMessage


def InputField(placeholder: str, value, on_change, type: str = "text") -> rx.Component:
    return rx.input(
                rx.input.slot(rx.icon("user")),
                placeholder="usuario@integraqs.es",
                value=value,
                on_change=on_change,
                type="email",
                size="3",
                width="100%",
                style={
                    "_hover" : {
                        "border_color": "blue",
                    }
                }
            ),

def LoginForm(image: bool = False) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.center(
                # If image is set to True, display the logo image
                rx.cond(
                    image,
                    rx.image(
                        src="/img/logo.png",
                        width="6em",
                        height="auto",
                        border_radius="25%",
                    ),
                ),
                rx.heading(
                    "Iniciar Sesión",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                direction="column",
                spacing="5",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Correo Electrónico",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                InputField(
                    placeholder="usuario@integraqs.es", 
                    type="email", 
                    value=AuthState.nickname,
                    on_change=AuthState.set_nickname
                    ),
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Contraseña",
                        size="3",
                        weight="medium",
                    ),
                    rx.link(
                        "Olvidé mi contraseña",
                        href="#",
                        size="3",
                    ),
                    justify="between",
                    width="100%",
                ),
                InputField(
                    placeholder="usuario@integraqs.es", 
                    type="email", 
                    value=AuthState.password,
                    on_change=AuthState.set_password,
                    ),
                # rx.input(
                #     rx.input.slot(rx.icon("lock")),
                #     placeholder="Contraseña",
                #     type="password",
                #     size="3",
                #     width="100%",
                # ),
                spacing="2",
                width="100%",
            ),
            rx.button(
                "Inicia Sesión", 
                size="3", 
                width="100%",
                type_="submit",
                loading=AuthState.loading,
                width="100%",
                on_click=AuthState.login,),
            rx.center(
                rx.link("Registrate", href="#", size="3"),
                opacity="0.8",
                spacing="2",
                direction="row",
                width="100%",
            ),
            spacing="6",
            width="100%",
        ),
        max_width="28em",
        size="4",
        width="100%",
    )