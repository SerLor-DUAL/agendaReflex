import reflex as rx
from ...utils.styles import colors, spacing, typography, get_card_styles, get_button_styles, get_text_styles

# Colors now imported directly from design system

def HeroSection(
    title: str = "Welcome to IntegraQS",
    subtitle: str = "Modern business management made simple",
    size: str = "compact"
) -> rx.Component:
    """
    Modular hero section component with customizable content.
    
    Args:
        title: Main hero title
        subtitle: Hero subtitle/description
        size: "compact" or "large" for different sizing options
    
    Returns:
        rx.Component: Hero section with gradient text and animations
    """
    
    # Size configurations
    sizes = {
        "compact": {
            "title_size": "6",
            "title_weight": "700",
            "subtitle_size": "16px",
            "max_width": "400px",
            "spacing": "2",
            "margin_bottom": "24px"
        },
        "large": {
            "title_size": "8", 
            "title_weight": "800",
            "subtitle_size": "20px",
            "max_width": "600px",
            "spacing": "4",
            "margin_bottom": "48px"
        }
    }
    
    config = sizes.get(size, sizes["compact"])
    
    return rx.vstack(
        # Hero title with gradient
        rx.heading(
            title,
            size=config["title_size"],
            style={
                "color": colors["primary"],
                "font_weight": config["title_weight"],
                "letter_spacing": "-0.03em",
                "text_align": "center",
                "margin_bottom": "8px",
                "line_height": "1.2",
                "animation": "fadeIn 0.6s ease-out",
            }
        ),
        
        # Hero subtitle
        rx.text(
            subtitle,
            style={
                **get_text_styles(size=typography["sizes"]["md"], color=colors["text_primary"]),
                "text_align": "center",
                "font_size": config["subtitle_size"],
                "color": colors["text_secondary"],
                "margin_bottom": "16px",
                "max_width": config["max_width"],
                "animation": "fadeIn 0.6s ease-out 0.2s both",
            }
        ),
        
        spacing=config["spacing"],
        align="center",
        width="100%",
        margin_bottom=config["margin_bottom"],
        style={
            "animation": "slideUp 0.8s ease-out"
        }
    )
