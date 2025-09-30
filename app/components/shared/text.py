"""
Text Component

This module provides reusable Text components that leverage the design system
for consistent typography throughout the application.
"""

import reflex as rx
from typing import Union, Optional

# Import styles from the design system
from app.utils.styles import get_text_styles, colors, typography

def Text(
    children: Union[str, int, float],
    size: str = "md",
    weight: str = "normal",
    color: Optional[str] = None,
    align: str = "left",
    variant: str = "body",
    class_name: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Modern text component following the design system.
    
    Args:
        children: Text content
        size: Text size token (xs, sm, md, lg, xl, 2xl, 3xl)
        weight: Font weight (normal, medium, semibold, bold, extrabold)
        color: Text color (uses semantic color if provided, otherwise text_primary)
        align: Text alignment (left, center, right)
        variant: Text variant (body, heading, caption)
        class_name: Additional CSS class names
        **props: Additional props
    
    Returns:
        A styled Text component
    """
    
    # Color mapping for semantic colors
    color_map = {
        "primary": colors["text_primary"],
        "secondary": colors["text_secondary"],
        "muted": colors["text_muted"],
        "disabled": colors["text_disabled"],
        "error": colors["error"],
        "success": colors["success"],
        "warning": colors["warning"],
        "info": colors["info"],
    }
    
    # Get text styles
    text_color = color_map.get(color) if color else colors["text_primary"]
    text_styles = get_text_styles(
        size=size,
        weight=weight,
        color=text_color
    )
    
    # Add alignment
    text_styles["text_align"] = align
    
    # Merge additional styles from props
    if "style" in props:
        for key, value in props["style"].items():
            text_styles[key] = value
        props.pop("style")
    
    return rx.text(
        str(children),
        size=typography["sizes"].get(size, typography["sizes"]["md"]),
        style=text_styles,
        class_name=class_name,
        **props
    )

def Heading(
    children: Union[str, int, float],
    level: int = 2,
    size: Optional[str] = None,
    weight: str = "semibold",
    color: Optional[str] = None,
    align: str = "left",
    class_name: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Heading component following the design system.
    
    Args:
        children: Heading content
        level: Heading level (1-6)
        size: Override size (if not provided, uses level-based sizing)
        weight: Font weight (normal, medium, semibold, bold, extrabold)
        color: Text color (uses semantic color if provided, otherwise text_primary)
        align: Text alignment (left, center, right)
        class_name: Additional CSS class names
        **props: Additional props
    
    Returns:
        A styled Heading component
    """
    
    # Level-based size mapping if size not provided
    level_size_map = {
        1: "3xl",  # Largest
        2: "2xl",
        3: "xl",
        4: "lg",
        5: "lg2",
        6: "md"
    }
    
    heading_size = size or level_size_map.get(level, "lg")
    
    # Color mapping
    color_map = {
        "primary": colors["text_primary"],
        "secondary": colors["text_secondary"],
        "muted": colors["text_muted"],
        "disabled": colors["text_disabled"],
        "error": colors["error"],
        "success": colors["success"],
        "warning": colors["warning"],
        "info": colors["info"],
    }
    
    # Get text styles
    text_color = color_map.get(color) if color else colors["text_primary"]
    heading_styles = get_text_styles(
        size=heading_size,
        weight=weight,
        color=text_color,
        line_height="tight"
    )
    
    # Add alignment
    heading_styles["text_align"] = align
    
    # Merge additional styles from props
    if "style" in props:
        for key, value in props["style"].items():
            heading_styles[key] = value
        props.pop("style")
    
    return rx.heading(
        str(children),
        size=typography["sizes"].get(heading_size, typography["sizes"]["lg"]),
        style=heading_styles,
        class_name=class_name,
        **props
    )

def Caption(
    children: Union[str, int, float],
    color: Optional[str] = "muted",
    align: str = "left",
    class_name: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Caption text component for small descriptive text.
    
    Args:
        children: Caption content
        color: Text color (defaults to muted)
        align: Text alignment (left, center, right)
        class_name: Additional CSS class names
        **props: Additional props
    
    Returns:
        A styled Caption component
    """
    
    return Text(
        children,
        size="xs",
        weight="normal",
        color=color or "muted",
        align=align,
        class_name=class_name,
        **props
    )

def Label(
    children: Union[str, int, float],
    required: bool = False,
    color: Optional[str] = None,
    class_name: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Label component for form fields and UI labels.
    
    Args:
        children: Label content
        required: Whether to show required indicator
        color: Text color (defaults to text_primary)
        class_name: Additional CSS class names
        **props: Additional props
    
    Returns:
        A styled Label component
    """
    
    label_content = [str(children)]
    
    if required:
        label_content.extend([
            " ",
            rx.text(
                "*",
                color=colors["error"],
                style={"display": "inline"}
            )
        ])
    
    return rx.label(
        *label_content,
        size=typography["sizes"]["sm"],
        color=colors["text_primary"] if not color else colors.get(color, color),
        font_weight=typography["weights"]["medium"],
        class_name=class_name,
        **props
    )
