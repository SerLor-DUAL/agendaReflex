"""
Modern Design System for Reflex Dashboard Application.

This module provides a consistent design system with:
- Standardized color variants with opacity
- Reusable component patterns
- Consistent spacing and typography
- Responsive utilities
"""

from .colorPallet import ColorPallet

colors = ColorPallet().colors

# -------------------------
# COLOR SYSTEM
# -------------------------
class ColorSystem:
    """Standardized color system with opacity variants."""
    
    @staticmethod
    def get_color_variant(color_name: str, opacity: int = 100) -> str:
        """Get color with specified opacity (10-100)."""
        base_color = colors.get(color_name, colors["primary"])
        
        # Convert to hex if not already
        if base_color.startswith("#"):
            # Remove # and convert to RGB
            hex_color = base_color.lstrip("#")
            r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            alpha = opacity / 100
            return f"rgba({r}, {g}, {b}, {alpha})"
        
        return base_color
    
    @staticmethod
    def get_status_colors(status: str) -> dict:
        """Get colors for status badges."""
        status_map = {
            "active": "success",
            "inactive": "textMuted", 
            "pending": "warning",
            "completed": "success",
            "cancelled": "error",
            "default": "textMuted"
        }
        
        color_key = status_map.get(status.lower(), "textMuted")
        return {
            "color": colors[color_key],
            "bg": ColorSystem.get_color_variant(color_key, 20),
            "border": ColorSystem.get_color_variant(color_key, 40)
        }

# -------------------------
# SPACING SYSTEM
# -------------------------
class Spacing:
    """Consistent spacing system."""
    xs = "4px"
    sm = "8px"
    md = "16px"
    lg = "24px"
    xl = "32px"
    xxl = "48px"

# -------------------------
# TYPOGRAPHY SYSTEM
# -------------------------
class Typography:
    """Typography utilities."""
    
    @staticmethod
    def get_text_style(variant: str = "body") -> dict:
        """Get standardized text styles."""
        styles = {
            "h1": {"font_size": "32px", "font_weight": "700", "line_height": "1.2"},
            "h2": {"font_size": "24px", "font_weight": "600", "line_height": "1.3"},
            "h3": {"font_size": "20px", "font_weight": "600", "line_height": "1.3"},
            "body": {"font_size": "14px", "font_weight": "400", "line_height": "1.5"},
            "caption": {"font_size": "12px", "font_weight": "400", "line_height": "1.4"},
        }
        
        base_style = {
            "color": colors["text"],
            "letter_spacing": "-0.025em"
        }
        
        return {**base_style, **styles.get(variant, styles["body"])}

# -------------------------
# COMPONENT PATTERNS
# -------------------------
class ComponentStyles:
    """Reusable component style patterns."""
    
    @staticmethod
    def get_card_style(variant: str = "default") -> dict:
        """Get card styles."""
        base = {
            "background": colors["cards"],
            "border": f"1px solid {colors['border']}",
            "border_radius": "16px",
            "padding": Spacing.lg,
            "transition": "all 0.2s ease"
        }
        
        variants = {
            "default": {},
            "hover": {
                "_hover": {
                    "transform": "translateY(-2px)",
                    "box_shadow": f"0 8px 24px {ColorSystem.get_color_variant('textMuted', 15)}"
                }
            },
            "interactive": {
                "cursor": "pointer",
                "_hover": {
                    "transform": "translateY(-1px)",
                    "border_color": colors["borderLight"]
                }
            }
        }
        
        return {**base, **variants.get(variant, {})}
    
    @staticmethod
    def get_button_style(variant: str = "primary", size: str = "md") -> dict:
        """Get button styles."""
        sizes = {
            "sm": {"height": "32px", "padding": f"{Spacing.xs} {Spacing.sm}", "font_size": "13px"},
            "md": {"height": "40px", "padding": f"{Spacing.sm} {Spacing.md}", "font_size": "14px"},
            "lg": {"height": "48px", "padding": f"{Spacing.md} {Spacing.lg}", "font_size": "16px"}
        }
        
        variants = {
            "primary": {
                "background": colors["primary"],
                "color": colors["text"],
                "border": "none"
            },
            "secondary": {
                "background": "transparent",
                "color": colors["textSecondary"],
                "border": f"1px solid {colors['border']}"
            },
            "ghost": {
                "background": "transparent",
                "color": colors["textSecondary"],
                "border": "none"
            }
        }
        
        base = {
            "border_radius": "8px",
            "font_weight": "500",
            "cursor": "pointer",
            "transition": "all 0.2s ease",
            "display": "flex",
            "align_items": "center",
            "justify_content": "center",
            "_hover": {
                "opacity": "0.9",
                "transform": "translateY(-1px)"
            }
        }
        
        return {**base, **sizes.get(size, sizes["md"]), **variants.get(variant, variants["primary"])}
    
    @staticmethod
    def get_input_style() -> dict:
        """Get input field styles."""
        return {
            "background": colors["surface"],
            "border": f"1px solid {colors['border']}",
            "border_radius": "8px",
            "padding": f"{Spacing.sm} {Spacing.md}",
            "font_size": "14px",
            "transition": "all 0.2s ease",
            "_focus": {
                "outline": "none",
                "border_color": colors["primary"],
                "box_shadow": f"0 0 0 3px {ColorSystem.get_color_variant('primary', 10)}"
            },
            "_placeholder": {
                "color": colors["textMuted"]
            }
        }

# -------------------------
# LAYOUT UTILITIES
# -------------------------
class Layout:
    """Layout utilities and patterns."""
    
    @staticmethod
    def get_container_style(max_width: str = "1200px") -> dict:
        """Get container styles."""
        return {
            "width": "100%",
            "max_width": max_width,
            "margin": "0 auto",
            "padding": f"0 {Spacing.lg}"
        }
    
    @staticmethod
    def get_page_style() -> dict:
        """Get page wrapper styles."""
        return {
            "min_height": "100vh",
            "background": colors["generalBackground"],
            "padding": Spacing.lg
        }
    
    @staticmethod
    def get_grid_style(columns: int = 1, gap: str = None) -> dict:
        """Get grid layout styles."""
        if gap is None:
            gap = Spacing.lg
            
        return {
            "display": "grid",
            "grid_template_columns": f"repeat({columns}, 1fr)",
            "gap": gap,
            "width": "100%"
        }
