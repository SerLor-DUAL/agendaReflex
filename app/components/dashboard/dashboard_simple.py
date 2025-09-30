"""
Simple Dashboard Component using the New Design System

A simplified dashboard that works with our current design system architecture.
"""

import reflex as rx
from ...utils.styles import (
    colors, 
    spacing, 
    typography,
    get_card_styles,
    get_button_styles,
    get_text_styles
)
from ..shared import Card, CardHeader, CardBody, Button

def _stats_card(title: str, value: str, icon: str) -> rx.Component:
    """Simple stats card component."""
    return Card(
        CardBody(
            rx.hstack(
                rx.vstack(
                    rx.text(
                        title,
                        style={
                            **get_text_styles(size=typography["sizes"]["sm"], color=colors["text_muted"]),
                            "font_weight": "500"
                        }
                    ),
                    rx.text(
                        value,
                        style={
                            **get_text_styles(size=typography["sizes"]["lg"], color=colors["text_primary"]),
                            "font_size": "24px",
                            "font_weight": "700",
                            "color": colors["primary"]
                        }
                    ),
                    align="start",
                    spacing="1",
                    flex="1"
                ),
                rx.icon(icon, size=24, color=colors["primary"]),
                justify="between",
                align="center",
                width="100%"
            )
        ),
        size="sm"
    )

def dashboard_view() -> rx.Component:
    """
    Main dashboard view using the new design system.
    
    A simplified dashboard that demonstrates:
    - Using design system colors, spacing, and typography
    - Leveraging reusable Card and Button components
    - Clean component composition
    """
    
    return rx.vstack(
        # Page header
        rx.box(
            rx.hstack(
                rx.vstack(
                    rx.text(
                        "Panel de control",
                        style={
                            **get_text_styles(size=typography["sizes"]["lg"], color=colors["text_primary"]),
                            "font_size": "28px",
                            "font_weight": "700"
                        }
                    ),
                    rx.text(
                        "¡Bienvenido! Aquí tienes un resumen de tu negocio.",
                        style={
                            **get_text_styles(size=typography["sizes"]["md"], color=colors["text_muted"])
                        }
                    ),
                    align="start",
                    spacing="1"
                ),
                rx.box(
                    rx.hstack(
                        rx.icon("refresh-cw", size=16, color=colors["text_secondary"]),
                        rx.text(
                            "Refrescar",
                            style={
                                **get_text_styles(size=typography["sizes"]["sm"], color=colors["text_secondary"]),
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
                # Stats section
                rx.text(
                    "Overview",
                    style={
                        **get_text_styles(size=typography["sizes"]["lg"], color=colors["text_primary"]),
                        "font_weight": "600",
                        "margin_bottom": spacing["lg"]
                    }
                ),
                
                # Stats grid
                rx.grid(
                    _stats_card("Total Clients", "127", "users"),
                    _stats_card("Active Orders", "23", "shopping-bag"),
                    _stats_card("Revenue", "$45,280", "dollar-sign"),
                    _stats_card("Completion Rate", "94.5%", "circle-check"),
                    columns="4",
                    spacing="4",
                    width="100%"
                ),
                
                # Welcome message
                Card(
                    CardHeader(
                        "",  # Empty children since we're using title/subtitle
                        title="Bienvenido a IntegraQS",
                        subtitle="Tu solución para la gestión del negocio"
                    ),
                    CardBody(
                        rx.vstack(
                            rx.text(
                                "¡Todo se ve bien! Tu panel de control muestra las actualizaciones recientes de tus operaciones comerciales.",
                                style={
                                    **get_text_styles(size=typography["sizes"]["md"], color=colors["text_secondary"]),
                                    "line_height": "1.6"
                                }
                            ),
                            rx.hstack(
                                Button("Ver clientes", variant="primary", size="sm"),
                                Button("Ver pedidos", variant="outline", size="sm"),
                                spacing="3",
                                align="center"
                            ),
                            spacing="4",
                            align="start",
                            width="100%"
                        )
                    ),
                    style={"margin_top": spacing["xl"]}
                ),
                
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
