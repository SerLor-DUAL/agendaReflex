import reflex as rx
from ...state.auth_state import AuthState
from .auth_message import AuthMessage

def LoginForm():

    return rx.form(
        rx.vstack(
            # Nickname input
            rx.input(
                placeholder="Nickname",
                value=AuthState.nickname,
                on_change=AuthState.set_nickname,
                width="100%",
            ),
            
            # Password input
            rx.input(
                placeholder="Password",
                type_="password",
                value=AuthState.password,
                on_change=AuthState.set_password,
                width="100%",
            ),
            
            # Login button
            rx.button(
                "Login",
                type_="submit",
                loading=AuthState.loading,
                width="100%",
                # on_click=AuthState.login,
            ),
            
            # Logout button solo si está logueado
            rx.cond(
                AuthState.is_authenticated,
                rx.button(
                    "Logout",
                    on_click=AuthState.logout,
                    width="100%",
                    color_scheme="red",
                ),
                None
            ),
            
            AuthMessage()

        ),
        padding="1rem",
        width="400px",
        border_radius="md",
        box_shadow="md",
        on_submit=AuthState.login
    )
