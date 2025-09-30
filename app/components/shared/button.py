"""
Button Component

This module provides a reusable Button component that leverages the design system
for consistent styling and behavior throughout the application.
"""

import reflex as rx
from typing import List, Union, Optional, Callable, Any

# Import styles from the design system
from app.utils.styles import get_button_styles

def Button(
    children: Union[str, List[rx.Component]],
    variant: str = "primary",
    size: str = "md",
    on_click: Optional[Callable] = None,
    icon: Optional[str] = None,
    icon_position: str = "left",
    is_loading: bool = False,
    is_disabled: bool = False,
    full_width: bool = False,
    class_name: Optional[str] = None,
    **kwargs
) -> rx.Component:
    """
    Primary Button component following the design system.
    
    Args:
        children: Button content (text or components)
        variant: Button style variant (primary, secondary, outline, ghost, danger)
        size: Button size (sm, md, lg)
        on_click: Function to call when the button is clicked
        icon: Optional icon name to display
        icon_position: Position of the icon (left or right)
        is_loading: Whether to show a loading state
        is_disabled: Whether the button is disabled
        full_width: Whether the button should take full width
        class_name: Additional CSS class names
        **kwargs: Additional props to pass to the button element
        
    Returns:
        A styled Button component
    """
    # Get style dictionary based on props
    button_styles = get_button_styles(
        variant=variant,
        size=size,
        full_width=full_width,
        disabled=is_disabled
    )
    
    # Merge additional styles from kwargs
    if "style" in kwargs:
        for key, value in kwargs["style"].items():
            button_styles[key] = value
        kwargs.pop("style")
    
    # Handle button content
    button_content = []
    
    # Add icon if provided
    if icon and not is_loading and icon_position == "left":
        button_content.append(rx.icon(icon, font_size="1em"))
    
    # Add button text or children
    if isinstance(children, str):
        button_content.append(rx.text(children))
    else:
        if isinstance(children, list):
            button_content.extend(children)
        else:
            button_content.append(children)
    
    # Add icon at the end if specified
    if icon and not is_loading and icon_position == "right":
        button_content.append(rx.icon(icon, font_size="1em"))
    
    # Replace content with loading spinner if in loading state
    if is_loading:
        button_content = [
            rx.spinner(color="currentColor", size="sm", thickness="2px"),
            rx.text("Loading...")
        ]
    
    # Return the button component
    return rx.button(
        *button_content,
        on_click=on_click,
        disabled=is_disabled,
        style=button_styles,
        class_name=class_name,
        **kwargs
    )

def IconButton(
    icon: str,
    variant: str = "primary",
    size: str = "md",
    on_click: Optional[Callable] = None,
    aria_label: Optional[str] = None,
    is_loading: bool = False,
    is_disabled: bool = False,
    class_name: Optional[str] = None,
    **kwargs
) -> rx.Component:
    """
    Icon-only Button component following the design system.
    
    Args:
        icon: Icon name to display
        variant: Button style variant (primary, secondary, outline, ghost, danger)
        size: Button size (sm, md, lg)
        on_click: Function to call when the button is clicked
        aria_label: Accessibility label for the button
        is_loading: Whether to show a loading state
        is_disabled: Whether the button is disabled
        class_name: Additional CSS class names
        **kwargs: Additional props to pass to the button element
        
    Returns:
        A styled IconButton component
    """
    # Get base styles
    button_styles = get_button_styles(
        variant=variant,
        size=size,
        disabled=is_disabled
    )
    
    # Adjust for icon-only styling
    icon_sizes = {
        "sm": "16px",
        "md": "20px",
        "lg": "24px"
    }
    
    # Set fixed width/height to make the button square
    size_value = {
        "sm": "32px",
        "md": "40px",
        "lg": "48px"
    }
    
    # Add icon-specific styles
    button_styles.update({
        "width": size_value.get(size, size_value["md"]),
        "height": size_value.get(size, size_value["md"]),
        "padding": "0",
        "aspect_ratio": "1/1",
        "display": "inline-flex",
        "align_items": "center",
        "justify_content": "center"
    })
    
    # Handle loading state
    icon_content = rx.spinner(color="currentColor", size="sm") if is_loading else rx.icon(icon, font_size=icon_sizes.get(size, "20px"))
    
    # Return the icon button
    return rx.button(
        icon_content,
        on_click=on_click,
        disabled=is_disabled,
        style=button_styles,
        aria_label=aria_label or f"{icon} button",
        class_name=class_name,
        **kwargs
    )
