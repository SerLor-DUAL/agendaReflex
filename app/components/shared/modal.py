"""
Modal Component

This module provides reusable Modal components that leverage the design system
for consistent styling throughout the application.
"""

import reflex as rx
from typing import List, Union, Optional, Any

# Import styles from the design system
from app.utils.styles import get_modal_styles, get_modal_backdrop_styles, colors, spacing, typography

def Modal(
    children: Union[List[rx.Component], rx.Component],
    is_open: bool = False,
    on_close: Optional[Any] = None,
    size: str = "md",
    center: bool = True,
    close_on_overlay_click: bool = True,
    class_name: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Modal component following the design system.
    
    Args:
        children: Modal content
        is_open: Whether modal is open
        on_close: Function to call when modal should close
        size: Modal size (sm, md, lg, xl)
        center: Whether to center modal vertically
        close_on_overlay_click: Whether clicking overlay closes modal
        class_name: Additional CSS class names
        **props: Additional props
    
    Returns:
        A styled Modal component
    """
    
    # Get modal styles
    modal_styles = get_modal_styles(size=size)
    backdrop_styles = get_modal_backdrop_styles()
    
    if center:
        backdrop_styles.update({
            "align_items": "center",
            "justify_content": "center"
        })
    
    # Merge additional styles from props
    if "style" in props:
        for key, value in props["style"].items():
            modal_styles[key] = value
        props.pop("style")
    
    # Modal backdrop with overlay click handler
    backdrop_props = {}
    if close_on_overlay_click and on_close:
        backdrop_props["on_click"] = on_close
    
    return rx.cond(
        is_open,
        rx.box(
            rx.box(
                children,
                style=modal_styles,
                class_name=class_name,
                on_click=rx.stop_propagation,  # Prevent event bubbling to backdrop
                **props
            ),
            style=backdrop_styles,
            **backdrop_props
        )
    )

def ModalHeader(
    children: Union[str, List[rx.Component], rx.Component],
    title: Optional[str] = None,
    on_close: Optional[Any] = None,
    show_close_button: bool = True,
    class_name: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Modal Header component for consistent modal layouts.
    
    Args:
        children: Custom header content (overrides title)
        title: Header title text
        on_close: Function to call when close button is clicked
        show_close_button: Whether to show close button
        class_name: Additional CSS class names
        **props: Additional props
    
    Returns:
        A styled ModalHeader component
    """
    
    header_styles = {
        "display": "flex",
        "align_items": "center",
        "justify_content": "space-between",
        "padding_bottom": spacing["md"],
        "margin_bottom": spacing["md"],
        "border_bottom": f"1px solid {colors['border']}"
    }
    
    # If custom children provided, use them
    if not isinstance(children, str) and children is not None:
        return rx.box(
            children,
            style=header_styles,
            class_name=class_name,
            **props
        )
    
    # Build header content
    header_content = []
    
    if title:
        header_content.append(
            rx.heading(
                title,
                size="5",
                color=colors["text_primary"],
                font_weight=typography["weights"]["semibold"]
            )
        )
    
    if show_close_button and on_close:
        header_content.append(
            rx.button(
                rx.icon("x", size="18px"),
                variant="ghost",
                size="2",
                on_click=on_close,
                style={
                    "color": colors["text_secondary"],
                    "_hover": {
                        "background": colors["hover_overlay"],
                        "color": colors["text_primary"]
                    }
                }
            )
        )
    
    return rx.box(
        *header_content,
        style=header_styles,
        class_name=class_name,
        **props
    )

def ModalBody(
    children: Union[List[rx.Component], rx.Component],
    class_name: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Modal Body component for consistent modal content areas.
    
    Args:
        children: Body content
        class_name: Additional CSS class names
        **props: Additional props
    
    Returns:
        A styled ModalBody component
    """
    
    body_styles = {
        "flex": "1",
        "overflow_y": "auto",
        "padding_y": spacing["sm"]
    }
    
    return rx.box(
        children,
        style=body_styles,
        class_name=class_name,
        **props
    )

def ModalFooter(
    children: Union[List[rx.Component], rx.Component],
    align: str = "right",
    class_name: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Modal Footer component for consistent modal action areas.
    
    Args:
        children: Footer content (typically buttons)
        align: Footer content alignment (left, center, right, space-between)
        class_name: Additional CSS class names
        **props: Additional props
    
    Returns:
        A styled ModalFooter component
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
        "padding_top": spacing["md"],
        "margin_top": spacing["md"],
        "border_top": f"1px solid {colors['border']}"
    }
    
    return rx.box(
        children,
        style=footer_styles,
        class_name=class_name,
        **props
    )

def AlertDialog(
    title: str,
    description: str,
    is_open: bool = False,
    on_close: Optional[Any] = None,
    on_confirm: Optional[Any] = None,
    confirm_text: str = "Confirm",
    cancel_text: str = "Cancel",
    variant: str = "default",
    class_name: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Alert Dialog component for confirmations and alerts.
    
    Args:
        title: Dialog title
        description: Dialog description/message
        is_open: Whether dialog is open
        on_close: Function to call when dialog should close
        on_confirm: Function to call when confirm button is clicked
        confirm_text: Text for confirm button
        cancel_text: Text for cancel button
        variant: Dialog variant (default, danger)
        class_name: Additional CSS class names
        **props: Additional props
    
    Returns:
        A styled AlertDialog component
    """
    
    # Variant-specific styling
    confirm_variant = "danger" if variant == "danger" else "primary"
    
    return Modal(
        is_open=is_open,
        on_close=on_close,
        size="sm",
        class_name=class_name,
        **props,
        children=[
            ModalHeader(
                title=title,
                on_close=on_close
            ),
            ModalBody(
                rx.text(
                    description,
                    size="3",
                    color=colors["text_secondary"],
                    line_height=typography["line_heights"]["relaxed"]
                )
            ),
            ModalFooter(
                rx.button(
                    cancel_text,
                    variant="secondary",
                    on_click=on_close
                ),
                rx.button(
                    confirm_text,
                    variant=confirm_variant,
                    on_click=on_confirm
                ) if on_confirm else None,
                align="right"
            )
        ]
    )
