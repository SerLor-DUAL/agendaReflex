import reflex as rx
from ...utils.styles.colorPallet import ColorPallet
from ...utils.styles.modern_styles import get_modern_text_styles

colors = ColorPallet().colors

def Logo(company_name: str = "IntegraQS", size: str = "large") -> rx.Component:
    """
    Prominent logo component with modern styling and hover animations.
    
    Args:
        company_name: The company name to display
        size: "large" for desktop, "small" for mobile
    
    Returns:
        rx.Component: A modern logo component
    """
    
    # Size configurations
    sizes = {
        "large": {
            "image_size": "48px",
            "font_size": "24px",
            "spacing": "3"
        },
        "small": {
            "image_size": "36px", 
            "font_size": "20px",
            "spacing": "2"
        }
    }
    
    config = sizes.get(size, sizes["large"])
    
    return rx.hstack(
        # Company logo image - more prominent
        rx.image(
            src="/img/logo.png", 
            alt=f"{company_name} Logo",
            width=config["image_size"],
            height=config["image_size"],
            border_radius="12px",
            style={
                "filter": "brightness(1.2) saturate(1.1)",
                "transition": "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
                "box_shadow": "0 4px 20px rgba(0, 153, 204, 0.2)",
                "_hover": {
                    "transform": "scale(1.08) rotate(2deg)",
                    "filter": "brightness(1.3) saturate(1.2)",
                    "box_shadow": "0 8px 30px rgba(0, 153, 204, 0.4)",
                }
            }
        ),
        
        # Company name with gradient text
        rx.text(
            company_name,
            style={
                **get_modern_text_styles(colors, "heading"),
                "font_size": config["font_size"],
                "font_weight": "800",
                "letter_spacing": "-0.02em",
                "background": colors["gradientPrimary"],
                "background_clip": "text",
                "color": "transparent",
                "text_shadow": "0 2px 4px rgba(0, 0, 0, 0.1)",
                "cursor": "pointer",
                "transition": "all 0.3s ease",
                "_hover": {
                    "transform": "translateY(-1px)",
                    "filter": "brightness(1.1)",
                }
            }
        ),
        
        align="center",
        spacing=config["spacing"],
        cursor="pointer",
        style={
            "transition": "all 0.3s ease",
            "_hover": {
                "transform": "translateY(-1px)"
            }
        }
    )
