import reflex as rx
from ...utils.colorPallet.colorPallet import ColorPallet

# Get colors from ColorPallete class
colors = ColorPallet().colors

def Navbar(sCompanyName: str = "IntegraQS"):
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/img/logo.png",
                        width="4em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        sCompanyName, 
                        size="8", 
                        weight="bold",
                        color="white"
                    ),
                    align="center",
                ),
                rx.hstack(
                    navbar_link("Iniciar Sesión", "/#"),
                    navbar_link("Registrarse", "/#"),
                    justify="end",
                    spacing="5",
                    align="center",
                ),
                justify="between",
                align="center",
            ),
        ),
        
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/img/logo.png",
                        width="4em",
                        height="auto",
                        border_radius="25%",
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", 
                                size=30,
                                color=colors["text"],
                                style={
                                    "cursor": "pointer",
                                    "transition": "all 0.3s ease",
                                    "_hover": {
                                                "color": colors["primary"],
                                            }
                                })
                    ),
                    rx.menu.content(
                        rx.menu.item("Iniciar Sesión"),
                        rx.menu.item("Registrarse"),
                        variant="soft",
                        color_scheme="blue",
                        background_color=colors["background"],
                        color=colors["text"],
                    ),
                    justify="end",
                    
                ),
                justify="between",
                align="center",
            ),
        ),
        align_content="center",
        background_color=colors["background"], 
        padding="1em",
        width="100%",
        height="6em",
    )

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            text,
            size="3",
            variant="surface", 
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
            color=colors["text"],
        ),

        underline="none",
    )