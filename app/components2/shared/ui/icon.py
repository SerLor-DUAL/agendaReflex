import reflex as rx
from typing import Optional
from ....utils.colorPallet.colorPallet import ColorPallet

colors = ColorPallet().colors

def Icon(
    name: str,
    size: int = 16,
    color: Optional[str] = None,
    **props
) -> rx.Component:
    """
    Icon component.

    Args:
        name: Icon name
        size: Icon size in px
        color: Optional color (defaults to text color)
        **props: Additional styling props

    Returns:
        rx.Component: Styled icon
    """
    return rx.icon(
        name,
        size=size,
        color=color or colors["text"],
        **props
    )
