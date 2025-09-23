import reflex as rx
from ...utils.colorPallet.colorPallet import ColorPallet
from ...utils.styles.modern_styles import get_modern_text_styles

colors = ColorPallet().colors

def FormHeader(
    title: str,
    subtitle: str = "",
    show_logo: bool = False,
    logo_src: str = "/img/logo.png"
) -> rx.Component:
    """
    Reusable form header component with optional logo.
    
    Args:
        title: Main form title
        subtitle: Optional form subtitle
        show_logo: Whether to display the company logo
        logo_src: Path to the logo image
    
    Returns:
        rx.Component: Styled form header
    """
    
    return rx.vstack(
        # Optional logo
        rx.cond(
            show_logo,
            rx.image(
                src=logo_src,
                width="64px",
                height="64px",
                border_radius="16px",
                style={
                    "filter": "drop-shadow(0 4px 20px rgba(0, 153, 204, 0.3))",
                    "margin_bottom": "16px",
                    "animation": "scaleIn 0.5s ease-out"
                }
            ),
        ),
        
        # Form title
        rx.heading(
            title,
            size="6",
            style={
                **get_modern_text_styles(colors, "heading"),
                "text_align": "center",
                "margin_bottom": "8px" if subtitle else "24px",
                "animation": "fadeIn 0.6s ease-out"
            }
        ),
        
        # Optional subtitle
        rx.cond(
            subtitle != "",
            rx.text(
                subtitle,
                style={
                    **get_modern_text_styles(colors, "body"),
                    "text_align": "center",
                    "margin_bottom": "24px",
                    "animation": "fadeIn 0.6s ease-out 0.1s both"
                }
            ),
        ),
        
        align="center",
        width="100%",
        spacing="1"
    )
