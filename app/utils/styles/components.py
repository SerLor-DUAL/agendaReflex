"""
Component Style Utilities

This module provides reusable style functions for common UI components,
ensuring consistency across the application while following Reflex best practices.
"""

from typing import Dict, Any, Optional
from .theme import colors, spacing, typography, components, with_hover_effect, with_focus_ring

# ===========================
# BUTTON STYLES
# ===========================
def get_button_styles(
    variant: str = "primary",
    size: str = "md",
    full_width: bool = False,
    disabled: bool = False
) -> Dict[str, Any]:
    """
    Generate consistent button styles.
    
    Args:
        variant: Button variant (primary, secondary, outline, ghost, danger)
        size: Button size (sm, md, lg)
        full_width: Whether button should take full width
        disabled: Whether button is disabled
        
    Returns:
        Dict containing button styles
    """
    # Size configurations
    size_configs = {
        "sm": {
            "height": "32px",
            "padding_x": spacing["sm"],
            "font_size": typography["sizes"]["sm"],
        },
        "md": {
            "height": "40px", 
            "padding_x": spacing["md"],
            "font_size": typography["sizes"]["md"],
        },
        "lg": {
            "height": "48px",
            "padding_x": spacing["lg"],
            "font_size": typography["sizes"]["lg"],
        }
    }
    
    # Variant configurations
    variant_configs = {
        "primary": {
            "background": colors["primary"],
            "color": colors["text_primary"],
            "border": f"1px solid {colors['primary']}",
            "_hover": {
                "background": colors["primary_hover"],
                "border": f"1px solid {colors['primary_hover']}",
            }
        },
        "secondary": {
            "background": colors["surface"],
            "color": colors["text_primary"],
            "border": f"1px solid {colors['border']}",
            "_hover": {
                "background": colors["surface_elevated"],
                "border": f"1px solid {colors['border_light']}",
            }
        },
        "outline": {
            "background": "transparent",
            "color": colors["primary"],
            "border": f"1px solid {colors['primary']}",
            "_hover": {
                "background": colors["primary"],
                "color": colors["text_primary"],
            }
        },
        "ghost": {
            "background": "transparent",
            "color": colors["text_primary"],
            "border": "1px solid transparent",
            "_hover": {
                "background": colors["hover_overlay"],
            }
        },
        "danger": {
            "background": colors["error"],
            "color": colors["text_primary"],
            "border": f"1px solid {colors['error']}",
            "_hover": {
                "background": "#DC2626",  # Slightly darker red
                "border": "1px solid #DC2626",
            }
        }
    }
    
    # Base styles
    base_styles = {
        "display": "inline-flex",
        "align_items": "center",
        "justify_content": "center",
        "font_weight": typography["weights"]["medium"],
        "font_family": typography["font_family"],
        "border_radius": components["radius"]["md"],
        "transition": components["transitions"]["fast"],
        "cursor": "pointer",
        "text_decoration": "none",
        "outline": "none",
        "gap": spacing["xs"],
        **size_configs.get(size, size_configs["md"]),
        **variant_configs.get(variant, variant_configs["primary"])
    }
    
    # Full width modifier
    if full_width:
        base_styles["width"] = "100%"
    
    # Disabled state
    if disabled:
        base_styles.update({
            "opacity": "0.5",
            "cursor": "not-allowed",
            "_hover": {},  # Remove hover effects
        })
    
    # Add focus ring
    base_styles = with_focus_ring(base_styles)
    
    return base_styles

# ===========================
# CARD STYLES  
# ===========================
def get_card_styles(
    variant: str = "default",
    padding: str = "md",
    hoverable: bool = False,
    elevated: bool = False
) -> Dict[str, Any]:
    """
    Generate consistent card styles.
    
    Args:
        variant: Card variant (default, outline, filled)
        padding: Card padding size token
        hoverable: Whether card should have hover effects
        elevated: Whether card should have elevation shadow
        
    Returns:
        Dict containing card styles
    """
    # Base styles
    base_styles = {
        "background": colors["surface"],
        "border_radius": components["radius"]["lg"],
        "padding": spacing.get(padding, spacing["md"]),
        "transition": components["transitions"]["normal"],
    }
    
    # Variant configurations
    if variant == "outline":
        base_styles["border"] = f"1px solid {colors['border']}"
    elif variant == "filled":
        base_styles["background"] = colors["surface_elevated"]
    else:  # default
        base_styles["border"] = f"1px solid {colors['border']}"
    
    # Elevation
    if elevated:
        base_styles["box_shadow"] = components["shadows"]["md"]
    
    # Hoverable effects
    if hoverable:
        base_styles = with_hover_effect(base_styles)
        base_styles["_hover"]["box_shadow"] = components["shadows"]["lg"]
    
    return base_styles

# ===========================
# INPUT STYLES
# ===========================
def get_input_styles(
    size: str = "md",
    variant: str = "default",
    error: bool = False,
    disabled: bool = False
) -> Dict[str, Any]:
    """
    Generate consistent input styles.
    
    Args:
        size: Input size (sm, md, lg)
        variant: Input variant (default, filled)
        error: Whether input has error state
        disabled: Whether input is disabled
        
    Returns:
        Dict containing input styles
    """
    # Size configurations
    size_configs = {
        "sm": {
            "height": "32px",
            "padding_x": spacing["sm"],
            "font_size": typography["sizes"]["sm"],
        },
        "md": {
            "height": "40px",
            "padding_x": spacing["md"], 
            "font_size": typography["sizes"]["md"],
        },
        "lg": {
            "height": "48px",
            "padding_x": spacing["lg"],
            "font_size": typography["sizes"]["lg"],
        }
    }
    
    # Base styles
    base_styles = {
        "width": "100%",
        "background": colors["surface"],
        "color": colors["text_primary"],
        "border": f"1px solid {colors['border']}",
        "border_radius": components["radius"]["md"],
        "font_family": typography["font_family"],
        "transition": components["transitions"]["fast"],
        "outline": "none",
        **size_configs.get(size, size_configs["md"])
    }
    
    # Variant configurations
    if variant == "filled":
        base_styles["background"] = colors["surface_elevated"]
    
    # Interactive states
    base_styles["_hover"] = {
        "border": f"1px solid {colors['border_light']}"
    }
    
    base_styles["_focus"] = {
        "border": f"1px solid {colors['border_focus']}",
        "box_shadow": f"0 0 0 3px {colors['focus_ring']}"
    }
    
    base_styles["_placeholder"] = {
        "color": colors["text_muted"]
    }
    
    # Error state
    if error:
        base_styles["border"] = f"1px solid {colors['error']}"
        base_styles["_focus"]["border"] = f"1px solid {colors['error']}"
        base_styles["_focus"]["box_shadow"] = f"0 0 0 3px rgba(239, 68, 68, 0.1)"
    
    # Disabled state
    if disabled:
        base_styles.update({
            "background": colors["surface"],
            "color": colors["text_disabled"],
            "cursor": "not-allowed",
            "_hover": {},
            "_focus": {},
        })
    
    return base_styles

# ===========================
# MODAL STYLES
# ===========================
def get_modal_styles(size: str = "md") -> Dict[str, Any]:
    """
    Generate consistent modal styles.
    
    Args:
        size: Modal size (sm, md, lg, xl)
        
    Returns:
        Dict containing modal styles
    """
    # Size configurations
    size_configs = {
        "sm": {"max_width": "400px"},
        "md": {"max_width": "500px"},
        "lg": {"max_width": "700px"},
        "xl": {"max_width": "900px"},
    }
    
    return {
        "background": colors["surface"],
        "border": f"1px solid {colors['border']}",
        "border_radius": components["radius"]["xl"],
        "box_shadow": components["shadows"]["xl"],
        "padding": spacing["xl"],
        "margin": spacing["md"],
        "width": "100%",
        **size_configs.get(size, size_configs["md"])
    }

def get_modal_backdrop_styles() -> Dict[str, Any]:
    """Get modal backdrop styles."""
    return {
        "position": "fixed",
        "top": "0",
        "left": "0",
        "right": "0",
        "bottom": "0",
        "background": "rgba(0, 0, 0, 0.5)",
        "display": "flex",
        "align_items": "center",
        "justify_content": "center",
        "z_index": components["z_index"]["modal_backdrop"],
        "backdrop_filter": "blur(4px)",
    }

# ===========================
# TABLE STYLES
# ===========================
def get_table_styles() -> Dict[str, Any]:
    """Generate consistent table styles."""
    return {
        "width": "100%",
        "border_collapse": "collapse",
        "background": colors["surface"],
        "border_radius": components["radius"]["lg"],
        "overflow": "hidden",
        "border": f"1px solid {colors['border']}",
    }

def get_table_header_styles() -> Dict[str, Any]:
    """Generate table header styles."""
    return {
        "background": colors["surface_elevated"],
        "color": colors["text_primary"],
        "font_weight": typography["weights"]["semibold"],
        "font_size": typography["sizes"]["sm"],
        "text_align": "left",
        "padding": spacing["md"],
        "border_bottom": f"1px solid {colors['border']}",
    }

def get_table_cell_styles(striped: bool = False, row_index: Optional[int] = None) -> Dict[str, Any]:
    """
    Generate table cell styles.
    
    Args:
        striped: Whether to use striped rows
        row_index: Row index for striped styling
        
    Returns:
        Dict containing table cell styles
    """
    base_styles = {
        "padding": spacing["md"],
        "border_bottom": f"1px solid {colors['border']}",
        "font_size": typography["sizes"]["md"],
        "color": colors["text_primary"],
    }
    
    if striped and row_index is not None and row_index % 2 == 0:
        base_styles["background"] = colors["surface"]
    elif striped:
        base_styles["background"] = colors["surface_elevated"]
        
    return base_styles

# ===========================
# BADGE/CHIP STYLES
# ===========================
def get_badge_styles(
    variant: str = "default",
    size: str = "md"
) -> Dict[str, Any]:
    """
    Generate consistent badge/chip styles.
    
    Args:
        variant: Badge variant (default, success, warning, error, info)
        size: Badge size (sm, md)
        
    Returns:
        Dict containing badge styles
    """
    # Size configurations
    size_configs = {
        "sm": {
            "font_size": typography["sizes"]["xs"],
            "padding_x": spacing["xs"],
            "padding_y": "2px",
            "height": "20px",
        },
        "md": {
            "font_size": typography["sizes"]["sm"],
            "padding_x": spacing["sm"],
            "padding_y": "4px",  
            "height": "24px",
        }
    }
    
    # Variant configurations
    variant_configs = {
        "default": {
            "background": colors["surface_elevated"],
            "color": colors["text_primary"],
            "border": f"1px solid {colors['border']}",
        },
        "success": {
            "background": colors["success"],
            "color": colors["text_primary"],
        },
        "warning": {
            "background": colors["warning"],
            "color": colors["background"],
        },
        "error": {
            "background": colors["error"],
            "color": colors["text_primary"],
        },
        "info": {
            "background": colors["info"],
            "color": colors["text_primary"],
        }
    }
    
    return {
        "display": "inline-flex",
        "align_items": "center",
        "font_weight": typography["weights"]["medium"],
        "font_family": typography["font_family"],
        "border_radius": components["radius"]["full"],
        "white_space": "nowrap",
        **size_configs.get(size, size_configs["md"]),
        **variant_configs.get(variant, variant_configs["default"])
    }

# ===========================
# NAVIGATION STYLES
# ===========================
def get_nav_link_styles(active: bool = False) -> Dict[str, Any]:
    """
    Generate navigation link styles.
    
    Args:
        active: Whether link is currently active
        
    Returns:
        Dict containing nav link styles
    """
    base_styles = {
        "display": "flex",
        "align_items": "center",
        "padding": spacing["sm"],
        "border_radius": components["radius"]["md"],
        "color": colors["text_secondary"],
        "text_decoration": "none",
        "transition": components["transitions"]["fast"],
        "gap": spacing["sm"],
        "font_weight": typography["weights"]["medium"],
    }
    
    if active:
        base_styles.update({
            "background": colors["primary"],
            "color": colors["text_primary"],
        })
    else:
        base_styles["_hover"] = {
            "background": colors["hover_overlay"],
            "color": colors["text_primary"],
        }
    
    return base_styles

# ===========================
# UTILITY FUNCTIONS
# ===========================
def get_divider_styles(orientation: str = "horizontal") -> Dict[str, Any]:
    """
    Generate divider styles.
    
    Args:
        orientation: Divider orientation (horizontal, vertical)
        
    Returns:
        Dict containing divider styles
    """
    if orientation == "vertical":
        return {
            "width": "1px",
            "height": "100%",
            "background": colors["border"],
            "margin_x": spacing["sm"],
        }
    else:  # horizontal
        return {
            "height": "1px",
            "width": "100%", 
            "background": colors["border"],
            "margin_y": spacing["sm"],
        }

def get_loading_spinner_styles(size: str = "md") -> Dict[str, Any]:
    """
    Generate loading spinner styles.
    
    Args:
        size: Spinner size (sm, md, lg)
        
    Returns:
        Dict containing spinner styles
    """
    sizes = {
        "sm": "16px",
        "md": "24px", 
        "lg": "32px"
    }
    
    return {
        "width": sizes.get(size, sizes["md"]),
        "height": sizes.get(size, sizes["md"]),
        "border": f"2px solid {colors['border']}",
        "border_top": f"2px solid {colors['primary']}",
        "border_radius": "50%",
        "animation": "spin 1s linear infinite",
        "@keyframes spin": {
            "0%": {"transform": "rotate(0deg)"},
            "100%": {"transform": "rotate(360deg)"},
        }
    }
