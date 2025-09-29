import reflex as rx
from typing import Optional
from ...utils.styles.colorPallet import ColorPallet
from ..shared.card import Card

colors = ColorPallet().colors

def FormContainer(
    *children,
    title: Optional[str] = None,
    subtitle: Optional[str] = None,
    max_width: str = "400px",
    **props
) -> rx.Component:
    """
    Modern form container with optional header.
    
    Args:
        *children: Form content
        title: Form title
        subtitle: Form subtitle
        max_width: Maximum form width
        **props: Additional container props
    
    Returns:
        rx.Component: Styled form container
    """
    
    form_content = []
    
    # Add header if title is provided
    if title:
        header_content = [
            rx.heading(
                title,
                size="6",
                style={
                    "color": colors["text"],
                    "text_align": "center",
                    "font_weight": "700",
                    "margin_bottom": "8px"
                }
            )
        ]
        
        if subtitle:
            header_content.append(
                rx.text(
                    subtitle,
                    style={
                        "color": colors["textSecondary"],
                        "text_align": "center",
                        "font_size": "14px",
                        "margin_bottom": "24px"
                    }
                )
            )
        
        form_content.append(
            rx.vstack(*header_content, spacing="2", align="center", width="100%")
        )
    
    # Add form children
    form_content.extend(children)
    
    return rx.center(
        Card(
            rx.vstack(
                *form_content,
                spacing="5",
                align="start", 
                width="100%"
            ),
            variant="default",
            size="lg",
            style={"max_width": max_width}
        ),
        width="100%",
        **props
    )

def FieldGroup(
    *children,
    label: Optional[str] = None,
    description: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Form field group with optional label and description.
    
    Args:
        *children: Field content
        label: Group label
        description: Group description
        **props: Additional props
    
    Returns:
        rx.Component: Field group component
    """
    
    group_content = []
    
    if label:
        group_content.append(
            rx.text(
                label,
                style={
                    "font_weight": "600",
                    "font_size": "14px",
                    "color": colors["text"],
                    "margin_bottom": "4px"
                }
            )
        )
    
    if description:
        group_content.append(
            rx.text(
                description,
                style={
                    "font_size": "13px",
                    "color": colors["textMuted"],
                    "margin_bottom": "8px"
                }
            )
        )
    
    group_content.extend(children)
    
    return rx.vstack(
        *group_content,
        spacing="2",
        align="start",
        width="100%",
        **props
    )

def FormActions(*children, **props) -> rx.Component:
    """
    Form actions container (typically for buttons).
    
    Args:
        *children: Action buttons
        **props: Additional props
    
    Returns:
        rx.Component: Form actions container
    """
    
    return rx.hstack(
        *children,
        spacing="3",
        width="100%",
        justify="end",
        style={
            "margin_top": "16px",
            "padding_top": "16px",
            "border_top": f"1px solid {colors['border']}"
        },
        **props
    )
