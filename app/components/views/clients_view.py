import reflex as rx
from typing import Dict, Any
from ...state.app_state import AppState
from ...utils.styles.modern_styles import get_modern_card_styles, get_modern_text_styles, get_modern_input_styles, get_modern_button_styles, get_button_variant, get_button_size
from ...utils.styles.colorPallet import ColorPallet
from ..shared.card import Card, CardHeader, CardBody, CardFooter

colors = ColorPallet().colors

def _search_bar() -> rx.Component:
    """Search bar component."""
    return rx.box(
        rx.hstack(
            rx.box(
                rx.icon("search", size=18, color=colors["textMuted"]),
                style={
                    "position": "absolute",
                    "left": "12px",
                    "top": "50%",
                    "transform": "translateY(-50%)",
                    "z_index": "1"
                }
            ),
            rx.input(
                placeholder="Search clients by name, email or phone...",
                value=AppState.clients_search_query,
                on_change=AppState.set_clients_search_query,
                style={
                    **get_modern_input_styles(),
                    "padding_left": "44px",
                    "width": "100%"
                }
            ),
            style={"position": "relative", "flex": "1"}
        ),
        rx.box(
            rx.text(
                "Add Client",
                style={
                    **get_modern_text_styles(colors, "body"),
                    "color": colors["text"],
                    "font_weight": "500"
                }
            ),
            on_click=lambda: AppState.open_client_modal(""),
            style={
                **get_modern_button_styles(),
                **get_button_variant("primary"),
                **get_button_size("md"),
                "display": "flex",
                "align_items": "center",
                "justify_content": "center",
                "gap": "8px",
                "white_space": "nowrap"
            }
        ),
        style={
            "display": "flex",
            "gap": "16px",
            "align_items": "center",
            "width": "100%",
            "margin_bottom": "24px"
        }
    )

def _client_status_badge(status: str) -> rx.Component:
    """Client status badge."""
    return rx.cond(
        status == "active",
        rx.box(
            rx.text(
                "Active",
                style={
                    **get_modern_text_styles(colors, "caption"),
                    "color": colors["success"],
                    "font_weight": "500"
                }
            ),
            style={
                "padding": "4px 12px",
                "background": f"{colors['success']}20",
                "border": f"1px solid {colors['success']}40",
                "border_radius": "20px",
                "display": "inline-flex",
                "align_items": "center"
            }
        ),
        rx.box(
            rx.text(
                "Inactive",
                style={
                    **get_modern_text_styles(colors, "caption"),
                    "color": colors["textMuted"],
                    "font_weight": "500"
                }
            ),
            style={
                "padding": "4px 12px",
                "background": f"{colors['textMuted']}20",
                "border": f"1px solid {colors['textMuted']}40",
                "border_radius": "20px",
                "display": "inline-flex",
                "align_items": "center"
            }
        )
    )

def _client_card(client: Dict[str, Any]) -> rx.Component:
    """Individual client card."""
    return Card(
        CardBody(
            rx.vstack(
                # Client header
                rx.hstack(
                    rx.box(
                        rx.icon(
                            "user",
                            size=20,
                            color=colors["primary"]
                        ),
                        style={
                            "width": "48px",
                            "height": "48px",
                            "background": f"{colors['primary']}20",
                            "border_radius": "12px",
                            "border": f"1px solid {colors['primary']}40",
                            "display": "flex",
                            "align_items": "center",
                            "justify_content": "center"
                        }
                    ),
                    rx.vstack(
                        rx.hstack(
                            rx.text(
                                client.get("name", "Unknown"),
                                style={
                                    **get_modern_text_styles(colors, "subheading"),
                                    "font_weight": "600",
                                    "line_height": "1.2"
                                }
                            ),
                            _client_status_badge(client.get("status", "inactive")),
                            spacing="2",
                            align="center"
                        ),
                        rx.text(
                            client.get("company", "No company"),
                            style={
                                **get_modern_text_styles(colors, "body"),
                                "color": colors["textMuted"],
                                "margin_top": "-2px"
                            }
                        ),
                        align="start",
                        spacing="0",
                        flex="1"
                    ),
                    spacing="3",
                    align="start",
                    width="100%"
                ),
                
                # Divider
                rx.divider(color=colors["border"]),
                
                # Client details
                rx.vstack(
                    rx.hstack(
                        rx.icon("mail", size=16, color=colors["textMuted"]),
                        rx.text(
                            client.get("email", "No email"),
                            style={
                                **get_modern_text_styles(colors, "body"),
                                "color": colors["textSecondary"]
                            }
                        ),
                        spacing="2",
                        align="center",
                        width="100%"
                    ),
                    rx.hstack(
                        rx.icon("phone", size=16, color=colors["textMuted"]),
                        rx.text(
                            client.get("phone", "No phone"),
                            style={
                                **get_modern_text_styles(colors, "body"),
                                "color": colors["textSecondary"]
                            }
                        ),
                        spacing="2",
                        align="center",
                        width="100%"
                    ),
                    rx.hstack(
                        rx.icon("map", size=16, color=colors["textMuted"]),
                        rx.text(
                            client.get("address", "No address"),
                            style={
                                **get_modern_text_styles(colors, "body"),
                                "color": colors["textSecondary"],
                                "overflow": "hidden",
                                "text_overflow": "ellipsis",
                                "white_space": "nowrap"
                            }
                        ),
                        spacing="2",
                        align="center",
                        width="100%"
                    ),
                    spacing="2",
                    width="100%",
                    align="start"
                ),
                
                spacing="4",
                width="100%",
                align="start"
            )
        ),
        CardFooter(
            rx.hstack(
                rx.text(
                    "Created recently",
                    style={
                        **get_modern_text_styles(colors, "caption"),
                        "color": colors["textMuted"]
                    }
                ),
                rx.box(flex="1"),
                rx.hstack(
                    rx.box(
                        rx.icon("settings", size=14, color=colors["textMuted"]),
                        on_click=lambda client_id=str(client.get("id", "")): AppState.open_client_modal(client_id),
                        style={
                            "padding": "6px",
                            "border_radius": "6px",
                            "cursor": "pointer",
                            "transition": "all 0.2s ease",
                            "_hover": {
                                "background": colors["surface"],
                                "color": colors["primary"]
                            }
                        }
                    ),
                    rx.box(
                        rx.icon("trash", size=14, color=colors["error"]),
                        style={
                            "padding": "6px",
                            "border_radius": "6px",
                            "cursor": "pointer",
                            "transition": "all 0.2s ease",
                            "_hover": {
                                "background": f"{colors['error']}20"
                            }
                        }
                    ),
                    spacing="1"
                ),
                width="100%",
                align="center"
            )
        ),
        hover=True,
        size="sm"
    )

def _empty_state() -> rx.Component:
    """Empty state when no clients found."""
    return rx.center(
        rx.vstack(
            rx.box(
                rx.icon(
                    "users",
                    size=64,
                    color=colors["textMuted"]
                ),
                style={
                    "padding": "24px",
                    "background": f"{colors['textMuted']}10",
                    "border_radius": "50%",
                    "border": f"1px solid {colors['textMuted']}20"
                }
            ),
            rx.text(
                "No clients found",
                style={
                    **get_modern_text_styles(colors, "subheading"),
                    "font_weight": "600",
                    "color": colors["textMuted"]
                }
            ),
            rx.text(
                "Add your first client to get started",
                style={
                    **get_modern_text_styles(colors, "body"),
                    "color": colors["textMuted"],
                    "text_align": "center"
                }
            ),
            rx.box(
                rx.text(
                    "Add Client",
                    style={
                        **get_modern_text_styles(colors, "body"),
                        "color": colors["primary"],
                        "font_weight": "500"
                    }
                ),
                on_click=lambda: AppState.open_client_modal(""),
                style={
                    **get_modern_button_styles(),
                    **get_button_variant("outline"),
                    **get_button_size("md"),
                    "display": "flex",
                    "align_items": "center",
                    "justify_content": "center",
                    "margin_top": "16px"
                }
            ),
            spacing="4",
            align="center"
        ),
        style={
            "min_height": "400px",
            "width": "100%"
        }
    )

def _clients_grid() -> rx.Component:
    """Grid of client cards."""
    return rx.cond(
        AppState.filtered_clients.length() > 0,
        rx.grid(
            rx.foreach(
                AppState.filtered_clients,
                _client_card
            ),
            columns="3",
            spacing="6",
            width="100%"
        ),
        _empty_state()
    )

def _stats_summary() -> rx.Component:
    """Client statistics summary."""
    return rx.grid(
        Card(
            CardBody(
                rx.hstack(
                    rx.vstack(
                        rx.text(
                            "Total Clients",
                            style={
                                **get_modern_text_styles(colors, "body"),
                                "color": colors["textMuted"],
                                "font_weight": "500"
                            }
                        ),
                        rx.text(
                            AppState.clients_stats["total"],
                            style={
                                **get_modern_text_styles(colors, "heading"),
                                "font_size": "24px",
                                "font_weight": "700",
                                "color": colors["primary"]
                            }
                        ),
                        align="start",
                        spacing="1",
                        flex="1"
                    ),
                    rx.icon("users", size=24, color=colors["primary"]),
                    justify="between",
                    align="center",
                    width="100%"
                )
            ),
            size="sm"
        ),
        Card(
            CardBody(
                rx.hstack(
                    rx.vstack(
                        rx.text(
                            "Active Clients",
                            style={
                                **get_modern_text_styles(colors, "body"),
                                "color": colors["textMuted"],
                                "font_weight": "500"
                            }
                        ),
                        rx.text(
                            AppState.clients_stats["active"],
                            style={
                                **get_modern_text_styles(colors, "heading"),
                                "font_size": "24px",
                                "font_weight": "700",
                                "color": colors["success"]
                            }
                        ),
                        align="start",
                        spacing="1",
                        flex="1"
                    ),
                    rx.icon("user", size=24, color=colors["success"]),
                    justify="between",
                    align="center",
                    width="100%"
                )
            ),
            size="sm"
        ),
        Card(
            CardBody(
                rx.hstack(
                    rx.vstack(
                        rx.text(
                            "Inactive Clients",
                            style={
                                **get_modern_text_styles(colors, "body"),
                                "color": colors["textMuted"],
                                "font_weight": "500"
                            }
                        ),
                        rx.text(
                            AppState.clients_stats["inactive"],
                            style={
                                **get_modern_text_styles(colors, "heading"),
                                "font_size": "24px",
                                "font_weight": "700",
                                "color": colors["textMuted"]
                            }
                        ),
                        align="start",
                        spacing="1",
                        flex="1"
                    ),
                    rx.icon("user", size=24, color=colors["textMuted"]),
                    justify="between",
                    align="center",
                    width="100%"
                )
            ),
            size="sm"
        ),
        columns="3",
        spacing="4",
        width="100%",
        margin_bottom="32px"
    )

def ClientsView() -> rx.Component:
    """Professional client management view."""
    return rx.vstack(
        # Page header
        rx.box(
            rx.hstack(
                rx.vstack(
                    rx.text(
                        "Client Management",
                        style={
                            **get_modern_text_styles(colors, "heading"),
                            "font_size": "28px",
                            "font_weight": "700"
                        }
                    ),
                    rx.text(
                        "Manage your client relationships and contact information.",
                        style={
                            **get_modern_text_styles(colors, "body"),
                            "color": colors["textMuted"]
                        }
                    ),
                    align="start",
                    spacing="1"
                ),
                rx.box(
                    rx.hstack(
                        rx.icon("download", size=16, color=colors["textSecondary"]),
                        rx.text(
                            "Export",
                            style={
                                **get_modern_text_styles(colors, "body"),
                                "color": colors["textSecondary"],
                                "font_weight": "500"
                            }
                        ),
                        spacing="2",
                        align="center"
                    ),
                    style={
                        **get_modern_button_styles(),
                        **get_button_variant("ghost"),
                        **get_button_size("sm"),
                        "display": "flex",
                        "align_items": "center",
                        "justify_content": "center"
                    }
                ),
                justify="between",
                align="start",
                width="100%"
            ),
            style={
                "padding": "32px",
                "border_bottom": f"1px solid {colors['border']}"
            }
        ),
        
        # Main content
        rx.box(
            rx.vstack(
                # Search and actions
                _search_bar(),
                
                # Stats summary
                _stats_summary(),
                
                # Clients grid
                _clients_grid(),
                
                spacing="0",
                width="100%",
                align="start"
            ),
            style={"padding": "32px"}
        ),
        
        spacing="0",
        width="100%",
        align="start"
    )
