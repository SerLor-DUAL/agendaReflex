import reflex as rx
from typing import Literal, Optional
from ....utils.colorPallet.colorPallet import ColorPallet

colors = ColorPallet().colors

AlertVariant = Literal["info", "success", "warning", "error"]
AlertSize = Literal["sm", "md", "lg"]

def Alert(
    children: str = "",
    variant: AlertVariant = "info",
    size: AlertSize = "md",
    title: Optional[str] = None,
    dismissible: bool = False,
    icon: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Modern alert component with multiple variants.
    
    Args:
        children: Alert message content
        variant: Alert type/severity
        size: Alert size
        title: Optional alert title
        dismissible: Whether alert can be dismissed
        icon: Custom icon (auto-selected if not provided)
        **props: Additional alert props
    
    Returns:
        rx.Component: Styled alert component
    """
    
    # Size configurations
    size_config = {
        "sm": {"padding": "8px 12px", "font_size": "13px", "icon_size": 16},
        "md": {"padding": "12px 16px", "font_size": "14px", "icon_size": 18},
        "lg": {"padding": "16px 20px", "font_size": "15px", "icon_size": 20}
    }
    
    # Variant configurations
    variant_config = {
        "info": {
            "background": f"{colors['primary']}20",
            "border": f"1px solid {colors['primary']}40",
            "color": colors["primary"],
            "icon": "info"
        },
        "success": {
            "background": f"{colors['success']}20", 
            "border": f"1px solid {colors['success']}40",
            "color": colors["success"],
            "icon": "check-circle"
        },
        "warning": {
            "background": f"{colors['warning']}20",
            "border": f"1px solid {colors['warning']}40", 
            "color": colors["warning"],
            "icon": "alert-triangle"
        },
        "error": {
            "background": f"{colors['error']}20",
            "border": f"1px solid {colors['error']}40",
            "color": colors["error"],
            "icon": "x-circle"
        }
    }
    
    config = size_config[size]
    variant_style = rx.Var.create(variant_config)[variant]
    alert_icon = icon or variant_style["icon"]
    
    # Alert styles
    alert_styles = {
        "background": variant_style["background"],
        "border": variant_style["border"],
        "border_radius": "12px",
        "padding": config["padding"],
        "display": "flex",
        "align_items": "flex-start",
        "gap": "12px",
        "width": "100%",
        "box_sizing": "border-box",
        "animation": "slideIn 0.3s ease-out"
    }
    
    # Build alert content
    alert_content = [
        # Icon
        rx.icon(
            alert_icon,
            size=config["icon_size"],
            color=variant_style["color"],
            style={"flex_shrink": "0", "margin_top": "2px"}
        ),
        
        # Content
        rx.vstack(
            rx.cond(
                title,
                rx.text(
                    title,
                    style={
                        "font_size": config["font_size"],
                        "font_weight": "600",
                        "color": variant_style["color"],
                        "margin_bottom": "4px"
                    }
                )
            ),
            rx.text(
                children,
                style={
                    "font_size": config["font_size"],
                    "color": colors["text"],
                    "line_height": "1.5"
                }
            ),
            spacing="1",
            align="start",
            width="100%"
        )
    ]
    
    # Add dismiss button if dismissible
    if dismissible:
        alert_content.append(
            rx.button(
                rx.icon("x", size=14),
                variant="ghost",
                size="1",
                style={
                    "color": variant_style["color"],
                    "padding": "4px",
                    "margin_left": "auto",
                    "flex_shrink": "0"
                }
            )
        )
    
    merged_styles = {**alert_styles, **props.pop("style", {})}

    return rx.box(
        rx.hstack(*alert_content, align="start", width="100%"),
        style=merged_styles,
        **props
    )

def Toast(
    message: str,
    variant: AlertVariant = "info",
    duration: int = 3000,
    **props
) -> rx.Component:
    """
    Toast notification component.
    
    Args:
        message: Toast message
        variant: Toast type/severity
        duration: Auto-dismiss duration in ms
        **props: Additional props
    
    Returns:
        rx.Component: Toast component
    """
    
    return Alert(
        message,
        variant=variant,
        size="md",
        dismissible=True,
        style={
            "position": "fixed",
            "top": "20px",
            "right": "20px",
            "max_width": "400px",
            "z_index": "1000",
            "animation": "slideInRight 0.3s ease-out"
        },
        **props
    )
