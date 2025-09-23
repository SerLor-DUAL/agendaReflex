import reflex as rx
from typing import Literal, Optional
from ....utils.colorPallet.colorPallet import ColorPallet
from ....utils.styles.modern_styles import get_modern_button_styles

colors = ColorPallet().colors

ButtonVariant = Literal["primary", "secondary", "outline", "ghost", "destructive"]
ButtonSize = Literal["xs", "sm", "md", "lg", "xl"]

def Button(
    children: Optional[str] = None,
    variant: ButtonVariant = "primary",
    size: ButtonSize = "md",
    loading: bool = False,
    disabled: bool = False,
    width: str = "auto",
    icon_left: Optional[str] = None,
    icon_right: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Modern button component with multiple variants and sizes.
    
    Args:
        children: Button text/content
        variant: Button style variant
        size: Button size
        loading: Loading state
        disabled: Disabled state
        width: Button width
        icon_left: Icon on the left side
        icon_right: Icon on the right side
        **props: Additional button props
    
    Returns:
        rx.Component: Styled button component
    """
    
    # Size configurations
    size_config = {
        "xs": {"height": "28px", "padding": "4px 8px", "font_size": "12px"},
        "sm": {"height": "32px", "padding": "6px 12px", "font_size": "13px"},
        "md": {"height": "36px", "padding": "8px 16px", "font_size": "14px"},
        "lg": {"height": "40px", "padding": "10px 20px", "font_size": "15px"},
        "xl": {"height": "44px", "padding": "12px 24px", "font_size": "16px"}
    }
    
    # Variant configurations
    variant_config = {
        "primary": {
            "background": colors["gradientPrimary"],
            "color": colors["text"],
            "border": "none",
            "hover_bg": colors["primaryHover"]
        },
        "secondary": {
            "background": colors["secondary"],
            "color": colors["textSecondary"],
            "border": f"1px solid {colors['border']}",
            "hover_bg": colors["surface"]
        },
        "outline": {
            "background": "transparent",
            "color": colors["primary"],
            "border": f"2px solid {colors['primary']}",
            "hover_bg": colors["primary"],
            "hover_color": colors["text"]
        },
        "ghost": {
            "background": "transparent",
            "color": colors["text"],
            "border": "none",
            "hover_bg": colors["surface"]
        },
        "destructive": {
            "background": colors["error"],
            "color": colors["text"],
            "border": "none",
            "hover_bg": "#DC2626"
        }
    }
    
    config = variant_config[variant]
    sizing = size_config[size]
    
    # Build button styles
    button_styles = {
        **get_modern_button_styles(colors),
        "background": config["background"],
        "color": config["color"],
        "border": config["border"],
        "height": sizing["height"],
        "padding": sizing["padding"],
        "font_size": sizing["font_size"],
        "min_width": "auto",
        "width": width,
        "_hover": {
            "background": config["hover_bg"],
            "color": config.get("hover_color", config["color"]),
            "transform": "translateY(-1px)",
            "box_shadow": f"0 4px 12px {colors['focusRing']}"
        },
        "_disabled": {
            "opacity": "0.5",
            "cursor": "not-allowed",
            "transform": "none"
        }
    }
    
    # Build button content
    button_content = []
    
    if icon_left:
        button_content.append(
            rx.icon(icon_left, size=16, style={"margin_right": "8px" if children else "0"})
        )
    
    button_content.append(
        rx.cond(
            loading,
            rx.spinner(size="1", style={"margin_right": "8px" if children else "0"}),
            rx.fragment(),
        )
    )
    
    if children:
        button_content.append(rx.text(children, style={"font_weight": "500"}))
    
    if icon_right:
        button_content.append(
            rx.icon(icon_right, size=16, style={"margin_left": "8px" if children else "0"})
        )
    
    return rx.button(
        rx.hstack(*button_content, align="center", spacing="0") if len(button_content) > 1 else button_content[0] if button_content else None,
        style=button_styles,
        disabled=disabled or loading,
        **props
    )
