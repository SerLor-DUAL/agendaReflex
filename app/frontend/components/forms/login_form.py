import reflex as rx
# Import state and needed functions
from ...state.auth_state import AuthState
from ..auth.auth_message import AuthMessage

# Import the ColorPallete class to access color definitions.
from ...utils.colorPallet.colorPallet import ColorPallet

# Import components
from ..forms.primaryBtn import PrimaryBtn

colors = ColorPallet().colors

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
                },
                background_color=colors["textSecondary"],
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
                    color=colors["background"],
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
                    color=colors["background"],
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
                        color=colors["background"],
                    ),
                    rx.link(
                        "Olvidé mi contraseña",
                        href="#",
                        size="3",
                        underline=None,
                        color=colors["primary"],

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
            PrimaryBtn(
                text="Inicia Sesión", 
                size="3",
                width="100%",
                style={
                    "cursor": "pointer",
                    "transition": "all 0.3s ease",
                    "_hover": {
                                "bg": colors["primaryHover"],
                            },
                    "_active": {
                                "bg": colors["primaryActive"],
                                }
                },
                type_="submit",
                background_color=colors["primary"],
                loading=AuthState.loading,
                on_click=AuthState.login,
                ),
            rx.button(
                "Inicia Sesión", 
                size="3", 
                width="100%",
                type_="submit",
                style={
                    "cursor": "pointer",
                    "transition": "all 0.3s ease",
                    "_hover": {
                                "bg": colors["primaryHover"],
                            },
                    "_active": {
                                "bg": colors["primaryActive"],
                                }
                },
                background_color=colors["primary"],
                loading=AuthState.loading,
                on_click=AuthState.login,),
            rx.center(
                rx.link("Registrate", href="#", size="3"),
                opacity="0.8",
                spacing="2",
                direction="row",
                width="100%",
                color=colors["primary"],
                underline="none",
                style={
                    "cursor": "pointer",
                    "transition": "all 0.3s ease",
                    "_hover": {
                                "color": colors["primaryHover"],
                            }
                }
            ),
            spacing="6",
            width="100%",
        ),
        max_width="28em",
        size="4",
        width="100%",
        background_color=colors["text"],
    )