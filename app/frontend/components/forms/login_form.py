import reflex as rx

def InputField(placeholder: str, type: str = "text") -> rx.Component:
    return rx.input(
                rx.input.slot(rx.icon("user")),
                placeholder="usuario@integraqs.es",
                type="email",
                size="3",
                width="100%",
                style={
                    "_hover" : {
                        "border_color": "blue",
                    }
                }
            ),

def LoginForm() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.center(
                rx.image(
                    src="/img/logo.png",
                    width="6em",
                    height="auto",
                    border_radius="25%",
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
                InputField(placeholder="usuario@integraqs.es", type="email"),
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
                rx.input(
                    rx.input.slot(rx.icon("lock")),
                    placeholder="Contraseña",
                    type="password",
                    size="3",
                    width="100%",
                ),
                spacing="2",
                width="100%",
            ),
            rx.button("Inicia Sesión", size="3", width="100%"),
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