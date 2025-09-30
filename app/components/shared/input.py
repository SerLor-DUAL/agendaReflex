"""
Input Component

This module provides reusable Input components that leverage the design system
for consistent styling throughout the application.
"""

import reflex as rx
from typing import List, Union, Optional, Callable, Any

# Import styles from the design system
from app.utils.styles import get_input_styles, spacing, colors

def Input(
    placeholder: str = "",
    value = None,
    on_change = None,
    type_: str = "text",
    size: str = "md",
    variant: str = "default",
    disabled: bool = False,
    error: bool = False,
    icon_left: Optional[str] = None,
    icon_right: Optional[str] = None,
    width: str = "100%",
    class_name: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Modern input component following the design system.
    
    Args:
        placeholder: Input placeholder text
        value: Input value
        on_change: Change handler
        type_: Input type (text, password, email, etc.)
        size: Input size (sm, md, lg)
        variant: Input variant style (default, filled)
        disabled: Disabled state
        error: Error state
        icon_left: Icon on the left side
        icon_right: Icon on the right side
        width: Input width
        class_name: Additional CSS class names
        **props: Additional input props
    
    Returns:
        A styled Input component
    """
    # Get style dictionary based on props
    input_styles = get_input_styles(
        size=size,
        variant=variant,
        error=error,
        disabled=disabled
    )
    
    # Apply width
    input_styles["width"] = width
    
    # Merge additional styles from kwargs
    if "style" in props:
        for key, value in props["style"].items():
            input_styles[key] = value
        props.pop("style")
    
    # Build input content with icons if provided
    input_children = []
    
    if icon_left:
        input_children.append(
            rx.input.slot(
                rx.icon(
                    icon_left, 
                    size=16,
                    color=colors["text_muted"]
                )
            )
        )
    
    if icon_right:
        input_children.append(
            rx.input.slot(
                rx.icon(
                    icon_right, 
                    size=16,
                    color=colors["text_muted"]
                ),
                side="right"
            )
        )
    
    # Return the input component
    return rx.input(
        *input_children,
        placeholder=placeholder,
        value=value,
        on_change=on_change,
        type=type_,
        disabled=disabled,
        style=input_styles,
        class_name=class_name,
        **props
    )

def TextArea(
    placeholder: str = "",
    value = None,
    on_change = None,
    size: str = "md",
    variant: str = "default",
    disabled: bool = False,
    error: bool = False,
    rows: int = 4,
    resize: str = "vertical",
    class_name: Optional[str] = None,
    **props
) -> rx.Component:
    """
    TextArea component following the design system.
    
    Args:
        placeholder: TextArea placeholder text
        value: TextArea value
        on_change: Change handler
        size: TextArea size (sm, md, lg)
        variant: TextArea variant style (default, filled)
        disabled: Disabled state
        error: Error state
        rows: Number of rows
        resize: Resize behavior (none, both, horizontal, vertical)
        class_name: Additional CSS class names
        **props: Additional props
    
    Returns:
        A styled TextArea component
    """
    # Get base input styles
    textarea_styles = get_input_styles(
        size=size,
        variant=variant,
        error=error,
        disabled=disabled
    )
    
    # Adjust for textarea-specific styling
    textarea_styles.update({
        "resize": resize,
        "min_height": f"{rows * 1.5}rem",
        "height": "auto",
        "padding": spacing["md"]
    })
    
    # Merge additional styles from props
    if "style" in props:
        for key, value in props["style"].items():
            textarea_styles[key] = value
        props.pop("style")
    
    return rx.text_area(
        placeholder=placeholder,
        value=value,
        on_change=on_change,
        disabled=disabled,
        rows=rows,
        style=textarea_styles,
        class_name=class_name,
        **props
    )
