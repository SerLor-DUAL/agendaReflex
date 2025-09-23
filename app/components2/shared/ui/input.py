import reflex as rx
from typing import Optional, Literal
from .modern_styles import get_modern_input_styles, get_input_variant, get_input_size

InputSize = Literal["sm", "md", "lg"]
InputVariant = Literal["default", "filled", "flushed"]

def Input(
    placeholder: str = "",
    value=None,
    on_change=None,
    type_: str = "text",
    size: InputSize = "md",
    variant: InputVariant = "default",
    disabled: bool = False,
    error: bool = False,
    icon_left: Optional[str] = None,
    icon_right: Optional[str] = None,
    width: str = "100%",
    **props
) -> rx.Component:

    base_styles = get_modern_input_styles()
    size_styles = get_input_size(size)
    var_styles = get_input_variant(variant)

    styles = {**base_styles, **size_styles, **var_styles, "width": width}

    if error:
        styles.update({"border_color": "#EF4444", "_focus": {"border_color": "#EF4444"}})
    if disabled:
        styles.update({"opacity": "0.5", "cursor": "not-allowed"})

    children = []
    if icon_left:
        children.append(rx.input.slot(rx.icon(icon_left, size=16)))
    if icon_right:
        children.append(rx.input.slot(rx.icon(icon_right, size=16), side="right"))

    return rx.input(*children, placeholder=placeholder, value=value, on_change=on_change, type=type_, disabled=disabled, style=styles, **props)
