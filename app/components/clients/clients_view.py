import reflex as rx
from typing import Dict, Any
from ...state.app_state import AppState
from ...utils.styles import (
    colors, 
    spacing, 
    typography, 
    get_card_styles,
    get_button_styles,
    get_input_styles,
    get_badge_styles,
    get_text_styles
)
from ..shared import Card, CardHeader, CardBody, CardFooter, Button, Input, Badge, StatusBadge

def _search_bar() -> rx.Component:
    """Search bar component using new design system."""
    return rx.box(
        rx.hstack(
            Input(
                placeholder="Search clients by name, email or phone...",
                value=AppState.clients_search_query,
                on_change=AppState.set_clients_search_query,
                icon_left="search",
                width="100%"
            ),
            Button(
                "Add Client",
                variant="primary",
                size="md",
                on_click=lambda: AppState.open_client_modal("")
            ),
            spacing=spacing["md"],
            align="center",
            width="100%"
        ),
        style={
            "margin_bottom": spacing["xl"]
        }
    )

def _client_status_badge(status: str) -> rx.Component:
    """Client status badge using new design system."""
    return StatusBadge(status, size="sm")

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
                                    **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
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
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                "color": colors["text_muted"],
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
                        rx.icon("mail", size=16, color=colors["text_muted"]),
                        rx.text(
                            client.get("email", "No email"),
                            style={
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                "color": colors["text_secondary"]
                            }
                        ),
                        spacing="2",
                        align="center",
                        width="100%"
                    ),
                    rx.hstack(
                        rx.icon("phone", size=16, color=colors["text_muted"]),
                        rx.text(
                            client.get("phone", "No phone"),
                            style={
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                "color": colors["text_secondary"]
                            }
                        ),
                        spacing="2",
                        align="center",
                        width="100%"
                    ),
                    rx.hstack(
                        rx.icon("map", size=16, color=colors["text_muted"]),
                        rx.text(
                            client.get("address", "No address"),
                            style={
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                "color": colors["text_secondary"],
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
                        **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                        "color": colors["text_muted"]
                    }
                ),
                rx.box(flex="1"),
                rx.hstack(
                    rx.box(
                        rx.icon("settings", size=14, color=colors["text_muted"]),
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
                    color=colors["text_muted"]
                ),
                style={
                    "padding": "24px",
                    "background": f"{colors['text_muted']}10",
                    "border_radius": "50%",
                    "border": f"1px solid {colors['text_muted']}20"
                }
            ),
            rx.text(
                "No clients found",
                style={
                    **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                    "font_weight": "600",
                    "color": colors["text_muted"]
                }
            ),
            rx.text(
                "Add your first client to get started",
                style={
                    **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                    "color": colors["text_muted"],
                    "text_align": "center"
                }
            ),
            rx.box(
                rx.text(
                    "Add Client",
                    style={
                        **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                        "color": colors["primary"],
                        "font_weight": "500"
                    }
                ),
                on_click=lambda: AppState.open_client_modal(""),
                style={
                    **get_button_styles(variant="outline", size="md"),
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
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                "color": colors["text_muted"],
                                "font_weight": "500"
                            }
                        ),
                        rx.text(
                            AppState.clients_stats["total"],
                            style={
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
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
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                "color": colors["text_muted"],
                                "font_weight": "500"
                            }
                        ),
                        rx.text(
                            AppState.clients_stats["active"],
                            style={
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
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
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                "color": colors["text_muted"],
                                "font_weight": "500"
                            }
                        ),
                        rx.text(
                            AppState.clients_stats["inactive"],
                            style={
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                "font_size": "24px",
                                "font_weight": "700",
                                "color": colors["text_muted"]
                            }
                        ),
                        align="start",
                        spacing="1",
                        flex="1"
                    ),
                    rx.icon("user", size=24, color=colors["text_muted"]),
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
                            **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                            "font_size": "28px",
                            "font_weight": "700"
                        }
                    ),
                    rx.text(
                        "Manage your client relationships and contact information.",
                        style={
                            **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                            "color": colors["text_muted"]
                        }
                    ),
                    align="start",
                    spacing="1"
                ),
                rx.box(
                    rx.hstack(
                        rx.icon("download", size=16, color=colors["text_secondary"]),
                        rx.text(
                            "Export",
                            style={
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                "color": colors["text_secondary"],
                                "font_weight": "500"
                            }
                        ),
                        spacing="2",
                        align="center"
                    ),
                    style={
                        **get_button_styles(variant="ghost", size="sm"),
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
