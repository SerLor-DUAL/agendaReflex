import reflex as rx
from typing import Literal, Optional
from ...utils.colorPallet.colorPallet import ColorPallet
from ...utils.styles.modern_styles import get_modern_text_styles

colors = ColorPallet().colors

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
    """
    Modern text component with typography variants.
    
    Args:
        children: Text content
        variant: Typography variant
        color: Text color variant
        align: Text alignment
        weight: Font weight
        **props: Additional text props
    
    Returns:
        rx.Component: Styled text component
    """
    
    # Variant configurations
    variant_config = {
        "h1": {"size": "9", "component": "heading", "font_weight": "800"},
        "h2": {"size": "8", "component": "heading", "font_weight": "700"},
        "h3": {"size": "7", "component": "heading", "font_weight": "600"},
        "h4": {"size": "6", "component": "heading", "font_weight": "600"},
        "h5": {"size": "5", "component": "heading", "font_weight": "500"},
        "h6": {"size": "4", "component": "heading", "font_weight": "500"},
        "body": {"size": "3", "component": "text", "font_weight": "400"},
        "small": {"size": "2", "component": "text", "font_weight": "400"},
        "caption": {"size": "1", "component": "text", "font_weight": "400"},
        "overline": {"size": "1", "component": "text", "font_weight": "500", "text_transform": "uppercase", "letter_spacing": "0.1em"}
    }
    
    # Color configurations
    color_config = {
        "primary": colors["text"],
        "secondary": colors["textSecondary"],
        "muted": colors["textMuted"],
        "disabled": colors["textDisabled"],
        "error": colors["error"],
        "success": colors["success"],
        "warning": colors["warning"]
    }
    
    config = variant_config[variant]
    component_type = config["component"]
    
    # Build text styles
    text_styles = {
        "color": color_config.get(color, colors["text"]),
        "text_align": align,
        "font_weight": config.get("font_weight", weight),
        "line_height": "1.5",
        "letter_spacing": "-0.025em"
    }
    
    # Add variant-specific styles
    if "text_transform" in config:
        text_styles["text_transform"] = config["text_transform"]
    if "letter_spacing" in config:
        text_styles["letter_spacing"] = config["letter_spacing"]
    
    # Create component based on type
    if component_type == "heading":
        return rx.heading(
            children,
            size=config["size"],
            style=text_styles,
            **props
        )
    else:
        return rx.text(
            children,
            size=config["size"],
            style=text_styles,
            **props
        )
