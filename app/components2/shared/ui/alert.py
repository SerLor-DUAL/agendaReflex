import reflex as rx
from typing import Literal, Optional
from utils.styles.modern_styles import get_modern_alert_styles

AlertVariant = Literal["info", "success", "warning", "error"]

def Alert(children: str = "", variant: AlertVariant = "info", dismissible: bool = False, title: Optional[str] = None, **props) -> rx.Component:
    """Alert component with multiple variants."""
    
    config = get_modern_alert_styles(variant)

    # Alert body
    content = [
        rx.icon(config["icon"], size=18, color=config["color"]),
        rx.vstack(
            rx.cond(
                title,
                rx.text(
                    title,
                    style={"font_weight": "600", "color": config["color"]},
                ),
            ),
            rx.text(children, style={"color": config["text_color"]}),
            spacing="1",
            align="start",
            width="100%",
        ),
    ]

    # Optional dismiss button
    if dismissible:
        content.append(
            rx.button(
                rx.icon("x", size=14),
                variant="ghost",
                size="1",
                style={"margin_left": "auto"},
                aria_label="Close alert",
            )
        )

    # Final wrapper
    return rx.box(
        rx.hstack(*content, align="start", width="100%"),
        role="alert",
        style={
            "background": config["bg"],
            "border": config["border"],
            "padding": "12px",
            "border_radius": "12px",
            "display": "flex",
            "align_items": "flex-start",
            "gap": "8px",
        },
        **props,
    )