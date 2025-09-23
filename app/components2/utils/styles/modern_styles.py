"""
Modern CSS utilities and styles for consistent minimalist design in Reflex.
"""

from .colorPallet.colorPallet import ColorPallet

colors = ColorPallet().colors

# -------------------------
# BUTTON STYLES
# -------------------------
def get_modern_button_styles():
    """Estilos base de todos los botones"""
    return {
        "position": "relative",
        "overflow": "hidden",
        "border": f"1px solid {colors['glassBorder']}",
        "border_radius": "12px",
        "backdrop_filter": "blur(10px)",
        "transition": "all 0.3s cubic-bezier(0.4,0,0.2,1)",
        "cursor": "pointer",
        "font_weight": "500",
        "letter_spacing": "0.025em",
        "_hover": {
            "transform": "translateY(-1px)",
            "box_shadow": f"0 10px 30px -10px {colors['focusRing']}",
            "border_color": colors['focus'],
        },
        "_active": {"transform": "translateY(0px)"},
        "_before": {
            "content": "''",
            "position": "absolute",
            "top": "0",
            "left": "-100%",
            "width": "100%",
            "height": "100%",
            "background": f"linear-gradient(90deg, transparent, {colors['focusRing']}, transparent)",
            "transition": "left 0.5s",
        },
    }

def get_button_variant(variant: str):
    """Configuración de colores según variante"""
    return {
        "primary": {
            "bg": colors["gradientPrimary"],
            "color": colors["text"],
            "border": "none",
            "hover_bg": colors["primaryHover"],
        },
        "secondary": {
            "bg": colors["secondary"],
            "color": colors["textSecondary"],
            "border": f"1px solid {colors['border']}",
            "hover_bg": colors["surface"],
        },
        "outline": {
            "bg": "transparent",
            "color": colors["primary"],
            "border": f"2px solid {colors['primary']}",
            "hover_bg": colors["primary"],
            "hover_color": colors["text"],
        },
        "ghost": {
            "bg": "transparent",
            "color": colors["text"],
            "border": "none",
            "hover_bg": colors["surface"],
        },
        "destructive": {
            "bg": colors["error"],
            "color": colors["text"],
            "border": "none",
            "hover_bg": "#DC2626",
        },
    }[variant]

def get_button_size(size: str):
    return {
        "xs": {"height": "28px", "padding": "4px 8px", "font_size": "12px"},
        "sm": {"height": "32px", "padding": "6px 12px", "font_size": "13px"},
        "md": {"height": "36px", "padding": "8px 16px", "font_size": "14px"},
        "lg": {"height": "40px", "padding": "10px 20px", "font_size": "15px"},
        "xl": {"height": "44px", "padding": "12px 24px", "font_size": "16px"},
    }[size]

# -------------------------
# CARD STYLES
# -------------------------
def get_modern_card_styles():
    return {
        "background": colors['glassBackground'],
        "backdrop_filter": "blur(20px)",
        "border": f"1px solid {colors['glassBorder']}",
        "border_radius": "16px",
        "box_shadow": "0 8px 32px rgba(0,0,0,0.3)",
        "transition": "all 0.3s cubic-bezier(0.4,0,0.2,1)",
        "_hover": {
            "transform": "translateY(-2px)",
            "box_shadow": "0 12px 48px rgba(0,0,0,0.4)",
            "border_color": colors['borderLight'],
        },
    }

def get_card_variant(variant: str):
    return {
        "default": {},
        "elevated": {"box_shadow": "0 12px 48px rgba(0,0,0,0.4)"},
        "outlined": {"background": "transparent", "border": f"2px solid {colors['border']}"},
        "filled": {"background": colors["surface"]},
    }[variant]

def get_card_size(size: str):
    return {
        "sm": {"padding": "16px", "border_radius": "12px"},
        "md": {"padding": "24px", "border_radius": "16px"},
        "lg": {"padding": "32px", "border_radius": "20px"},
    }[size]

# -------------------------
# INPUT STYLES
# -------------------------
def get_modern_input_styles():
    return {
        "background": colors['surface'],
        "border": f"1px solid {colors['border']}",
        "border_radius": "12px",
        "padding": "12px 16px",
        "transition": "all 0.2s cubic-bezier(0.4,0,0.2,1)",
        "font_size": "14px",
        "_focus": {
            "outline": "none",
            "border_color": colors['focus'],
            "box_shadow": f"0 0 0 3px {colors['focusRing']}",
            "background": colors['cards'],
        },
        "_placeholder": {"color": colors['textMuted']},
    }

def get_input_variant(variant: str):
    return {
        "default": {},
        "filled": {"background": colors["surface"], "border": "none"},
        "flushed": {"background": "transparent", "border": "none", "border_bottom": f"1px solid {colors['border']}"},
    }[variant]

def get_input_size(size: str):
    return {
        "sm": {"height": "32px", "padding": "6px 12px", "font_size": "13px"},
        "md": {"height": "36px", "padding": "8px 16px", "font_size": "14px"},
        "lg": {"height": "40px", "padding": "10px 20px", "font_size": "15px"},
    }[size]

# -------------------------
# TEXT STYLES
# -------------------------
def get_modern_text_styles(variant="body"):
    base_styles = {"letter_spacing": "-0.025em", "line_height": "1.5"}
    return {
        "heading": {**base_styles, "font_weight": "700", "font_size": "24px", "color": colors['text'], "letter_spacing": "-0.05em"},
        "subheading": {**base_styles, "font_weight": "600", "font_size": "18px", "color": colors['text']},
        "body": {**base_styles, "font_weight": "400", "font_size": "14px", "color": colors['textSecondary']},
        "caption": {**base_styles, "font_weight": "400", "font_size": "12px", "color": colors['textMuted']},
    }.get(variant, base_styles)

# -------------------------
# ALERT / TOAST STYLES
# -------------------------
def get_modern_alert_styles(variant: str):
    return {
        "info": {"bg": f"{colors['primary']}20", "border": f"1px solid {colors['primary']}40", "color": colors["primary"], "icon": "info"},
        "success": {"bg": f"{colors['success']}20", "border": f"1px solid {colors['success']}40", "color": colors["success"], "icon": "check-circle"},
        "warning": {"bg": f"{colors['warning']}20", "border": f"1px solid {colors['warning']}40", "color": colors["warning"], "icon": "alert-triangle"},
        "error": {"bg": f"{colors['error']}20", "border": f"1px solid {colors['error']}40", "color": colors["error"], "icon": "x-circle"},
    }[variant]

# -------------------------
# AVATAR STYLES
# -------------------------
def get_modern_avatar_styles():
    return {
        "border_radius": "50%",
        "object_fit": "cover",
        "border": f"2px solid {colors['borderLight']}",
        "box_shadow": "0 2px 6px rgba(0,0,0,0.15)",
    }

def get_avatar_size(size: str):
    return {
        "sm": {"width": "32px", "height": "32px"},
        "md": {"width": "40px", "height": "40px"},
        "lg": {"width": "56px", "height": "56px"},
    }[size]

# -------------------------
# BADGE STYLES
# -------------------------
def get_modern_badge_styles(variant: str):
    return {
        "primary": {
            "background": colors["primary"],
            "color": colors["text"],
        },
        "secondary": {
            "background": colors["secondary"],
            "color": colors["textSecondary"],
        },
        "success": {
            "background": colors["success"],
            "color": colors["text"],
        },
        "warning": {
            "background": colors["warning"],
            "color": colors["text"],
        },
        "error": {
            "background": colors["error"],
            "color": colors["text"],
        },
    }[variant]

# -------------------------
# ANIMATIONS
# -------------------------
def get_animation_styles():
    return {
        "fadeIn": {"animation": "fadeIn 0.3s ease-in-out"},
        "slideUp": {"animation": "slideUp 0.4s cubic-bezier(0.4,0,0.2,1)"},
        "scaleIn": {"animation": "scaleIn 0.2s cubic-bezier(0.4,0,0.2,1)"},
    }
