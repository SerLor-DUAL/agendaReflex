"""
Design Tokens for Reflex Application

This module defines all design tokens following Reflex conventions:
- Colors, spacing, typography, shadows, etc.
- Semantic color mappings
- Component-specific token configurations
"""

from typing import Dict, Any

# ===========================
# COLOR PALETTE
# ===========================
class Colors:
    """Design system colors following modern dark theme patterns."""
    
    # Base colors
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    
    # Grays
    GRAY_50 = "#F8FAFC"
    GRAY_100 = "#F1F5F9" 
    GRAY_200 = "#E2E8F0"
    GRAY_300 = "#CBD5E1"
    GRAY_400 = "#94A3B8"
    GRAY_500 = "#64748B"
    GRAY_600 = "#475569"
    GRAY_700 = "#334155"
    GRAY_800 = "#1E293B"
    GRAY_900 = "#0F172A"
    
    # Brand colors
    BLUE_400 = "#60A5FA"
    BLUE_500 = "#3B82F6"
    BLUE_600 = "#2563EB"
    BLUE_700 = "#1D4ED8"
    
    CYAN_400 = "#22D3EE"
    CYAN_500 = "#06B6D4"
    CYAN_600 = "#0891B2"
    
    # Status colors
    GREEN_400 = "#4ADE80"
    GREEN_500 = "#22C55E"
    GREEN_600 = "#16A34A"
    
    YELLOW_400 = "#FACC15"
    YELLOW_500 = "#EAB308"
    YELLOW_600 = "#CA8A04"
    
    RED_400 = "#F87171"
    RED_500 = "#EF4444" 
    RED_600 = "#DC2626"

# ===========================
# SEMANTIC COLOR MAPPING
# ===========================
class SemanticColors:
    """Semantic color mapping for consistent theming."""
    
    # Background colors
    BACKGROUND = "#0A0A0A"           # Pure dark background
    SURFACE = "#1A1A1A"             # Card/surface backgrounds
    SURFACE_ELEVATED = "#252525"    # Elevated surfaces
    
    # Text colors
    TEXT_PRIMARY = Colors.WHITE
    TEXT_SECONDARY = Colors.GRAY_400
    TEXT_MUTED = Colors.GRAY_500
    TEXT_DISABLED = Colors.GRAY_600
    
    # Border colors  
    BORDER = Colors.GRAY_800
    BORDER_LIGHT = Colors.GRAY_700
    BORDER_FOCUS = Colors.CYAN_400
    
    # Brand colors
    PRIMARY = Colors.BLUE_500
    PRIMARY_HOVER = Colors.BLUE_400
    PRIMARY_ACTIVE = Colors.BLUE_600
    
    ACCENT = Colors.CYAN_400
    
    # Status colors
    SUCCESS = Colors.GREEN_500
    WARNING = Colors.YELLOW_500  
    ERROR = Colors.RED_500
    INFO = Colors.BLUE_500
    
    # Interactive colors
    HOVER_OVERLAY = "rgba(255, 255, 255, 0.05)"
    ACTIVE_OVERLAY = "rgba(255, 255, 255, 0.1)"
    FOCUS_RING = "rgba(34, 211, 238, 0.3)"  # Cyan with opacity

# ===========================
# SPACING SYSTEM
# ===========================
class Spacing:
    """Reflex-compliant spacing system using string values."""
    
    # Reflex spacing scale (0-9)
    XS = "1"    # 4px
    SM = "2"    # 8px  
    MD = "4"    # 16px
    LG = "6"    # 24px
    XL = "8"    # 32px
    XXL = "9"   # 48px
    
    # Pixel values for custom styles
    PIXEL_XS = "4px"
    PIXEL_SM = "8px"
    PIXEL_MD = "16px"
    PIXEL_LG = "24px"
    PIXEL_XL = "32px"
    PIXEL_XXL = "48px"

# ===========================
# TYPOGRAPHY SCALE
# ===========================
class Typography:
    """Typography system with semantic naming."""
    
    # Font families
    FONT_FAMILY = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    FONT_FAMILY_MONO = "'Fira Code', 'Monaco', 'Cascadia Code', monospace"
    
    # Font sizes (following Reflex size scale)
    # SIZE_XS = "12px"    # size="1"
    # SIZE_SM = "14px"    # size="2" 
    # SIZE_MD = "16px"    # size="3"
    # SIZE_LG = "18px"    # size="4"
    # SIZE_XL = "24px"    # size="6"
    # SIZE_2XL = "32px"   # size="8"
    
    SIZE_XS = "1"    # 12px
    SIZE_SM = "2"    # 14px
    SIZE_MD = "3"    # 16px
    SIZE_LG = "4"    # 18px
    SIZE_LG2 = "5"   # 20px
    SIZE_XL = "6"    # 24px
    SIZE_2XL = "7"   # 28px
    SIZE_3XL = "8"   # 32px
    
    # Font weights
    WEIGHT_NORMAL = "400"
    WEIGHT_MEDIUM = "500"
    WEIGHT_SEMIBOLD = "600"
    WEIGHT_BOLD = "700"
    WEIGHT_EXTRABOLD = "800"
    
    # Line heights
    LINE_HEIGHT_TIGHT = "1.25"
    LINE_HEIGHT_NORMAL = "1.5"
    LINE_HEIGHT_RELAXED = "1.625"

# ===========================
# COMPONENT TOKENS
# ===========================
class ComponentTokens:
    """Component-specific design tokens."""
    
    # Border radius
    RADIUS_SM = "6px"
    RADIUS_MD = "8px"
    RADIUS_LG = "12px"
    RADIUS_XL = "16px"
    RADIUS_FULL = "9999px"
    
    # Shadows
    SHADOW_SM = "0 1px 2px rgba(0, 0, 0, 0.05)"
    SHADOW_MD = "0 4px 6px rgba(0, 0, 0, 0.1)"
    SHADOW_LG = "0 10px 15px rgba(0, 0, 0, 0.1)"
    SHADOW_XL = "0 20px 25px rgba(0, 0, 0, 0.15)"
    
    # Transitions
    TRANSITION_FAST = "0.15s ease"
    TRANSITION_NORMAL = "0.3s ease"
    TRANSITION_SLOW = "0.5s ease"
    
    # Z-index scale
    Z_INDEX_DROPDOWN = "100"
    Z_INDEX_STICKY = "200"
    Z_INDEX_FIXED = "300"
    Z_INDEX_MODAL_BACKDROP = "400"
    Z_INDEX_MODAL = "500"
    Z_INDEX_POPOVER = "600"
    Z_INDEX_TOOLTIP = "700"
    Z_INDEX_TOAST = "1000"

# ===========================
# THEME CONFIGURATION
# ===========================
def get_theme_config() -> Dict[str, Any]:
    """
    Get complete theme configuration for the application.
    
    Returns:
        Dict containing all theme tokens organized by category
    """
    return {
        "colors": {
            # Semantic colors for easy access
            "background": SemanticColors.BACKGROUND,
            "surface": SemanticColors.SURFACE,
            "surface_elevated": SemanticColors.SURFACE_ELEVATED,
            
            "text_primary": SemanticColors.TEXT_PRIMARY,
            "text_secondary": SemanticColors.TEXT_SECONDARY,
            "text_muted": SemanticColors.TEXT_MUTED,
            "text_disabled": SemanticColors.TEXT_DISABLED,
            
            "border": SemanticColors.BORDER,
            "border_light": SemanticColors.BORDER_LIGHT,
            "border_focus": SemanticColors.BORDER_FOCUS,
            
            "primary": SemanticColors.PRIMARY,
            "primary_hover": SemanticColors.PRIMARY_HOVER,
            "primary_active": SemanticColors.PRIMARY_ACTIVE,
            "accent": SemanticColors.ACCENT,
            
            "success": SemanticColors.SUCCESS,
            "warning": SemanticColors.WARNING,
            "error": SemanticColors.ERROR,
            "info": SemanticColors.INFO,
            
            "hover_overlay": SemanticColors.HOVER_OVERLAY,
            "active_overlay": SemanticColors.ACTIVE_OVERLAY,
            "focus_ring": SemanticColors.FOCUS_RING,
        },
        
        "spacing": {
            "xs": Spacing.XS,
            "sm": Spacing.SM,
            "md": Spacing.MD,
            "lg": Spacing.LG,
            "xl": Spacing.XL,
            "xxl": Spacing.XXL,
        },
        
        "typography": {
            "font_family": Typography.FONT_FAMILY,
            "font_family_mono": Typography.FONT_FAMILY_MONO,
            "sizes": {
                "xs": Typography.SIZE_XS,
                "sm": Typography.SIZE_SM,
                "md": Typography.SIZE_MD,
                "lg": Typography.SIZE_LG,
                "xl": Typography.SIZE_XL,
                "2xl": Typography.SIZE_2XL,
            },
            "weights": {
                "normal": Typography.WEIGHT_NORMAL,
                "medium": Typography.WEIGHT_MEDIUM,
                "semibold": Typography.WEIGHT_SEMIBOLD,
                "bold": Typography.WEIGHT_BOLD,
                "extrabold": Typography.WEIGHT_EXTRABOLD,
            },
            "line_heights": {
                "tight": Typography.LINE_HEIGHT_TIGHT,
                "normal": Typography.LINE_HEIGHT_NORMAL,
                "relaxed": Typography.LINE_HEIGHT_RELAXED,
            }
        },
        
        "components": {
            "radius": {
                "sm": ComponentTokens.RADIUS_SM,
                "md": ComponentTokens.RADIUS_MD,
                "lg": ComponentTokens.RADIUS_LG,
                "xl": ComponentTokens.RADIUS_XL,
                "full": ComponentTokens.RADIUS_FULL,
            },
            "shadows": {
                "sm": ComponentTokens.SHADOW_SM,
                "md": ComponentTokens.SHADOW_MD,
                "lg": ComponentTokens.SHADOW_LG,
                "xl": ComponentTokens.SHADOW_XL,
            },
            "transitions": {
                "fast": ComponentTokens.TRANSITION_FAST,
                "normal": ComponentTokens.TRANSITION_NORMAL,
                "slow": ComponentTokens.TRANSITION_SLOW,
            },
            "z_index": {
                "dropdown": ComponentTokens.Z_INDEX_DROPDOWN,
                "sticky": ComponentTokens.Z_INDEX_STICKY,
                "fixed": ComponentTokens.Z_INDEX_FIXED,
                "modal_backdrop": ComponentTokens.Z_INDEX_MODAL_BACKDROP,
                "modal": ComponentTokens.Z_INDEX_MODAL,
                "popover": ComponentTokens.Z_INDEX_POPOVER,
                "tooltip": ComponentTokens.Z_INDEX_TOOLTIP,
                "toast": ComponentTokens.Z_INDEX_TOAST,
            }
        }
    }
