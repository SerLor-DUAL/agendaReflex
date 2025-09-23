import reflex as rx
from .modern_styles import get_modern_modal_styles

def Modal(*children, open: bool = False, **props):
    """
    Generic modal component using modern styles.
    """
    styles = get_modern_modal_styles()
    return rx.box(*children, style=styles, display="block" if open else "none", **props)
