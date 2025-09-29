import reflex as rx
from typing import Optional
from ...utils.styles.colorPallet import ColorPallet
from ..shared.input import Input
from ..shared.text import Text

colors = ColorPallet().colors

def FormField(
    label: str,
    placeholder: str,
    value,
    on_change,
    type_: str = "text",
    icon_left: Optional[str] = None,
    icon_right: Optional[str] = None,
    helper_text: str = "",
    error_text: str = "",
    required: bool = False,
    disabled: bool = False,
    size: str = "md",
    **kwargs
) -> rx.Component:
    """
    Modern form field component with label, input, and validation.
    
    Args:
        label: Field label text
        placeholder: Input placeholder text
        value: Bound state value
        on_change: State change handler
        type_: Input type (text, password, email, etc.)
        icon_left: Left side icon
        icon_right: Right side icon
        helper_text: Helper text
        error_text: Error message text
        required: Whether field is required
        disabled: Whether field is disabled
        size: Input size (sm, md, lg)
        **kwargs: Additional input props
    
    Returns:
        rx.Component: Complete modern form field
    """
    
    has_error = error_text != ""
    
    return rx.vstack(
        # Field label
        Text(
            f"{label}{'*' if required else ''}",
            variant="small",
            color="primary" if not has_error else "error",
            weight="medium"
        ),
        
        # Input field with modern styling
        Input(
            placeholder=placeholder,
            value=value,
            on_change=on_change,
            type_=type_,
            size=size,
            disabled=disabled,
            error=has_error,
            icon_left=icon_left,
            icon_right=icon_right,
            **kwargs
        ),
        
        # Helper or error text
        rx.cond(
            error_text != "",
            Text(
                error_text,
                variant="caption",
                color="error"
            ),
            rx.cond(
                helper_text != "",
                Text(
                    helper_text,
                    variant="caption",
                    color="muted"
                )
            )
        ),
        
        spacing="1",
        width="100%",
        align="start"
    )
