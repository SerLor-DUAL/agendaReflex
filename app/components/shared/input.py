import reflex as rx
from typing import Literal, Optional
from ....utils.colorPallet.colorPallet import ColorPallet
from ....utils.styles.modern_styles import get_modern_input_styles

colors = ColorPallet().colors

InputSize = Literal["sm", "md", "lg"]
InputVariant = Literal["default", "filled", "flushed"]

def Input(
    placeholder: str = "",
    value = None,
    on_change = None,
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
    """
    Modern input component with multiple variants and states.
    
    Args:
        placeholder: Input placeholder text
        value: Input value
        on_change: Change handler
        type_: Input type (text, password, email, etc.)
        size: Input size
        variant: Input variant style
        disabled: Disabled state
        error: Error state
        icon_left: Icon on the left side
        icon_right: Icon on the right side
        width: Input width
        **props: Additional input props
    
    Returns:
        rx.Component: Styled input component
    """
    
    # Size configurations
    size_config = {
        "sm": {"height": "32px", "padding": "6px 12px", "font_size": "13px"},
        "md": {"height": "36px", "padding": "8px 16px", "font_size": "14px"},
        "lg": {"height": "40px", "padding": "10px 20px", "font_size": "15px"}
    }
    
    config = size_config[size]
    
    # Build input styles based on variant and state
    input_styles = {
        **get_modern_input_styles(colors),
        "height": config["height"],
        "padding": config["padding"],
        "font_size": config["font_size"],
        "width": width,
    }
    
    if variant == "filled":
        input_styles.update({
            "background": colors["surface"],
            "border": "none",
            "_focus": {
                "background": colors["cards"],
                "box_shadow": f"0 0 0 2px {colors['focus']}"
            }
        })
    elif variant == "flushed":
        input_styles.update({
            "background": "transparent",
            "border": "none",
            "border_bottom": f"1px solid {colors['border']}",
            "border_radius": "0",
            "_focus": {
                "border_bottom_color": colors["focus"],
                "box_shadow": f"0 1px 0 0 {colors['focus']}"
            }
        })
    
    if error:
        input_styles.update({
            "border_color": colors["error"],
            "_focus": {
                "border_color": colors["error"],
                "box_shadow": f"0 0 0 3px {colors['error']}33"
            }
        })
    
    if disabled:
        input_styles.update({
            "opacity": "0.5",
            "cursor": "not-allowed"
        })
    
    # Build input content
    input_children = []
    
    if icon_left:
        input_children.append(
            rx.input.slot(
                rx.icon(
                    icon_left, 
                    size=16,
                    color=colors["textMuted"],
                    style={"transition": "color 0.2s ease"}
                )
            )
        )
    
    if icon_right:
        input_children.append(
            rx.input.slot(
                rx.icon(
                    icon_right, 
                    size=16,
                    color=colors["textMuted"],
                    style={"transition": "color 0.2s ease"}
                ),
                side="right"
            )
        )
    
    return rx.input(
        *input_children,
        placeholder=placeholder,
        value=value,
        on_change=on_change,
        type=type_,
        disabled=disabled,
        style=input_styles,
        **props
    )
