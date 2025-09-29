# Design System Usage Guide

This guide shows how to use the newly implemented centralized design system in your Reflex application.

## 🎨 **Quick Start**

### Basic Imports
```python
# Import design tokens and utilities
from app.utils.styles import colors, spacing, typography, get_button_styles

# Import pre-built components  
from app.components.shared.ui.button import Button, IconButton
from app.components.shared.ui.card import Card, StatsCard, CardHeader

# Import layout helpers
from app.utils.styles import get_flex_styles, get_grid_styles, get_container_styles
```

### Using Colors
```python
import reflex as rx
from app.utils.styles import colors

# Using semantic colors
rx.text("Primary text", color=colors["text_primary"])
rx.text("Secondary text", color=colors["text_secondary"]) 
rx.box(background=colors["surface"], border=f"1px solid {colors['border']}")
```

### Using Spacing
```python
from app.utils.styles import spacing

# Consistent spacing throughout your app
rx.box(
    margin=spacing["md"],          # 16px margin
    padding_x=spacing["lg"],       # 24px horizontal padding
    gap=spacing["sm"]              # 8px gap
)
```

### Using Typography
```python
from app.utils.styles import typography, get_text_styles

# Using typography tokens
rx.text(
    "Heading text", 
    font_size=typography["sizes"]["xl"],
    font_weight=typography["weights"]["bold"]
)

# Or use the helper function
rx.text("Body text", style=get_text_styles("md", "normal", colors["text_primary"]))
```

## 🧩 **Component Examples**

### Buttons
```python
from app.components.shared.ui.button import Button, IconButton

# Different button variants
Button("Primary Action", variant="primary", size="md")
Button("Secondary Action", variant="secondary", icon="plus", size="sm")
Button("Danger Action", variant="danger", full_width=True)

# Icon buttons
IconButton(icon="settings", variant="ghost", size="sm")
IconButton(icon="delete", variant="danger", size="lg")
```

### Cards
```python
from app.components.shared.ui.card import Card, StatsCard, CardHeader, CardBody

# Basic card
Card(
    rx.text("Card content goes here"),
    variant="default",
    padding="lg",
    hoverable=True,
    elevated=True
)

# Stats card with trend
StatsCard(
    title="Total Users",
    value="1,234",
    trend="up", 
    trend_value="+12.5%",
    icon="users",
    subtitle="Active this month"
)

# Structured card
Card(
    CardHeader(
        title="Card Title",
        subtitle="Card description",
        actions=[Button("Action", size="sm")]
    ),
    CardBody(
        rx.text("Main card content here")
    ),
    variant="outline"
)
```

### Layout Helpers
```python
from app.utils.styles import get_flex_styles, get_grid_styles

# Flex layouts
rx.box(
    children=[...],
    **get_flex_styles(
        direction="row", 
        align="center", 
        justify="space-between",
        gap="md"
    )
)

# Grid layouts  
rx.box(
    children=[...],
    **get_grid_styles(
        columns="repeat(3, 1fr)",
        gap="lg",
        align_items="stretch"
    )
)

# Responsive container
rx.box(
    children=[...],
    **get_container_styles(max_width="1200px")
)
```

## 🎛️ **Advanced Usage**

### Custom Styling with Design System
```python
from app.utils.styles import colors, spacing, with_hover_effect, with_focus_ring

# Create custom component with design system values
def custom_card():
    base_styles = {
        "background": colors["surface"],
        "border": f"1px solid {colors['border']}",
        "border_radius": "12px",
        "padding": spacing["lg"]
    }
    
    # Add hover effects using utility
    styles_with_hover = with_hover_effect(base_styles)
    
    return rx.box(
        "Custom card content",
        style=styles_with_hover
    )
```

### Component-Specific Styles
```python
from app.utils.styles.components import get_input_styles, get_modal_styles

# Use pre-defined component styles
rx.input(
    placeholder="Enter text...",
    style=get_input_styles(size="lg", variant="filled", error=False)
)

# Modal with consistent styling
rx.box(
    "Modal content",
    style=get_modal_styles(size="md")
)
```

### Theming Your App
```python
from app.utils.styles import get_base_app_styles

# Apply base theme to your app root
def app():
    return rx.box(
        # Your app content
        style=get_base_app_styles()
    )
```

## 🚀 **Migration from Old Styles**

### Before (hardcoded styles):
```python
rx.box(
    "Content",
    background="#1A1A1A",
    border="1px solid #374151", 
    border_radius="12px",
    padding="24px",
    color="white"
)
```

### After (design system):
```python
from app.utils.styles import colors, spacing, components

rx.box(
    "Content",
    background=colors["surface"],
    border=f"1px solid {colors['border']}",
    border_radius=components["radius"]["lg"],
    padding=spacing["lg"],
    color=colors["text_primary"]
)
```

### Or even better, use components:
```python
from app.components.shared.ui.card import Card

Card("Content", padding="lg", variant="default")
```

## 📋 **Best Practices**

1. **Always use design tokens** instead of hardcoded values
2. **Prefer pre-built components** over custom styling
3. **Use layout helpers** for consistent spacing and alignment
4. **Leverage semantic color names** instead of specific color codes
5. **Compose components** rather than building everything from scratch

## 🔧 **Customization**

You can always extend or override styles when needed:

```python
from app.utils.styles import get_button_styles

# Get base button styles and customize
custom_styles = get_button_styles(variant="primary", size="lg")
custom_styles.update({
    "border_radius": "20px",  # Custom border radius
    "font_weight": "800"      # Extra bold
})

rx.button("Custom Button", style=custom_styles)
```

## 📁 **File Organization**

Your components should be organized like this:
```
app/
├── utils/styles/           # Design system
│   ├── tokens.py          # Color, spacing, typography tokens  
│   ├── theme.py           # Theme configuration & utilities
│   ├── components.py      # Component-specific styles
│   └── __init__.py        # Clean imports
├── components/shared/ui/   # Reusable UI components
│   ├── button.py          # Button components
│   ├── card.py            # Card components  
│   ├── input.py           # Input components
│   └── ...
└── components/            # Feature-specific components
    ├── dashboard/         # Dashboard components
    ├── clients/           # Client components  
    └── orders/            # Order components
```

This structure ensures:
- ✅ **Single source of truth** for all design decisions
- ✅ **Easy maintenance** and updates
- ✅ **Consistent experience** across the entire app
- ✅ **Developer productivity** with reusable components
- ✅ **Scalable architecture** for growing applications
