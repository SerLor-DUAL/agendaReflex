import reflex as rx
from typing import Optional
from ..shared import Input
from ...utils.styles.colorPallet import ColorPallet

colors = ColorPallet().colors

def FormField(
    label: str,
    placeholder: str,
    value,
    on_change,
    type_: str = "text",
    icon_left: Optional[str] = None,
    error_text: str = "",
    required: bool = False,
    **kwargs
) -> rx.Component:
    """Clean form field component."""
    
    has_error = error_text != ""
    
    return rx.vstack(
        # Label
        rx.cond(
            required,
            rx.text(
                f"{label}*",
                style={
                    "font_size": "14px",
                    "font_weight": "500",
                    "color": colors["error"] if has_error else colors["text"],
                    "margin_bottom": "4px"
                }
            ),
            rx.text(
                label,
                style={
                    "font_size": "14px",
                    "font_weight": "500",
                    "color": colors["error"] if has_error else colors["text"],
                    "margin_bottom": "4px"
                }
            ),
        ),
        
        # Input
        Input(
            placeholder=placeholder,
            value=value,
            on_change=on_change,
            type_=type_,
            icon_left=icon_left,
            error=has_error,
            **kwargs
        ),
        
        # Error message
        rx.cond(
            error_text != "",
            rx.text(
                error_text,
                style={
                    "font_size": "12px",
                    "color": colors["error"],
                    "margin_top": "4px"
                }
            )
        ),
        
        spacing="1",
        width="100%",
        align="start"
    )
