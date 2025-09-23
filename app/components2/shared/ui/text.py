import reflex as rx
from typing import Literal, Optional
from .modern_styles import get_modern_text_styles

TextVariant = Literal["h1", "h2", "h3", "h4", "h5", "h6", "body", "small", "caption", "overline"]
TextColor = Literal["primary", "secondary", "muted", "disabled", "error", "success", "warning"]

def Text(
    children: str = "",
    variant: TextVariant = "body",
    color: Optional[TextColor] = None,
    align: Literal["left", "center", "right"] = "left",
    weight: Literal["light", "normal", "medium", "semibold", "bold", "extrabold"] = "normal",
    **props
) -> rx.Component:

    styles = get_modern_text_styles(variant)
    styles["text_align"] = align
    styles["font_weight"] = weight
    if color:
        styles["color"] = color

    return rx.text(children, style=styles, **props)
