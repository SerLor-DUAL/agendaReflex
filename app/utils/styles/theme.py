"""
Main Theme Configuration for Reflex Application

This module provides the main theme configuration and helper functions
for accessing design tokens throughout the application.
"""

from typing import Dict, Any
from .tokens import get_theme_config, SemanticColors, Spacing, Typography, ComponentTokens

# ===========================
# MAIN THEME INSTANCE
# ===========================
THEME = get_theme_config()

# ===========================
# THEME ACCESS HELPERS
# ===========================
def get_colors() -> Dict[str, str]:
    """Get all theme colors."""
    return THEME["colors"]

def get_spacing() -> Dict[str, str]:
    """Get all spacing tokens."""
    return THEME["spacing"]

def get_typography() -> Dict[str, Any]:
    """Get all typography tokens."""
    return THEME["typography"]

def get_component_tokens() -> Dict[str, Any]:
    """Get all component-specific tokens."""
    return THEME["components"]

# ===========================
# QUICK ACCESS TO COMMON VALUES
# ===========================
# Colors for direct import
colors = get_colors()
spacing = get_spacing()
typography = get_typography()
components = get_component_tokens()

# ===========================
# BASE APPLICATION STYLES
# ===========================
def get_base_app_styles() -> Dict[str, str]:
    """
    Get base application styles that should be applied to the root component.
    
    Returns:
        Dict containing base CSS styles for the application
    """
    return {
        "background": colors["background"],
        "color": colors["text_primary"],
        "font_family": typography["font_family"],
        "font_size": typography["sizes"]["md"],
        "line_height": typography["line_heights"]["normal"],
        "min_height": "100vh",
        "overflow_x": "hidden",
    }

def get_container_styles(max_width: str = "1200px") -> Dict[str, str]:
    """
    Get container styles for main content areas.
    
    Args:
        max_width: Maximum width for the container
        
    Returns:
        Dict containing container styles
    """
    return {
        "max_width": max_width,
        "margin": "0 auto",
        "padding_x": spacing["md"],
        "width": "100%",
    }

# ===========================
# COMMON LAYOUT STYLES
# ===========================
def get_flex_styles(
    direction: str = "row", 
    align: str = "flex-start", 
    justify: str = "flex-start",
    wrap: str = "nowrap",
    gap: str = None
) -> Dict[str, str]:
    """
    Generate flex container styles.
    
    Args:
        direction: flex-direction value
        align: align-items value
        justify: justify-content value
        wrap: flex-wrap value
        gap: gap value (uses spacing token if provided)
        
    Returns:
        Dict containing flex styles
    """
    styles = {
        "display": "flex",
        "flex_direction": direction,
        "align_items": align,
        "justify_content": justify,
        "flex_wrap": wrap,
    }
    
    if gap:
        # If gap is a spacing token key, use the token value
        if gap in spacing:
            styles["gap"] = spacing[gap]
        else:
            styles["gap"] = gap
            
    return styles

def get_grid_styles(
    columns: str = "1fr",
    rows: str = "auto", 
    gap: str = None,
    align_items: str = "stretch",
    justify_items: str = "stretch"
) -> Dict[str, str]:
    """
    Generate grid container styles.
    
    Args:
        columns: grid-template-columns value
        rows: grid-template-rows value  
        gap: gap value (uses spacing token if provided)
        align_items: align-items value
        justify_items: justify-items value
        
    Returns:
        Dict containing grid styles
    """
    styles = {
        "display": "grid",
        "grid_template_columns": columns,
        "grid_template_rows": rows,
        "align_items": align_items,
        "justify_items": justify_items,
    }
    
    if gap:
        # If gap is a spacing token key, use the token value
        if gap in spacing:
            styles["gap"] = spacing[gap]
        else:
            styles["gap"] = gap
            
    return styles

# ===========================
# RESPONSIVE BREAKPOINTS
# ===========================
class Breakpoints:
    """Responsive breakpoints following common conventions."""
    
    # Mobile first approach
    SM = "640px"     # Small devices
    MD = "768px"     # Medium devices (tablets)
    LG = "1024px"    # Large devices (desktops)
    XL = "1280px"    # Extra large devices
    XXL = "1536px"   # Ultra wide devices

def get_responsive_styles() -> Dict[str, Dict[str, str]]:
    """
    Get responsive utilities for common breakpoints.
    
    Note: Reflex handles responsive styles differently.
    This is more for reference and planning responsive components.
    
    Returns:
        Dict containing breakpoint information
    """
    return {
        "breakpoints": {
            "sm": Breakpoints.SM,
            "md": Breakpoints.MD,
            "lg": Breakpoints.LG,
            "xl": Breakpoints.XL,
            "xxl": Breakpoints.XXL,
        },
        "container_max_widths": {
            "sm": "640px",
            "md": "768px", 
            "lg": "1024px",
            "xl": "1200px",
            "xxl": "1200px",  # Keep reasonable max width
        }
    }

# ===========================
# UTILITY FUNCTIONS
# ===========================
def with_hover_effect(base_styles: Dict[str, str], hover_color: str = None) -> Dict[str, str]:
    """
    Add hover effects to a style dictionary.
    
    Args:
        base_styles: Base styles to extend
        hover_color: Optional hover color override
        
    Returns:
        Dict with hover effects added
    """
    hover_styles = base_styles.copy()
    
    # Add hover effects
    hover_styles.update({
        "transition": components["transitions"]["normal"],
        "_hover": {
            "background": hover_color or colors["hover_overlay"],
            "transform": "translateY(-1px)",
            "cursor": "pointer",
        }
    })
    
    return hover_styles

def with_focus_ring(base_styles: Dict[str, str]) -> Dict[str, str]:
    """
    Add focus ring styles to a component.
    
    Args:
        base_styles: Base styles to extend
        
    Returns:
        Dict with focus ring styles added
    """
    focus_styles = base_styles.copy()
    focus_styles.update({
        "_focus": {
            "outline": "none",
            "box_shadow": f"0 0 0 3px {colors['focus_ring']}",
        }
    })
    
    return focus_styles

def get_text_styles(
    size: str = "md",
    weight: str = "normal", 
    color: str = None,
    line_height: str = "normal"
) -> Dict[str, str]:
    """
    Generate text styles with theme tokens.
    
    Args:
        size: Text size token key
        weight: Font weight token key
        color: Text color (defaults to primary text color)
        line_height: Line height token key
        
    Returns:
        Dict containing text styles
    """
    return {
        "font_size": typography["sizes"].get(size, typography["sizes"]["md"]),
        "font_weight": typography["weights"].get(weight, typography["weights"]["normal"]),
        "color": color or colors["text_primary"],
        "line_height": typography["line_heights"].get(line_height, typography["line_heights"]["normal"]),
        "font_family": typography["font_family"],
    }

# ===========================
# ANIMATION UTILITIES
# ===========================
def get_slide_in_styles(direction: str = "left") -> Dict[str, Any]:
    """
    Get slide-in animation styles.
    
    Args:
        direction: Direction to slide in from (left, right, top, bottom)
        
    Returns:
        Dict containing animation styles
    """
    transforms = {
        "left": "translateX(-100%)",
        "right": "translateX(100%)",
        "top": "translateY(-100%)",
        "bottom": "translateY(100%)",
    }
    
    return {
        "animation": "slideIn 0.3s ease-out",
        "@keyframes slideIn": {
            "from": {
                "transform": transforms.get(direction, transforms["left"]),
                "opacity": "0",
            },
            "to": {
                "transform": "translateX(0) translateY(0)",
                "opacity": "1",
            }
        }
    }

def get_fade_in_styles(duration: str = "0.3s") -> Dict[str, Any]:
    """
    Get fade-in animation styles.
    
    Args:
        duration: Animation duration
        
    Returns:
        Dict containing fade-in animation styles
    """
    return {
        "animation": f"fadeIn {duration} ease-out",
        "@keyframes fadeIn": {
            "from": {"opacity": "0"},
            "to": {"opacity": "1"},
        }
    }
