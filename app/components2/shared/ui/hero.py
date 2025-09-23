import reflex as rx
from .modern_styles import get_modern_hero_styles

def Hero(*children, **props):
    """
    Generic Hero section for landing pages.
    """
    styles = get_modern_hero_styles()
    return rx.box(*children, style=styles, width="100%", **props)
