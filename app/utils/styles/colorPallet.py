class ColorPallet:
    def __init__(self):
        self.colors = {
            # Modern minimalist backgrounds
            "background": "#0F0F0F",          # Deep dark navbar/header
            "generalBackground": "#111111",  # Main background - pure dark
            "cards": "#1A1A1A",              # Card backgrounds - subtle lift
            "surface": "#252525",            # Interactive surfaces
            
            # Glass morphism effects
            "glassBackground": "rgba(26, 26, 26, 0.8)",
            "glassBorder": "rgba(255, 255, 255, 0.1)",
            
            # Modern brand colors
            "accent": "#00D2FF",             # Bright cyan accent
            "primary": "#0099CC",            # Modern blue primary
            "primaryHover": "#0088BB",       # Hover state
            "primaryActive": "#0077AA",      # Active state
            "secondary": "#333333",          # Subtle secondary
            "success": "#10B981",            # Success green
            "warning": "#F59E0B",            # Warning amber
            "error": "#EF4444",              # Error red
            
            # Modern text hierarchy
            "text": "#FFFFFF",               # Pure white text
            "textSecondary": "#A1A1AA",      # Secondary text - zinc-400
            "textMuted": "#71717A",          # Muted text - zinc-500
            "textDisabled": "#52525B",       # Disabled text - zinc-600
            
            # Modern borders and focus
            "border": "#27272A",             # Subtle border - zinc-800
            "borderLight": "#3F3F46",        # Light border - zinc-700
            "focus": "#00D2FF",              # Focus ring - cyan
            "focusRing": "rgba(0, 210, 255, 0.3)", # Focus ring with opacity
            
            # Gradients for modern effects
            "gradientPrimary": "linear-gradient(135deg, #0099CC 0%, #00D2FF 100%)",
            "gradientDark": "linear-gradient(180deg, #0F0F0F 0%, #1A1A1A 100%)",
        }
