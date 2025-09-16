import reflex as rx
from ...state.auth_state import AuthState

def RegisterForm():
    
    return rx.form(
        
        # Nickname input
        rx.input(
            placeholder="Nickname",
            value=AuthState.nickname,
            on_change=AuthState.set_nickname
        ),
        
        # Password input
        rx.input(
            placeholder="Password",
            type_="password",
            value=AuthState.password,
            on_change=AuthState.set_password
        ),
        
        # Register Button
        rx.button(
            "Register",
            type_="submit",         
            loading=AuthState.loading
        ),
        
        # Error message display
        rx.cond(
            AuthState.message != "",
            rx.text(AuthState.message, color="red"),
            None
        ),
        
        padding="1rem",
        width="100%",
        border_radius="md",
        box_shadow="md",
        on_submit=AuthState.register
    )
