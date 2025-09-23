import reflex as rx
from typing import Optional, Literal, Union
from utils.styles.modern_styles import (get_modern_button_styles, get_button_variant, get_button_size)

ButtonVariant = Literal["primary", "secondary", "outline", "ghost", "destructive"]
ButtonSize = Literal["xs", "sm", "md", "lg", "xl"]

def Button(
    children: Optional[Union[str, rx.Component]] = None,
    variant: ButtonVariant = "primary",
    size: ButtonSize = "md",
    loading: bool = False,
    disabled: bool = False,
    width: str = "auto",
    icon_left: Optional[str] = None,
    icon_right: Optional[str] = None,
    **props,
) -> rx.Component:
    
    # Base styles
    base_styles = get_modern_button_styles()
    var_config = get_button_variant(variant)
    size_config = get_button_size(size)

    # Merge all styles
    styles = {
        **base_styles,
        "background": var_config["bg"],
        "color": var_config["color"],
        "border": var_config["border"],
        "height": size_config["height"],
        "padding": size_config["padding"],
        "font_size": size_config["font_size"],
        "width": width,
        "min_width": "auto",
        "_hover": {
            **base_styles.get("_hover", {}),
            "background": var_config.get("hover_bg", var_config["bg"]),
            "color": var_config.get("hover_color", var_config["color"]),
        },
        "_disabled": {
            "opacity": "0.5",
            "cursor": "not-allowed",
            "pointer_events": "none",
        },
    }

    # Content builder
    content: list[rx.Component] = []
    
    if icon_left:
        content.append(rx.icon(icon_left, size=16, style={"margin_right": "8px" if children else "0"}))
    if loading:
        content.append(rx.spinner(size="1", style={"margin_right": "8px" if children else "0"}))
    if children:
        # If text, wrap in rx.text
        if isinstance(children, str):
            content.append(rx.text(children, style={"font_weight": "500"}))
        else:
            content.append(children)
    if icon_right:
        content.append(rx.icon(icon_right, size=16, style={"margin_left": "8px" if children else "0"}))

    # Guarantee content (avoid empty button)
    if not content:
        content = [rx.box()]

    final_content = rx.hstack(*content, align="center", spacing="0") if len(content) > 1 else content[0]

    return rx.button(
        final_content,
        style=styles,
        disabled=disabled or loading,
        aria_busy=str(loading).lower(),
        **props,
    )
