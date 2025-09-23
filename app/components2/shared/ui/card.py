import reflex as rx
from typing import Literal
from utils.styles.modern_styles import get_modern_card_styles, get_card_variant, get_card_size

CardVariant = Literal["default", "elevated", "outlined", "filled"]
CardSize = Literal["sm", "md", "lg"]

def Card(*children, variant: CardVariant = "default", size: CardSize = "md", hover: bool = True, **props,) -> rx.Component:
    """Card container with variants, sizes, and optional hover effects."""
    
    base_styles = get_modern_card_styles()
    var_styles = get_card_variant(variant)
    size_styles = get_card_size(size)

    styles = {**base_styles, **var_styles, **size_styles}
    if not hover:
        styles.pop("_hover", None)

    return rx.box(*children, style=styles, **props)

def CardHeader(*children, **props) -> rx.Component:
    """Card header section (usually title, subtitle, actions)."""
    
    return rx.vstack(
        *children,
        spacing="2",
        align="start",
        width="100%",
        margin_bottom="16px",
        **props,
    )

def CardBody(*children, **props) -> rx.Component:
    """Card body section (main content)."""
    
    return rx.vstack(
        *children,
        spacing="4",
        align="start",
        width="100%",
        **props,
    )

def CardFooter(*children, **props) -> rx.Component:
    """Card footer section (buttons, links, metadata)."""
    
    return rx.hstack(
        *children,
        spacing="3",
        align="center",
        width="100%",
        margin_top="16px",
        **props,
    )
