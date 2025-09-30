"""
Badge Component

This module provides reusable Badge components that leverage the design system
for consistent indicators and labels throughout the application.
"""

import reflex as rx
from typing import Union, Optional

# Import styles from the design system
from app.utils.styles import get_badge_styles

def Badge(
    children: Union[str, int, float],
    variant: str = "default",
    size: str = "md",
    icon: Optional[str] = None,
    class_name: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Badge component following the design system.
    
    Args:
        children: Badge content
        variant: Badge variant (default, success, warning, error, info)
        size: Badge size (sm, md)
        icon: Optional icon to display
        class_name: Additional CSS class names
        **props: Additional props
    
    Returns:
        A styled Badge component
    """
    
    # Get badge styles
    badge_styles = get_badge_styles(
        variant=variant,
        size=size
    )
    
    # Merge additional styles from props
    if "style" in props:
        for key, value in props["style"].items():
            badge_styles[key] = value
        props.pop("style")
    
    # Build badge content
    badge_content = []
    
    if icon:
        badge_content.append(
            rx.icon(
                icon,
                size=12 if size == "sm" else 14
            )
        )
    
    badge_content.append(str(children))
    
    return rx.box(
        *badge_content,
        style=badge_styles,
        class_name=class_name,
        **props
    )

def StatusBadge(
    status: str,
    size: str = "md",
    class_name: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Status Badge component with predefined status variants.
    
    Args:
        status: Status value (active, inactive, pending, completed, error, etc.)
        size: Badge size (sm, md)
        class_name: Additional CSS class names
        **props: Additional props
    
    Returns:
        A styled StatusBadge component
    """
    
    # Use rx.cond to handle different status values
    return rx.cond(
        status == "active",
        Badge("Active", variant="success", size=size, icon="circle-check", class_name=class_name, **props),
        rx.cond(
            status == "inactive",
            Badge("Inactive", variant="default", size=size, icon="circle", class_name=class_name, **props),
            rx.cond(
                status == "pending",
                Badge("Pending", variant="warning", size=size, icon="clock", class_name=class_name, **props),
                rx.cond(
                    status == "completed",
                    Badge("Completed", variant="success", size=size, icon="check", class_name=class_name, **props),
                    rx.cond(
                        status == "error",
                        Badge("Error", variant="error", size=size, icon="circle-x", class_name=class_name, **props),
                        # Default case
                        Badge(status, variant="default", size=size, icon="circle", class_name=class_name, **props)
                    )
                )
            )
        )
    )

def NotificationBadge(
    count: Union[int, str],
    max_count: int = 99,
    show_zero: bool = False,
    size: str = "sm",
    class_name: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Notification Badge component for displaying counts.
    
    Args:
        count: Notification count
        max_count: Maximum count to display (shows "max_count+" if exceeded)
        show_zero: Whether to show badge when count is 0
        size: Badge size (sm, md)
        class_name: Additional CSS class names
        **props: Additional props
    
    Returns:
        A styled NotificationBadge component
    """
    
    # Convert count to integer if string
    try:
        count_int = int(count)
    except (ValueError, TypeError):
        count_int = 0
    
    # Don't show badge if count is 0 and show_zero is False
    if count_int <= 0 and not show_zero:
        return rx.fragment()
    
    # Format count display
    if count_int > max_count:
        display_count = f"{max_count}+"
    else:
        display_count = str(count_int)
    
    return Badge(
        display_count,
        variant="error",
        size=size,
        style={
            "min_width": "18px" if size == "sm" else "22px",
            "border_radius": "50%",
            "justify_content": "center"
        },
        class_name=class_name,
        **props
    )
