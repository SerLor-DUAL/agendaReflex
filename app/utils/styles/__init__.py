"""
Styles Module - Centralized Design System

This module provides a comprehensive design system with:
- Design tokens (colors, typography, spacing, etc.)
- Theme configuration
- Component-specific style utilities
- Layout helpers and responsive utilities

Usage Examples:
    from app.utils.styles import colors, spacing, get_button_styles
    from app.utils.styles.theme import get_base_app_styles
    from app.utils.styles.components import get_card_styles
"""

# Import main theme configuration and tokens
from .theme import (
    THEME,
    colors,
    spacing,
    typography,
    components,
    get_colors,
    get_spacing,
    get_typography,
    get_component_tokens,
    get_base_app_styles,
    get_container_styles,
    get_flex_styles,
    get_grid_styles,
    get_responsive_styles,
    with_hover_effect,
    with_focus_ring,
    get_text_styles,
    get_slide_in_styles,
    get_fade_in_styles,
    Breakpoints
)

# Import design tokens directly
from .tokens import (
    Colors,
    SemanticColors,
    Spacing,
    Typography,
    ComponentTokens,
    get_theme_config
)

# Import component style utilities
from .components import (
    get_button_styles,
    get_card_styles,
    get_input_styles,
    get_modal_styles,
    get_modal_backdrop_styles,
    get_table_styles,
    get_table_header_styles,
    get_table_cell_styles,
    get_badge_styles,
    get_nav_link_styles,
    get_divider_styles,
    get_loading_spinner_styles
)

# Export commonly used items for convenience
__all__ = [
    # Theme and tokens
    "THEME",
    "colors",
    "spacing", 
    "typography",
    "components",
    "Colors",
    "SemanticColors",
    "Spacing",
    "Typography",
    "ComponentTokens",
    "Breakpoints",
    
    # Theme functions
    "get_colors",
    "get_spacing", 
    "get_typography",
    "get_component_tokens",
    "get_theme_config",
    "get_base_app_styles",
    "get_container_styles",
    "get_flex_styles",
    "get_grid_styles",
    "get_responsive_styles",
    "get_text_styles",
    
    # Utility functions
    "with_hover_effect",
    "with_focus_ring",
    "get_slide_in_styles",
    "get_fade_in_styles",
    
    # Component styles
    "get_button_styles",
    "get_card_styles", 
    "get_input_styles",
    "get_modal_styles",
    "get_modal_backdrop_styles",
    "get_table_styles",
    "get_table_header_styles",
    "get_table_cell_styles",
    "get_badge_styles",
    "get_nav_link_styles",
    "get_divider_styles",
    "get_loading_spinner_styles"
]

# Version info
__version__ = "1.0.0"
