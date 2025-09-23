import reflex as rx
from typing import Literal, Union
from utils.styles.modern_styles import get_modern_badge_styles

BadgeVariant = Literal["primary", "secondary", "success", "warning", "error"]

def Badge(children: Union[str, rx.Component], variant: BadgeVariant = "primary", size: Literal["sm", "md", "lg"] = "md", rounded: bool = True, **props,) -> rx.Component:
    """Badge/label component with variants and sizes."""

    base_styles = get_modern_badge_styles(variant)

    size_styles = {
        "sm": {"font_size": "10px", "padding": "2px 6px"},
        "md": {"font_size": "12px", "padding": "4px 8px"},
        "lg": {"font_size": "14px", "padding": "6px 10px"},
    }[size]

    styles = {
        **base_styles,
        **size_styles,
        "border_radius": "9999px" if rounded else "6px",
        "display": "inline-flex",
        "align_items": "center",
        "font_weight": "500",
        "white_space": "nowrap",
    }

    return rx.box(children, role="status", style=styles, **props)
