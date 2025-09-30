import reflex as rx
from typing import List, Dict
from ...state.app_state import AppState
from ...utils.styles import colors, spacing, typography, get_card_styles, get_nav_link_styles, get_text_styles

def _nav_item(
    icon: str,
    label: str,
    view_name: str,
    is_active = False
) -> rx.Component:
    """Single navigation item using new design system."""
    # Use rx.cond to handle active state styling
    base_styles = {
        "display": "flex",
        "align_items": "center",
        "padding": spacing["sm"],
        "border_radius": "8px",
        "text_decoration": "none",
        "transition": "all 0.2s ease",
        "gap": spacing["sm"],
        "font_weight": "500",
        "cursor": "pointer",
        "width": "100%"
    }
    
    return rx.box(
        rx.hstack(
            rx.cond(
                is_active,
                rx.icon(
                    icon,
                    size=18,
                    color=colors["primary"]
                ),
                rx.icon(
                    icon,
                    size=18,
                    color=colors["text_secondary"]
                )
            ),
            rx.cond(
                ~AppState.sidebar_collapsed,
                rx.cond(
                    is_active,
                    rx.text(
                        label,
                        size=typography["sizes"]["sm"],
                        color=colors["text_primary"],
                        font_weight=typography["weights"]["medium"]
                    ),
                    rx.text(
                        label,
                        size=typography["sizes"]["sm"],
                        color=colors["text_secondary"],
                        font_weight=typography["weights"]["normal"]
                    )
                )
            ),
            spacing=spacing["sm"],
            align="center",
            width="100%"
        ),
        on_click=lambda: AppState.navigate_to(view_name),
        style=rx.cond(
            is_active,
            {
                **base_styles,
                "background": colors["primary"],
                "color": colors["text_primary"],
            },
            {
                **base_styles,
                "_hover": {
                    "background": colors["hover_overlay"],
                    "color": colors["text_primary"],
                }
            }
        ),
        width="100%"
    )

def _nav_section(title: str, items: List[Dict]) -> rx.Component:
    """Navigation section with title and items."""
    return rx.vstack(
        rx.cond(
            ~AppState.sidebar_collapsed,
            rx.text(
                title,
                size=typography["sizes"]["xs"],
                color=colors["text_muted"],
                font_weight=typography["weights"]["semibold"],
                style={
                    "text_transform": "uppercase",
                    "letter_spacing": "0.1em",
                    "margin_bottom": "8px",
                    "padding": "0 16px"
                }
            )
        ),
        rx.vstack(
            *[
                _nav_item(
                    item["icon"],
                    item["label"],
                    item["view"],
                    is_active=AppState.current_view == item["view"]
                )
                for item in items
            ],
            spacing="1",
            width="100%"
        ),
        spacing="2",
        align="start",
        width="100%"
    )

def _stats_card() -> rx.Component:
    """Quick stats card in sidebar."""
    return rx.cond(
        ~AppState.sidebar_collapsed,
        rx.box(
            rx.vstack(
                rx.hstack(
                    rx.icon("trending-up", size=16, color=colors["success"]),
                    rx.text(
                        "Quick Stats",
                        style={
                            **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                            "font_weight": "600"
                        }
                    ),
                    spacing="2",
                    align="center"
                ),
                rx.divider(color=colors["border"]),
                rx.vstack(
                    rx.hstack(
                        rx.text("Clients:", style=get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"])),
                        rx.text(
                            AppState.clients_stats["total"],
                            style={
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                "color": colors["primary"],
                                "font_weight": "600"
                            }
                        ),
                        justify="between",
                        width="100%"
                    ),
                    rx.hstack(
                        rx.text("Orders:", style=get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"])),
                        rx.text(
                            AppState.orders_stats["total"],
                            style={
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                "color": colors["success"],
                                "font_weight": "600"
                            }
                        ),
                        justify="between",
                        width="100%"
                    ),
                    spacing="1",
                    width="100%"
                ),
                spacing="3",
                align="start",
                width="100%"
            ),
            style={
                **get_card_styles(),
                "padding": "16px",
                "margin_top": "16px"
            }
        )
    )

def _toggle_button() -> rx.Component:
    """Sidebar toggle button."""
    return rx.box(
        rx.icon(
            "chevron-left",
            size=18,
            color=colors["text_secondary"],
            style={
                "transform": rx.cond(
                    AppState.sidebar_collapsed,
                    "rotate(180deg)",
                    "rotate(0deg)"
                ),
                "transition": "transform 0.2s ease"
            }
        ),
        on_click=AppState.toggle_sidebar,
        style={
            "position": "absolute",
            "top": "20px",
            "right": "-12px",
            "width": "24px",
            "height": "24px",
            "background": colors["surface"],
            "border": f"1px solid {colors['border']}",
            "border_radius": "50%",
            "display": "flex",
            "align_items": "center",
            "justify_content": "center",
            "cursor": "pointer",
            "transition": "all 0.2s ease",
            "_hover": {
                "background": colors["surface"],
                "border_color": colors["border_light"]
            }
        }
    )

def Sidebar() -> rx.Component:
    """Professional sidebar navigation."""
    
    # Navigation items configuration
    main_nav = [
        {"icon": "layout-dashboard", "label": "Dashboard", "view": "dashboard"},
        {"icon": "users", "label": "Clients", "view": "clients"},
        {"icon": "shopping-bag", "label": "Orders", "view": "orders"},
        {"icon": "bar-chart-3", "label": "Analytics", "view": "analytics"},
    ]
    
    return rx.box(
        rx.box(
            # Header with logo
            rx.box(
                rx.hstack(
                    rx.box(
                        rx.icon(
                            "zap",
                            size=24,
                            color=colors["primary"]
                        ),
                        style={
                            "padding": "8px",
                            "background": colors["primary"] + "20",
                            "border_radius": "12px",
                            "border": f"1px solid {colors['primary']}40"
                        }
                    ),
                    rx.cond(
                        ~AppState.sidebar_collapsed,
                        rx.vstack(
                            rx.text(
                                "IntegraQS",
                                style={
                                    **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                    "font_weight": "700",
                                    "line_height": "1.2"
                                }
                            ),
                            rx.text(
                                "Pro ERP",
                                style={
                                    **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                    "margin_top": "-4px",
                                    "color": colors["primary"]
                                }
                            ),
                            align="start",
                            spacing="0"
                        )
                    ),
                    spacing="3",
                    align="center",
                    width="100%"
                ),
                style={
                    "padding": "20px 16px",
                    "border_bottom": f"1px solid {colors['border']}",
                    "margin_bottom": "24px"
                }
            ),
            
            # Main navigation
            rx.box(
                _nav_section("Main", main_nav),
                style={"padding": "0 16px"}
            ),
            
            # Quick stats
            rx.box(
                _stats_card(),
                style={"padding": "0 16px"}
            ),
            
            # Spacer
            rx.box(flex="1"),
            
            # Bottom user info
            rx.cond(
                ~AppState.sidebar_collapsed,
                rx.box(
                    rx.hstack(
                        rx.box(
                            rx.icon(
                                "user",
                                size=16,
                                color=colors["text_secondary"]
                            ),
                            style={
                                "width": "32px",
                                "height": "32px",
                                "background": colors["surface"],
                                "border_radius": "50%",
                                "display": "flex",
                                "align_items": "center",
                                "justify_content": "center"
                            }
                        ),
                        rx.vstack(
                            rx.text(
                                "Administrator",
                                style={
                                    **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                    "font_weight": "500",
                                    "line_height": "1.2"
                                }
                            ),
                            rx.text(
                                "Online",
                                style={
                                    **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                    "color": colors["success"],
                                    "margin_top": "-2px"
                                }
                            ),
                            align="start",
                            spacing="0"
                        ),
                        spacing="3",
                        align="center",
                        width="100%"
                    ),
                    style={
                        "padding": "16px",
                        "border_top": f"1px solid {colors['border']}",
                        "margin": "20px 16px 0"
                    }
                )
            ),
            
            # Toggle button
            _toggle_button(),
            
            style={
                "height": "100vh",
                "display": "flex",
                "flex_direction": "column",
                "position": "relative"
            }
        ),
        
        style={
            "width": rx.cond(AppState.sidebar_collapsed, "80px", "280px"),
            "transition": "width 0.3s cubic-bezier(0.4,0,0.2,1)",
            "background": colors["surface"],
            "backdrop_filter": "blur(20px)",
                            "border_right": f"1px solid {colors['border']}",
            "box_shadow": "2px 0 10px rgba(0,0,0,0.1)",
            "position": "fixed",
            "left": "0",
            "top": "0",
            "z_index": "1000",
            "overflow": "hidden"
        }
    )
