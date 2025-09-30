import reflex as rx
from ...utils.styles import colors, spacing, typography, get_card_styles, get_button_styles

# Colors now imported directly from design system

def PageContainer(*children, **kwargs) -> rx.Component:
    """
    Main page container with consistent styling.
    
    Args:
        *children: Child components
        **kwargs: Additional container props
    
    Returns:
        rx.Component: Styled page container
    """
    
    default_style = {
        "width": "100%",
        "min_height": "100vh",
        "background": colors["background"],
        "box_sizing": "border-box",
        "font_family": "Inter, system-ui, -apple-system, sans-serif",
    }
    
    # Merge with custom styles if provided
    style = kwargs.pop("style", {})
    final_style = {**default_style, **style}
    
    return rx.box(
        *children,
        style=final_style,
        **kwargs
    )

def ContentContainer(*children, max_width: str = "1200px", **kwargs) -> rx.Component:
    """
    Content container with max width and centering.
    
    Args:
        *children: Child components
        max_width: Maximum container width
        **kwargs: Additional container props
    
    Returns:
        rx.Component: Centered content container
    """
    
    default_style = {
        "width": "100%",
        "max_width": max_width,
        "margin": "0 auto",
        "padding": "2rem",
        "box_sizing": "border-box"
    }
    
    style = kwargs.pop("style", {})
    final_style = {**default_style, **style}
    
    return rx.box(
        *children,
        style=final_style,
        **kwargs
    )

def CardContainer(*children, **kwargs) -> rx.Component:
    """
    Modern card container with glassmorphism styling.
    
    Args:
        *children: Child components
        **kwargs: Additional card props
    
    Returns:
        rx.Component: Styled card container
    """
    
    default_style = {
        **get_card_styles(),
        "padding": "32px",
        "width": "100%",
        "max_width": "400px"
    }
    
    style = kwargs.pop("style", {})
    final_style = {**default_style, **style}
    
    return rx.box(
        *children,
        style=final_style,
        **kwargs
    )

def CenteredLayout(*children, **kwargs) -> rx.Component:
    """
    Centered layout for forms and content.
    
    Args:
        *children: Child components
        **kwargs: Additional layout props
    
    Returns:
        rx.Component: Centered layout container
    """
    
    return rx.vstack(
        *children,
        spacing="4",
        align="center",
        width="100%",
        padding="1.5rem",
        min_height="calc(100vh - 72px)",  # Account for navbar height
        justify="center",
        style={
            "max_width": "800px",
            "margin": "0 auto"
        },
        **kwargs
    )
