import reflex as rx
from typing import Literal, Optional
from utils.styles.modern_styles import get_modern_avatar_styles, get_avatar_size
from utils.styles.colorPallet.colorPallet import ColorPallet

AvatarSize = Literal["sm", "md", "lg"]

def Avatar(src: Optional[str] = None, alt: str = "avatar", size: AvatarSize = "md", fallback: Optional[str] = None, **props,) -> rx.Component:
    """Avatar component with support for sizes and fallback."""

    base_styles = get_modern_avatar_styles()
    size_styles = get_avatar_size(size)

    styles = {**base_styles, **size_styles}

    if src:
        # Avatar con imagen
        return rx.image(src=src, alt=alt, style=styles, **props)

    # Fallback: iniciales, emoji o un icono
    fallback_content = (
        rx.text(
            fallback or alt[0].upper(),
            style={
                "color": ColorPallet().colors["text"],
                "font_weight": "600",
                "font_size": "14px" if size == "sm" else "16px",
            },
        )
    )

    return rx.center(
        fallback_content,
        style={**styles, "background": ColorPallet().colors["surface"]},
        **props,
    )
