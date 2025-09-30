import reflex as rx
from ..components.navigation.navbar import Navbar
from ..components.forms.login_form import LoginForm
from ..components.forms.register_form import RegisterForm
from ..components.hero.hero_section import HeroSection
from ..components.layout.containers import PageContainer, CenteredLayout
from ..components.layout.spa_layout import SPALayout
from ..state.page_state import PageState
from ..state.auth_state import AuthState
from ..state.app_state import AppState

# Import modern styling utilities  
from ..utils.styles import (
    colors, 
    spacing, 
    typography,
    get_card_styles,
    get_text_styles
)

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
                            style=get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
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
                style=get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                margin_bottom="24px"
            ),
            rx.grid(
                # Quick stats cards
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.icon("users", size=24, color=colors["primary"]),
                            rx.text("Clients", style=get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"])),
                            justify="between",
                            align="center",
                            width="100%"
                        ),
                        rx.text(
                            "0",
                            style={
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                "font_size": "32px",
                                "color": colors["text_primary"],
                            }
                        ),
                        spacing="3",
                        align="start",
                        width="100%"
                    ),
                    style=get_card_styles(),
                    padding="24px",
                    width="100%"
                ),
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.icon("shopping-bag", size=24, color=colors["primary"]),
                            rx.text("Orders", style=get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"])),
                            justify="between",
                            align="center",
                            width="100%"
                        ),
                        rx.text(
                            "0",
                            style={
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                "font_size": "32px",
                                "color": colors["text_primary"],
                            }
                        ),
                        spacing="3",
                        align="start",
                        width="100%"
                    ),
                    style=get_card_styles(),
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
    """Modern main page that switches between login/register and full SPA layout."""
    return rx.cond(
        AuthState.is_authenticated,
        # Show full SPA layout when authenticated
        SPALayout(),
        # Show login/register page when not authenticated
        PageContainer(
            Navbar(),
            CenteredLayout(
                HeroSection(
                    title="Bienvenido a IntegraQS",
                    subtitle="Un ERP moderno",
                    size="compact"
                ),
                _form_container(),
            ),
            on_mount=lambda: PageState.show_form("login"),
        )
    )
