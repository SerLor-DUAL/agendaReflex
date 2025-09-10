import reflex as rx

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
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Pricing"),
                        rx.menu.item("Contact"),
                    ),
                    justify="end",
                ),
                justify="between",
                align="center",
            ),
        ),
        align_content="center",
        background_color="#1F2937",
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
                    "background": "#2B7FFF",       
                },
                "_active": {
                    "background": "#1447E6",
                }
            },
            color="white",
            border="0px"
        ),
        background_color="#155DFC",
        href=url,
        underline="none",
    )