import reflex as rx
from ..components.navigation.navbar import Navbar
from ..components.forms.login_form import LoginForm
from ..components.forms.register_form import RegisterForm
from ..components.hero.hero_section import HeroSection
from ..components.layout.containers import PageContainer, CenteredLayout
from ..state.page_state import PageState
from ..state.auth_state import AuthState

# Import modern styling utilities
from ..utils.colorPallet.colorPallet import ColorPallet
from ..utils.styles.modern_styles import get_modern_card_styles, get_modern_text_styles

colors = ColorPallet().colors

def _form_container() -> rx.Component:
    """Modern form container with conditional forms."""
    return rx.center(
        rx.box(
            rx.cond(
                PageState.current_form == "login",
                LoginForm(),
                rx.cond(
                    PageState.current_form == "register",
                    RegisterForm(),
                    rx.center(
                        rx.text(
                            "Welcome! Please sign in to continue.",
                            style=get_modern_text_styles(colors, "body"),
                            text_align="center"
                        ),
                        padding="2rem"
                    ),
                ),
            ),
            width="100%",
            max_width="420px",
            style={
                "animation": "fadeIn 0.5s ease-in-out"
            }
        ),
        width="100%",
    )

def _dashboard_content() -> rx.Component:
    """Dashboard content for authenticated users."""
    return rx.center(
        rx.vstack(
            rx.heading(
                "Dashboard",
                size="6",
                style=get_modern_text_styles(colors, "heading"),
                margin_bottom="24px"
            ),
            rx.grid(
                # Quick stats cards
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.icon("users", size=24, color=colors["primary"]),
                            rx.text("Clients", style=get_modern_text_styles(colors, "subheading")),
                            justify="between",
                            align="center",
                            width="100%"
                        ),
                        rx.text(
                            "0",
                            style={
                                **get_modern_text_styles(colors, "heading"),
                                "font_size": "32px",
                                "color": colors["text"],
                            }
                        ),
                        spacing="3",
                        align="start",
                        width="100%"
                    ),
                    style=get_modern_card_styles(colors),
                    padding="24px",
                    width="100%"
                ),
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.icon("shopping-bag", size=24, color=colors["primary"]),
                            rx.text("Orders", style=get_modern_text_styles(colors, "subheading")),
                            justify="between",
                            align="center",
                            width="100%"
                        ),
                        rx.text(
                            "0",
                            style={
                                **get_modern_text_styles(colors, "heading"),
                                "font_size": "32px",
                                "color": colors["text"],
                            }
                        ),
                        spacing="3",
                        align="start",
                        width="100%"
                    ),
                    style=get_modern_card_styles(colors),
                    padding="24px",
                    width="100%"
                ),
                columns="2",
                spacing="4",
                width="100%",
                max_width="600px"
            ),
            spacing="6",
            align="center",
            width="100%"
        ),
        width="100%",
        min_height="60vh",
        padding="2rem"
    )

def MainPage() -> rx.Component:
    """Modern modular main page with clean component structure."""
    return PageContainer(
        Navbar(),
        rx.box(
            rx.cond(
                AuthState.is_authenticated,
                _dashboard_content(),
                CenteredLayout(
                    HeroSection(
                        title="Bienvenido a IntegraQS",
                        subtitle="Un ERP moderno",
                        size="compact"
                    ),
                    _form_container(),
                )
            ),
            on_mount=lambda: PageState.show_form("login"),
        )
    )
