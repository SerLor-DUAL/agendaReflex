"""
Card Component

This module provides reusable Card components that leverage the design system
for consistent styling throughout the application.
"""

import reflex as rx
from typing import List, Union, Optional, Any

# Import styles from the design system
from app.utils.styles import get_card_styles, spacing, colors, typography

def Card(
    children: Union[List[rx.Component], rx.Component],
    variant: str = "default",
    padding: str = "md",
    hoverable: bool = False,
    elevated: bool = False,
    class_name: Optional[str] = None,
    **kwargs
) -> rx.Component:
    """
    Basic Card component following the design system.
    
    Args:
        children: Card content components
        variant: Card style variant (default, outline, filled)
        padding: Card padding size token (xs, sm, md, lg, xl)
        hoverable: Whether card should have hover effects
        elevated: Whether card should have elevation shadow
        class_name: Additional CSS class names
        **kwargs: Additional props to pass to the card element
        
    Returns:
        A styled Card component
    """
    # Get style dictionary based on props
    card_styles = get_card_styles(
        variant=variant,
        padding=padding,
        hoverable=hoverable,
        elevated=elevated
    )
    
    # Merge additional styles from kwargs
    if "style" in kwargs:
        for key, value in kwargs["style"].items():
            card_styles[key] = value
        kwargs.pop("style")
    
    # Return the card component
    return rx.box(
        children,
        style=card_styles,
        class_name=class_name,
        **kwargs
    )

def CardHeader(
    children: Union[str, List[rx.Component], rx.Component],
    title: Optional[str] = None,
    subtitle: Optional[str] = None,
    actions: Optional[List[rx.Component]] = None,
    class_name: Optional[str] = None,
    **kwargs
) -> rx.Component:
    """
    Card Header component for consistent card layouts.
    
    Args:
        children: Custom header content (overrides title/subtitle)
        title: Header title text
        subtitle: Header subtitle text  
        actions: Optional action components (buttons, icons)
        class_name: Additional CSS class names
        **kwargs: Additional props to pass to the header element
        
    Returns:
        A styled CardHeader component
    """
    header_styles = {
        "display": "flex",
        "align_items": "flex-start",
        "justify_content": "space-between",
        "margin_bottom": spacing["md"],
    }
    
    # If custom children provided, use them
    if not isinstance(children, str) and children is not None:
        return rx.box(
            children,
            style=header_styles,
            class_name=class_name,
            **kwargs
        )
    
    # Build header content from title/subtitle
    title_content = []
    
    if title:
        title_content.append(
            rx.heading(
                title,
                size="5",
                color=colors["text_primary"],
                font_weight=typography["weights"]["semibold"],
                line_height="1.2"
            )
        )
    
    if subtitle:
        title_content.append(
            rx.text(
                subtitle,
                size="2",
                color=colors["text_secondary"],
                margin_top=spacing["xs"]
            )
        )
    
    # Create title section
    title_section = rx.box(
        *title_content,
        flex="1"
    )
    
    # Create actions section if provided
    actions_section = None
    if actions:
        actions_section = rx.box(
            *actions,
            display="flex",
            gap=spacing["xs"],
            align_items="center"
        )
    
    # Combine sections
    header_content = [title_section]
    if actions_section:
        header_content.append(actions_section)
    
    return rx.box(
        *header_content,
        style=header_styles,
        class_name=class_name,
        **kwargs
    )

def CardBody(
    children: Union[List[rx.Component], rx.Component],
    class_name: Optional[str] = None,
    **kwargs
) -> rx.Component:
    """
    Card Body component for consistent card content areas.
    
    Args:
        children: Body content components
        class_name: Additional CSS class names
        **kwargs: Additional props to pass to the body element
        
    Returns:
        A styled CardBody component
    """
    body_styles = {
        "flex": "1",
    }
    
    return rx.box(
        children,
        style=body_styles,
        class_name=class_name,
        **kwargs
    )

def CardFooter(
    children: Union[List[rx.Component], rx.Component],
    align: str = "right",
    class_name: Optional[str] = None,
    **kwargs
) -> rx.Component:
    """
    Card Footer component for consistent card action areas.
    
    Args:
        children: Footer content components (typically buttons)
        align: Footer content alignment (left, center, right, space-between)
        class_name: Additional CSS class names
        **kwargs: Additional props to pass to the footer element
        
    Returns:
        A styled CardFooter component
    """
    justify_content_map = {
        "left": "flex-start",
        "center": "center", 
        "right": "flex-end",
        "space-between": "space-between"
    }
    
    footer_styles = {
        "display": "flex",
        "align_items": "center",
        "justify_content": justify_content_map.get(align, "flex-end"),
        "gap": spacing["sm"],
        "margin_top": spacing["md"],
        "padding_top": spacing["md"],
        "border_top": f"1px solid {colors['border']}",
    }
    
    return rx.box(
        children,
        style=footer_styles,
        class_name=class_name,
        **kwargs
    )

def StatsCard(
    title: str,
    value: Union[str, int, float],
    subtitle: Optional[str] = None,
    icon: Optional[str] = None,
    trend: Optional[str] = None,
    trend_value: Optional[str] = None,
    variant: str = "default",
    class_name: Optional[str] = None,
    **kwargs
) -> rx.Component:
    """
    Specialized Stats Card for displaying key metrics.
    
    Args:
        title: Stat title/label
        value: Main stat value
        subtitle: Optional subtitle/description
        icon: Optional icon name
        trend: Trend direction (up, down, neutral)
        trend_value: Trend change value (e.g., "+5.2%")
        variant: Card style variant
        class_name: Additional CSS class names
        **kwargs: Additional props
        
    Returns:
        A styled StatsCard component
    """
    # Trend colors
    trend_colors = {
        "up": colors["success"],
        "down": colors["error"],
        "neutral": colors["text_muted"]
    }
    
    # Trend icons
    trend_icons = {
        "up": "trending-up",
        "down": "trending-down", 
        "neutral": "minus"
    }
    
    # Card content
    card_content = []
    
    # Header with title and icon
    header_content = []
    if icon:
        header_content.append(
            rx.icon(icon, font_size="20px", color=colors["accent"])
        )
    header_content.append(
        rx.text(
            title,
            size="2",
            color=colors["text_secondary"],
            font_weight=typography["weights"]["medium"]
        )
    )
    
    card_content.append(
        rx.box(
            *header_content,
            display="flex",
            align_items="center",
            gap=spacing["xs"],
            margin_bottom=spacing["sm"]
        )
    )
    
    # Main value
    card_content.append(
        rx.heading(
            str(value),
            size="6",
            color=colors["text_primary"],
            font_weight=typography["weights"]["bold"],
            line_height="1"
        )
    )
    
    # Bottom section with subtitle and/or trend
    bottom_content = []
    
    if subtitle:
        bottom_content.append(
            rx.text(
                subtitle,
                size="1",
                color=colors["text_muted"]
            )
        )
    
    if trend and trend_value:
        trend_element = rx.box(
            rx.icon(
                trend_icons.get(trend, "minus"),
                font_size="14px",
                color=trend_colors.get(trend, colors["text_muted"])
            ),
            rx.text(
                trend_value,
                size="1",
                color=trend_colors.get(trend, colors["text_muted"]),
                font_weight=typography["weights"]["medium"]
            ),
            display="flex",
            align_items="center",
            gap="2px"
        )
        bottom_content.append(trend_element)
    
    if bottom_content:
        card_content.append(
            rx.box(
                *bottom_content,
                display="flex",
                align_items="center",
                justify_content="space-between" if len(bottom_content) > 1 else "flex-start",
                margin_top=spacing["sm"]
            )
        )
    
    return Card(
        *card_content,
        variant=variant,
        padding="lg",
        class_name=class_name,
        **kwargs
    )
