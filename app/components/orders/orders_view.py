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
    get_text_styles
)
from ..shared import Card, CardHeader, CardBody, CardFooter

# Colors now imported directly from design system

def _order_status_badge(status: str) -> rx.Component:
    """Order status badge with appropriate colors."""
    status_config = {
        "pending": {"color": colors["warning"], "bg": f"{colors['warning']}20"},
        "completed": {"color": colors["success"], "bg": f"{colors['success']}20"},
        "cancelled": {"color": colors["error"], "bg": f"{colors['error']}20"},
    }
    
    config = status_config.get(status, {
        "color": colors["text_muted"],
        "bg": f"{colors['text_muted']}20"
    })
    
    return rx.box(
        rx.text(
            status,
            style={
                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                "color": config["color"],
                "font_weight": "500",
                "text_transform": "capitalize"
            }
        ),
        style={
            "padding": "4px 12px",
            "background": config["bg"],
            "border": f"1px solid {config['color']}40",
            "border_radius": "20px",
            "display": "inline-flex",
            "align_items": "center"
        }
    )

def _search_and_filters() -> rx.Component:
    """Search bar with status filters."""
    return rx.vstack(
        # Search bar
        rx.box(
            rx.hstack(
                rx.box(
                    rx.icon("search", size=18, color=colors["text_muted"]),
                    style={
                        "position": "absolute",
                        "left": "12px",
                        "top": "50%",
                        "transform": "translateY(-50%)",
                        "z_index": "1"
                    }
                ),
                rx.input(
                    placeholder="Search orders by ID, client or description...",
                    value=AppState.orders_search_query,
                    on_change=AppState.set_orders_search_query,
                    style={
                        **get_input_styles(),
                        "padding_left": "44px",
                        "width": "100%"
                    }
                ),
                style={"position": "relative", "flex": "1"}
            ),
            rx.box(
                rx.text(
                    "Create Order",
                    style={
                        **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                        "color": colors["text_primary"],
                        "font_weight": "500"
                    }
                ),
                on_click=lambda: AppState.open_order_modal(""),
                style={
                    **get_button_styles(variant="primary", size="md"),
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
                "width": "100%"
            }
        ),
        
        # Status filters
        rx.hstack(
            rx.text(
                "Filter by status:",
                style={
                    **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                    "color": colors["text_muted"],
                    "font_weight": "500"
                }
            ),
            rx.hstack(
                rx.box(
                    rx.text(
                        "All",
                        style={
                            **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                            "color": colors["primary"],
                            "font_weight": "500"
                        }
                    ),
                    on_click=lambda: AppState.set_orders_status_filter("all"),
                    style={
                        "padding": "8px 16px",
                        "border_radius": "8px",
                        "cursor": "pointer",
                        "transition": "all 0.2s ease",
                        "background": f"{colors['primary']}20",
                        "border": f"1px solid {colors['primary']}40",
                        "_hover": {
                            "background": f"{colors['primary']}15"
                        }
                    }
                ),
                rx.box(
                    rx.text(
                        "Pending",
                        style={
                            **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                            "color": colors["text_secondary"],
                            "font_weight": "500"
                        }
                    ),
                    on_click=lambda: AppState.set_orders_status_filter("pending"),
                    style={
                        "padding": "8px 16px",
                        "border_radius": "8px",
                        "cursor": "pointer",
                        "transition": "all 0.2s ease",
                        "background": "transparent",
                        "border": "1px solid transparent",
                        "_hover": {
                            "background": f"{colors['warning']}15"
                        }
                    }
                ),
                rx.box(
                    rx.text(
                        "Completed",
                        style={
                            **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                            "color": colors["text_secondary"],
                            "font_weight": "500"
                        }
                    ),
                    on_click=lambda: AppState.set_orders_status_filter("completed"),
                    style={
                        "padding": "8px 16px",
                        "border_radius": "8px",
                        "cursor": "pointer",
                        "transition": "all 0.2s ease",
                        "background": "transparent",
                        "border": "1px solid transparent",
                        "_hover": {
                            "background": f"{colors['success']}15"
                        }
                    }
                ),
                rx.box(
                    rx.text(
                        "Cancelled",
                        style={
                            **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                            "color": colors["text_secondary"],
                            "font_weight": "500"
                        }
                    ),
                    on_click=lambda: AppState.set_orders_status_filter("cancelled"),
                    style={
                        "padding": "8px 16px",
                        "border_radius": "8px",
                        "cursor": "pointer",
                        "transition": "all 0.2s ease",
                        "background": "transparent",
                        "border": "1px solid transparent",
                        "_hover": {
                            "background": f"{colors['error']}15"
                        }
                    }
                ),
                spacing="2"
            ),
            spacing="4",
            align="center",
            width="100%"
        ),
        
        spacing="4",
        width="100%",
        align="start",
        margin_bottom="24px"
    )

def _order_row(order: Dict[str, Any]) -> rx.Component:
    """Single order row for the table."""
    return rx.box(
        rx.hstack(
            # Order ID and Date
            rx.vstack(
                rx.text(
                    f"#{order.get('id', 'N/A')}",
                    style={
                        **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                        "font_weight": "600",
                        "color": colors["primary"]
                    }
                ),
                rx.text(
                    order.get("created_at", "Unknown"),
                    style={
                        **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                        "color": colors["text_muted"]
                    }
                ),
                align="start",
                spacing="1",
                min_width="120px"
            ),
            
            # Client
            rx.vstack(
                rx.text(
                    order.get("client_name", "Unknown Client"),
                    style={
                        **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                        "font_weight": "500"
                    }
                ),
                rx.text(
                    "Client",
                    style={
                        **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                        "color": colors["text_muted"]
                    }
                ),
                align="start",
                spacing="1",
                flex="1",
                min_width="150px"
            ),
            
            # Description
            rx.vstack(
                rx.text(
                    order.get("description", "No description"),
                    style={
                        **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                        "overflow": "hidden",
                        "text_overflow": "ellipsis",
                        "white_space": "nowrap",
                        "max_width": "200px"
                    }
                ),
                rx.text(
                    "Description",
                    style={
                        **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                        "color": colors["text_muted"]
                    }
                ),
                align="start",
                spacing="1",
                flex="2",
                min_width="200px"
            ),
            
            # Amount
            rx.vstack(
                rx.text(
                    f"€{order.get('amount', 0):,.2f}",
                    style={
                        **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                        "font_weight": "600",
                        "color": colors["success"]
                    }
                ),
                rx.text(
                    "Amount",
                    style={
                        **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                        "color": colors["text_muted"]
                    }
                ),
                align="start",
                spacing="1",
                min_width="120px"
            ),
            
            # Status
            rx.vstack(
                _order_status_badge(order.get("status", "pending")),
                rx.text(
                    "Status",
                    style={
                        **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                        "color": colors["text_muted"]
                    }
                ),
                align="start",
                spacing="1",
                min_width="100px"
            ),
            
            # Actions
            rx.hstack(
                rx.box(
                    rx.icon("settings", size=14, color=colors["text_muted"]),
                    on_click=lambda order_id=str(order.get("id", "")): AppState.open_order_modal(order_id),
                    style={
                        "padding": "8px",
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
                        "padding": "8px",
                        "border_radius": "6px",
                        "cursor": "pointer",
                        "transition": "all 0.2s ease",
                        "_hover": {
                            "background": f"{colors['error']}20"
                        }
                    }
                ),
                spacing="1",
                min_width="80px"
            ),
            
            spacing="6",
            align="center",
            width="100%",
            justify="start"
        ),
        style={
            "padding": "20px",
            "border_bottom": f"1px solid {colors['border']}",
            "transition": "background 0.2s ease",
            "_hover": {
                "background": colors["surface"]
            }
        }
    )

def _orders_table_header() -> rx.Component:
    """Table header for orders."""
    return rx.box(
        rx.hstack(
            rx.text(
                "Order ID",
                style={
                    **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                    "font_weight": "600",
                    "color": colors["text_muted"]
                },
                min_width="120px"
            ),
            rx.text(
                "Client",
                style={
                    **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                    "font_weight": "600",
                    "color": colors["text_muted"]
                },
                flex="1",
                min_width="150px"
            ),
            rx.text(
                "Description",
                style={
                    **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                    "font_weight": "600",
                    "color": colors["text_muted"]
                },
                flex="2",
                min_width="200px"
            ),
            rx.text(
                "Amount",
                style={
                    **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                    "font_weight": "600",
                    "color": colors["text_muted"]
                },
                min_width="120px"
            ),
            rx.text(
                "Status",
                style={
                    **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                    "font_weight": "600",
                    "color": colors["text_muted"]
                },
                min_width="100px"
            ),
            rx.text(
                "Actions",
                style={
                    **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                    "font_weight": "600",
                    "color": colors["text_muted"]
                },
                min_width="80px"
            ),
            spacing="6",
            align="center",
            width="100%",
            justify="start"
        ),
        style={
            "padding": "20px",
            "border_bottom": f"2px solid {colors['border']}",
            "background": colors["surface"]
        }
    )

def _orders_table() -> rx.Component:
    """Orders table component."""
    return Card(
        CardBody(
            rx.vstack(
                _orders_table_header(),
                rx.cond(
                    AppState.filtered_orders.length() > 0,
                    rx.vstack(
                        rx.foreach(
                            AppState.filtered_orders,
                            _order_row
                        ),
                        spacing="0",
                        width="100%"
                    ),
                    rx.center(
                        rx.vstack(
                            rx.icon(
                                "shopping-bag",
                                size=48,
                                color=colors["text_muted"]
                            ),
                            rx.text(
                                "No orders found",
                                style={
                                    **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                    "font_weight": "600",
                                    "color": colors["text_muted"]
                                }
                            ),
                            rx.text(
                                "Create your first order to get started",
                                style={
                                    **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                    "color": colors["text_muted"]
                                }
                            ),
                            spacing="3",
                            align="center"
                        ),
                        style={
                            "padding": "60px 20px",
                            "width": "100%"
                        }
                    )
                ),
                spacing="0",
                width="100%"
            )
        ),
        size="sm",
        style={"overflow": "hidden"}
    )

def _stats_summary() -> rx.Component:
    """Order statistics summary."""
    return rx.grid(
        Card(
            CardBody(
                rx.hstack(
                    rx.vstack(
                        rx.text(
                            "Total Orders",
                            style={
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                "color": colors["text_muted"],
                                "font_weight": "500"
                            }
                        ),
                        rx.text(
                            AppState.orders_stats["total"],
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
                    rx.icon("shopping-bag", size=24, color=colors["primary"]),
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
                            "Pending",
                            style={
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                "color": colors["text_muted"],
                                "font_weight": "500"
                            }
                        ),
                        rx.text(
                            AppState.orders_stats["pending"],
                            style={
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                "font_size": "24px",
                                "font_weight": "700",
                                "color": colors["warning"]
                            }
                        ),
                        align="start",
                        spacing="1",
                        flex="1"
                    ),
                    rx.icon("clock", size=24, color=colors["warning"]),
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
                            "Completed",
                            style={
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                "color": colors["text_muted"],
                                "font_weight": "500"
                            }
                        ),
                        rx.text(
                            AppState.orders_stats["completed"],
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
                    rx.icon("check", size=24, color=colors["success"]),
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
                            "Cancelled",
                            style={
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                "color": colors["text_muted"],
                                "font_weight": "500"
                            }
                        ),
                        rx.text(
                            AppState.orders_stats["cancelled"],
                            style={
                                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                                "font_size": "24px",
                                "font_weight": "700",
                                "color": colors["error"]
                            }
                        ),
                        align="start",
                        spacing="1",
                        flex="1"
                    ),
                    rx.icon("x", size=24, color=colors["error"]),
                    justify="between",
                    align="center",
                    width="100%"
                )
            ),
            size="sm"
        ),
        columns="4",
        spacing="4",
        width="100%",
        margin_bottom="32px"
    )

def OrdersView() -> rx.Component:
    """Professional orders management view."""
    return rx.vstack(
        # Page header
        rx.box(
            rx.hstack(
                rx.vstack(
                    rx.text(
                        "Order Management",
                        style={
                            **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                            "font_size": "28px",
                            "font_weight": "700"
                        }
                    ),
                    rx.text(
                        "Track and manage all your orders from creation to completion.",
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
                # Search and filters
                _search_and_filters(),
                
                # Stats summary
                _stats_summary(),
                
                # Orders table
                _orders_table(),
                
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
