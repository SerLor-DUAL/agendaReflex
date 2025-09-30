"""
Spinner Component

This module provides reusable Spinner components that leverage the design system
for consistent loading indicators throughout the application.
"""

import reflex as rx
from typing import Optional

# Import styles from the design system
from app.utils.styles import get_loading_spinner_styles, colors

def Spinner(
    size: str = "md",
    color: Optional[str] = None,
    thickness: str = "2px",
    class_name: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Spinner component following the design system.
    
    Args:
        size: Spinner size (sm, md, lg)
        color: Spinner color (defaults to primary)
        thickness: Border thickness
        class_name: Additional CSS class names
        **props: Additional props
    
    Returns:
        A styled Spinner component
    """
    
    # Get spinner styles
    spinner_styles = get_loading_spinner_styles(size=size)
    
    # Override color if provided
    if color:
        spinner_color = colors.get(color, color)
        spinner_styles["border_top"] = f"{thickness} solid {spinner_color}"
    
    # Merge additional styles from props
    if "style" in props:
        for key, value in props["style"].items():
            spinner_styles[key] = value
        props.pop("style")
    
    return rx.box(
        style=spinner_styles,
        class_name=class_name,
        **props
    )

def LoadingOverlay(
    is_loading: bool = False,
    spinner_size: str = "md",
    message: Optional[str] = None,
    class_name: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Loading overlay component with spinner and optional message.
    
    Args:
        is_loading: Whether to show loading overlay
        spinner_size: Size of the spinner
        message: Optional loading message
        class_name: Additional CSS class names
        **props: Additional props
    
    Returns:
        A styled LoadingOverlay component
    """
    
    overlay_styles = {
        "position": "fixed",
        "top": "0",
        "left": "0",
        "right": "0",
        "bottom": "0",
        "background": "rgba(0, 0, 0, 0.5)",
        "display": "flex",
        "flex_direction": "column",
        "align_items": "center",
        "justify_content": "center",
        "z_index": "9999",
        "backdrop_filter": "blur(4px)"
    }
    
    loading_content = [
        Spinner(size=spinner_size, color="primary")
    ]
    
    if message:
        loading_content.append(
            rx.text(
                message,
                size="3",
                color=colors["text_primary"],
                style={"margin_top": "16px", "text_align": "center"}
            )
        )
    
    return rx.cond(
        is_loading,
        rx.box(
            *loading_content,
            style=overlay_styles,
            class_name=class_name,
            **props
        )
    )
