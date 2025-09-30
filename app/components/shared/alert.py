"""
Alert Component

This module provides reusable Alert and Toast components that leverage the design system
for consistent styling throughout the application.
"""

import reflex as rx
from typing import List, Union, Optional, Any

# Import styles from the design system
from app.utils.styles import colors, spacing, typography
from app.utils.styles.theme import components

def Alert(
    children: Union[str, List[rx.Component], rx.Component],
    variant: str = "info",
    size: str = "md",
    title: Optional[str] = None,
    dismissible: bool = False,
    icon: Optional[str] = None,
    class_name: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Modern alert component following the design system.
    
    Args:
        children: Alert message content
        variant: Alert type/severity (info, success, warning, error)
        size: Alert size (sm, md, lg)
        title: Optional alert title
        dismissible: Whether alert can be dismissed
        icon: Custom icon (auto-selected if not provided)
        class_name: Additional CSS class names
        **props: Additional alert props
    
    Returns:
        A styled Alert component
    """
    
    # Size configurations
    size_configs = {
        "sm": {
            "padding": spacing["sm"],
            "font_size": typography["sizes"]["xs"],
            "icon_size": 14
        },
        "md": {
            "padding": spacing["md"],
            "font_size": typography["sizes"]["sm"],
            "icon_size": 16
        },
        "lg": {
            "padding": spacing["lg"],
            "font_size": typography["sizes"]["md"],
            "icon_size": 18
        }
    }
    
    # Variant configurations
    variant_configs = {
        "info": {
            "background": f"rgba(59, 130, 246, 0.1)",  # Blue with opacity
            "border": f"1px solid rgba(59, 130, 246, 0.3)",
            "color": colors["info"],
            "icon": "info"
        },
        "success": {
            "background": f"rgba(34, 197, 94, 0.1)",  # Green with opacity
            "border": f"1px solid rgba(34, 197, 94, 0.3)",
            "color": colors["success"],
            "icon": "circle-check"
        },
        "warning": {
            "background": f"rgba(234, 179, 8, 0.1)",  # Yellow with opacity
            "border": f"1px solid rgba(234, 179, 8, 0.3)",
            "color": colors["warning"],
            "icon": "alert-triangle"
        },
        "error": {
            "background": f"rgba(239, 68, 68, 0.1)",  # Red with opacity
            "border": f"1px solid rgba(239, 68, 68, 0.3)",
            "color": colors["error"],
            "icon": "circle-x"
        }
    }
    
    size_config = size_configs.get(size, size_configs["md"])
    variant_config = variant_configs.get(variant, variant_configs["info"])
    alert_icon = icon or variant_config["icon"]
    
    # Alert styles
    alert_styles = {
        "background": variant_config["background"],
        "border": variant_config["border"],
        "border_radius": components["radius"]["lg"],
        "padding": size_config["padding"],
        "display": "flex",
        "align_items": "flex-start",
        "gap": spacing["sm"],
        "width": "100%",
        "transition": components["transitions"]["normal"]
    }
    
    # Merge additional styles from props
    if "style" in props:
        for key, value in props["style"].items():
            alert_styles[key] = value
        props.pop("style")
    
    # Build alert content
    alert_content = []
    
    # Icon
    alert_content.append(
        rx.icon(
            alert_icon,
            size=size_config["icon_size"],
            color=variant_config["color"],
            style={"flex_shrink": "0", "margin_top": "2px"}
        )
    )
    
    # Content section
    content_elements = []
    
    if title:
        content_elements.append(
            rx.text(
                title,
                size=size_config["font_size"],
                color=variant_config["color"],
                font_weight=typography["weights"]["semibold"],
                style={"margin_bottom": spacing["xs"]}
            )
        )
    
    # Add children content
    if isinstance(children, str):
        content_elements.append(
            rx.text(
                children,
                size=size_config["font_size"],
                color=colors["text_primary"],
                style={"line_height": typography["line_heights"]["normal"]}
            )
        )
    else:
        if isinstance(children, list):
            content_elements.extend(children)
        else:
            content_elements.append(children)
    
    alert_content.append(
        rx.box(
            *content_elements,
            flex="1"
        )
    )
    
    # Add dismiss button if dismissible
    if dismissible:
        alert_content.append(
            rx.button(
                rx.icon("x", size=14),
                variant="ghost",
                size="1",
                color=variant_config["color"],
                style={
                    "padding": "4px",
                    "margin_left": "auto",
                    "flex_shrink": "0",
                    "_hover": {
                        "background": colors["hover_overlay"]
                    }
                }
            )
        )
    
    return rx.box(
        *alert_content,
        style=alert_styles,
        class_name=class_name,
        **props
    )

def Toast(
    message: str,
    variant: str = "info",
    duration: int = 3000,
    position: str = "top-right",
    class_name: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Toast notification component following the design system.
    
    Args:
        message: Toast message
        variant: Toast type/severity (info, success, warning, error)
        duration: Auto-dismiss duration in ms
        position: Toast position (top-right, top-left, bottom-right, bottom-left)
        class_name: Additional CSS class names
        **props: Additional props
    
    Returns:
        A styled Toast component
    """
    
    # Position configurations
    position_styles = {
        "top-right": {
            "position": "fixed",
            "top": "20px",
            "right": "20px",
        },
        "top-left": {
            "position": "fixed",
            "top": "20px",
            "left": "20px",
        },
        "bottom-right": {
            "position": "fixed",
            "bottom": "20px",
            "right": "20px",
        },
        "bottom-left": {
            "position": "fixed",
            "bottom": "20px",
            "left": "20px",
        }
    }
    
    toast_styles = {
        **position_styles.get(position, position_styles["top-right"]),
        "max_width": "400px",
        "z_index": components["z_index"]["toast"],
        "animation": "slideInRight 0.3s ease-out",
        "box_shadow": components["shadows"]["lg"]
    }
    
    return Alert(
        message,
        variant=variant,
        size="md",
        dismissible=True,
        style=toast_styles,
        class_name=class_name,
        **props
    )
