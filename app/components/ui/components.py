"""
Reusable UI Components following the design system.

This module provides consistent, reusable components:
- StatusBadge: Standardized status indicators
- SearchBar: Consistent search inputs
- ActionButton: Standardized buttons
- StatsCard: Dashboard statistics cards
- DataCard: Content display cards
"""

import reflex as rx
from typing import Optional, Any, Callable
from ...utils.styles.design_system import ColorSystem, Typography, ComponentStyles, Spacing

def StatusBadge(status: str, **props) -> rx.Component:
    """
    Reusable status badge with consistent styling.
    
    Args:
        status: Status text (active, inactive, pending, completed, cancelled)
        **props: Additional props
    """
    colors = ColorSystem.get_status_colors(status)
    
    return rx.box(
        rx.text(
            status.title(),
            style={
                **Typography.get_text_style("caption"),
                "color": colors["color"],
                "font_weight": "500"
            }
        ),
        style={
            "padding": f"{Spacing.xs} {Spacing.sm}",
            "background": colors["bg"],
            "border": f"1px solid {colors['border']}",
            "border_radius": "20px",
            "display": "inline-flex",
            "align_items": "center"
        },
        **props
    )

def SearchBar(
    placeholder: str = "Search...",
    value: Any = "",
    on_change: Optional[Callable] = None,
    icon: str = "search",
    **props
) -> rx.Component:
    """
    Reusable search bar component.
    
    Args:
        placeholder: Input placeholder text
        value: Input value
        on_change: Change handler
        icon: Search icon name
        **props: Additional props
    """
    return rx.box(
        rx.box(
            rx.icon(icon, size=18, style={"color": ColorSystem.get_color_variant("textMuted")}),
            style={
                "position": "absolute",
                "left": Spacing.md,
                "top": "50%",
                "transform": "translateY(-50%)",
                "z_index": "1"
            }
        ),
        rx.input(
            placeholder=placeholder,
            value=value,
            on_change=on_change,
            style={
                **ComponentStyles.get_input_style(),
                "padding_left": "44px",
                "width": "100%"
            }
        ),
        style={"position": "relative", "width": "100%"},
        **props
    )

def ActionButton(
    text: str,
    on_click: Optional[Callable] = None,
    variant: str = "primary",
    size: str = "md",
    icon: Optional[str] = None,
    loading: bool = False,
    **props
) -> rx.Component:
    """
    Reusable action button component.
    
    Args:
        text: Button text
        on_click: Click handler
        variant: Button variant (primary, secondary, ghost)
        size: Button size (sm, md, lg)
        icon: Optional icon name
        loading: Loading state
        **props: Additional props
    """
    content = []
    
    if loading:
        content.append(rx.spinner(size="1"))
    elif icon:
        content.append(rx.icon(icon, size=16))
    
    content.append(rx.text(text))
    
    # Extract style from props if present and merge with component style
    custom_style = props.pop("style", {})
    button_style = {**ComponentStyles.get_button_style(variant, size), **custom_style}
    
    return rx.box(
        rx.hstack(*content, spacing="2", align="center") if len(content) > 1 else content[0],
        on_click=on_click,
        style=button_style,
        **props
    )

def StatsCard(
    title: str,
    value: str,
    icon: str,
    color: str = "primary",
    subtitle: Optional[str] = None,
    trend: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Dashboard statistics card.
    
    Args:
        title: Card title
        value: Main statistic value
        icon: Icon name
        color: Color theme
        subtitle: Optional subtitle
        trend: Optional trend indicator
        **props: Additional props
    """
    from ...utils.styles.colorPallet import ColorPallet
    colors_palette = ColorPallet().colors
    icon_color = colors_palette.get(color, colors_palette["primary"])
    
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text(
                    title,
                    style={
                        **Typography.get_text_style("caption"),
                        "color": ColorSystem.get_color_variant("textMuted"),
                        "font_weight": "500"
                    }
                ),
                rx.text(
                    value,
                    style={
                        **Typography.get_text_style("h2"),
                        "color": icon_color,
                        "font_size": "28px"
                    }
                ),
                rx.cond(
                    subtitle,
                    rx.text(
                        subtitle,
                        style={
                            **Typography.get_text_style("caption"),
                            "color": ColorSystem.get_color_variant("textMuted")
                        }
                    )
                ),
                align="start",
                spacing="1",
                flex="1"
            ),
            rx.box(
                rx.icon(icon, size=24, color=icon_color),
                style={
                    "padding": Spacing.md,
                    "background": ColorSystem.get_color_variant(color, 20),
                    "border": f"1px solid {ColorSystem.get_color_variant(color, 40)}",
                    "border_radius": "12px"
                }
            ),
            justify="between",
            align="start",
            width="100%"
        ),
        style=ComponentStyles.get_card_style("hover"),
        **props
    )

def DataCard(
    children: rx.Component,
    title: Optional[str] = None,
    actions: Optional[rx.Component] = None,
    **props
) -> rx.Component:
    """
    Generic data display card.
    
    Args:
        children: Card content
        title: Optional card title
        actions: Optional action buttons
        **props: Additional props
    """
    content = []
    
    if title or actions:
        header = rx.hstack(
            rx.text(
                title or "",
                style={
                    **Typography.get_text_style("h3"),
                    "font_size": "18px"
                }
            ) if title else rx.box(),
            actions or rx.box(),
            justify="between",
            align="center",
            width="100%"
        )
        content.append(header)
        
        if title or actions:
            content.append(
                rx.divider(
                    color=ColorSystem.get_color_variant("border"),
                    margin=f"{Spacing.md} 0"
                )
            )
    
    content.append(children)
    
    return rx.box(
        rx.vstack(*content, spacing="2", align="start", width="100%"),
        style=ComponentStyles.get_card_style("default"),
        **props
    )

def FilterButton(
    text: str,
    is_active: bool = False,
    on_click: Optional[Callable] = None,
    **props
) -> rx.Component:
    """
    Filter button for status filtering.
    
    Args:
        text: Button text
        is_active: Whether button is active
        on_click: Click handler
        **props: Additional props
    """
    from ...utils.styles.colorPallet import ColorPallet
    colors = ColorPallet().colors
    
    if is_active:
        style = {
            "padding": f"{Spacing.xs} {Spacing.md}",
            "background": ColorSystem.get_color_variant("primary", 20),
            "border": f"1px solid {ColorSystem.get_color_variant('primary', 40)}",
            "color": colors["primary"],
            "border_radius": "8px",
            "cursor": "pointer",
            "font_weight": "500",
            "font_size": "14px"
        }
    else:
        style = {
            "padding": f"{Spacing.xs} {Spacing.md}",
            "background": "transparent",
            "border": "1px solid transparent",
            "color": colors["textSecondary"],
            "border_radius": "8px",
            "cursor": "pointer",
            "font_weight": "400",
            "font_size": "14px",
            "_hover": {
                "background": ColorSystem.get_color_variant("textMuted", 10)
            }
        }
    
    return rx.box(
        rx.text(text),
        on_click=on_click,
        style=style,
        **props
    )

def EmptyState(
    icon: str = "inbox",
    title: str = "No data",
    description: str = "No items found",
    action_text: Optional[str] = None,
    on_action: Optional[Callable] = None,
    **props
) -> rx.Component:
    """
    Empty state placeholder component.
    
    Args:
        icon: Icon name
        title: Empty state title
        description: Empty state description
        action_text: Optional action button text
        on_action: Optional action handler
        **props: Additional props
    """
    content = [
        rx.icon(
            icon, 
            size=48, 
            style={"color": ColorSystem.get_color_variant("textMuted")}
        ),
        rx.text(
            title,
            style={
                **Typography.get_text_style("h3"),
                "color": ColorSystem.get_color_variant("textMuted"),
                "margin_top": Spacing.md
            }
        ),
        rx.text(
            description,
            style={
                **Typography.get_text_style("body"),
                "color": ColorSystem.get_color_variant("textMuted"),
                "text_align": "center"
            }
        )
    ]
    
    if action_text and on_action:
        content.append(
            ActionButton(
                text=action_text,
                on_click=on_action,
                variant="secondary",
                style={"margin_top": Spacing.lg}
            )
        )
    
    return rx.center(
        rx.vstack(
            *content,
            spacing="2",
            align="center",
            style={"text_align": "center"}
        ),
        style={
            "min_height": "300px",
            "width": "100%"
        },
        **props
    )
