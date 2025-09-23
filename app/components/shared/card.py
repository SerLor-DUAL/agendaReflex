import reflex as rx
from typing import Literal, Optional
from ....utils.colorPallet.colorPallet import ColorPallet
from ....utils.styles.modern_styles import get_modern_card_styles

colors = ColorPallet().colors

CardVariant = Literal["default", "elevated", "outlined", "filled"]
CardSize = Literal["sm", "md", "lg"]

def Card(
    *children,
    variant: CardVariant = "default",
    size: CardSize = "md",
    hover: bool = True,
    **props
) -> rx.Component:
    """
    Modern card component with glassmorphism styling.
    
    Args:
        *children: Card content
        variant: Card style variant
        size: Card size
        hover: Enable hover effects
        **props: Additional card props
    
    Returns:
        rx.Component: Styled card component
    """
    
    # Size configurations
    size_config = {
        "sm": {"padding": "16px", "border_radius": "12px"},
        "md": {"padding": "24px", "border_radius": "16px"},
        "lg": {"padding": "32px", "border_radius": "20px"}
    }
    
    config = size_config[size]
    
    # Base card styles
    base_styles = {
        **get_modern_card_styles(colors),
        "padding": config["padding"],
        "border_radius": config["border_radius"],
        "width": "100%",
        "box_sizing": "border-box"
    }
    
    # Variant-specific styles
    if variant == "elevated":
        base_styles.update({
            "box_shadow": "0 12px 48px rgba(0, 0, 0, 0.4)",
            "_hover": {
                "transform": "translateY(-4px)",
                "box_shadow": "0 16px 64px rgba(0, 0, 0, 0.5)"
            } if hover else {}
        })
    elif variant == "outlined":
        base_styles.update({
            "background": "transparent",
            "border": f"2px solid {colors['border']}",
            "box_shadow": "none",
            "_hover": {
                "border_color": colors["borderLight"],
                "background": colors["glassBackground"]
            } if hover else {}
        })
    elif variant == "filled":
        base_styles.update({
            "background": colors["surface"],
            "backdrop_filter": "none",
            "_hover": {
                "background": colors["cards"]
            } if hover else {}
        })
    
    if not hover:
        base_styles.pop("_hover", None)
    
    # Remove style from props to avoid duplicate keyword argument
    cleaned_props = {k: v for k, v in props.items() if k != "style"}
    if "style" in props:
        # Merge props['style'] with base_styles, with props['style'] taking precedence
        merged_styles = {**base_styles, **props["style"]}
    else:
        merged_styles = base_styles

    return rx.box(
        *children,
        style=merged_styles,
        **cleaned_props
    )

def CardHeader(*children, **props) -> rx.Component:
    """Card header component."""
    return rx.vstack(
        *children,
        spacing="2",
        align="start",
        width="100%",
        margin_bottom="16px",
        **props
    )

def CardBody(*children, **props) -> rx.Component:
    """Card body component."""
    return rx.vstack(
        *children,
        spacing="4",
        align="start",
        width="100%",
        **props
    )

def CardFooter(*children, **props) -> rx.Component:
    """Card footer component."""
    return rx.hstack(
        *children,
        spacing="3",
        align="center",
        width="100%",
        margin_top="16px",
        **props
    )
