"""
Updated Dashboard using the New Centralized Design System

This demonstrates how to use the new design system components and styles
for consistent and maintainable UI development.
"""

import reflex as rx
from typing import List

# Import design system components and styles
from ...utils.styles import (
    colors, 
    spacing, 
    typography,
    get_card_styles,
    get_button_styles,
    get_text_styles
)
from ..shared import Card, CardHeader, CardBody, Button

# Mock data for demonstration
STATS = [
    {
        "title": "Total Clients", 
        "value": "127", 
        "change": "+5.3%", 
        "trend": "up", 
        "icon": "users",
        "subtitle": "12 active this week"
    },
    {
        "title": "Active Orders", 
        "value": "23", 
        "change": "+12.1%", 
        "trend": "up", 
        "icon": "shopping-cart",
        "subtitle": "5 completed today"
    },
    {
        "title": "Revenue", 
        "value": "$45,280", 
        "change": "+8.7%", 
        "trend": "up", 
        "icon": "dollar-sign",
        "subtitle": "This month"
    },
    {
        "title": "Completion Rate", 
        "value": "94.5%", 
        "change": "-2.1%", 
        "trend": "down", 
        "icon": "circle-check",
        "subtitle": "Last 30 days"
    },
]

QUICK_ACTIONS = [
    {
        "title": "New Client", 
        "icon": "user-plus", 
        "description": "Add a new client to your portfolio",
        "variant": "primary"
    },
    {
        "title": "New Order", 
        "icon": "plus-circle", 
        "description": "Create a new order for a client",
        "variant": "secondary"
    },
    {
        "title": "Generate Report", 
        "icon": "file-text", 
        "description": "Generate monthly performance report",
        "variant": "outline"
    },
    {
        "title": "Settings", 
        "icon": "settings", 
        "description": "Manage your account preferences",
        "variant": "ghost"
    },
]

RECENT_ACTIVITIES = [
    {"type": "client", "message": "New client 'Acme Corp' added", "time": "2 hours ago"},
    {"type": "order", "message": "Order #1234 completed successfully", "time": "4 hours ago"},
    {"type": "revenue", "message": "Payment of $2,500 received", "time": "6 hours ago"},
    {"type": "system", "message": "Monthly report generated", "time": "1 day ago"},
]

def dashboard_header() -> rx.Component:
    """Dashboard header with title, subtitle and action buttons."""
    return rx.box(
        **get_flex_styles(
            direction="column",
            align="flex-start",
            justify="space-between",
            gap="md"
        ),
        children=[
            # Title and subtitle
            rx.box(
                rx.heading(
                    "Dashboard",
                    size="8",
                    color=colors["text_primary"],
                    font_weight="700"
                ),
                rx.text(
                    "Welcome back! Here's what's happening with your business today.",
                    size="3",
                    color=colors["text_secondary"],
                    margin_top=spacing["xs"]
                ),
            ),
            
            # Action buttons
            rx.box(
                Button("Refresh Data", icon="refresh-cw", variant="secondary", size="sm"),
                Button("Export Report", icon="download", variant="outline", size="sm"),
                **get_flex_styles(gap="sm", align="center")
            )
        ],
        margin_bottom=spacing["xl"]
    )

def stats_section() -> rx.Component:
    """Statistics cards section using the design system."""
    return rx.box(
        # Section title
        rx.heading(
            "Overview",
            size="6",
            color=colors["text_primary"],
            font_weight="600",
            margin_bottom=spacing["lg"]
        ),
        
        # Stats grid
        rx.box(
            children=[
                StatsCard(
                    title=stat["title"],
                    value=stat["value"],
                    subtitle=stat["subtitle"],
                    trend_value=stat["change"],
                    trend=stat["trend"],
                    icon=stat["icon"],
                    variant="default",
                    elevated=True
                )
                for stat in STATS
            ],
            **get_grid_styles(
                columns="repeat(auto-fit, minmax(280px, 1fr))",
                gap="lg"
            )
        ),
        margin_bottom=spacing["xl"]
    )

def quick_actions_section() -> rx.Component:
    """Quick actions section with action cards."""
    return Card(
        CardHeader(
            title="Quick Actions",
            subtitle="Common tasks you can perform"
        ),
        CardBody(
            rx.box(
                children=[
                    Card(
                        rx.box(
                            rx.icon(action["icon"], font_size="24px", color=colors["accent"]),
                            margin_bottom=spacing["sm"]
                        ),
                        rx.heading(
                            action["title"],
                            size="4",
                            color=colors["text_primary"],
                            font_weight="600",
                            margin_bottom=spacing["xs"]
                        ),
                        rx.text(
                            action["description"],
                            size="2",
                            color=colors["text_secondary"],
                            line_height="1.4",
                            margin_bottom=spacing["md"]
                        ),
                        Button(
                            action["title"],
                            variant=action["variant"],
                            size="sm",
                            full_width=True
                        ),
                        variant="outline",
                        hoverable=True
                    )
                    for action in QUICK_ACTIONS
                ],
                **get_grid_styles(
                    columns="repeat(auto-fit, minmax(250px, 1fr))",
                    gap="md"
                )
            )
        ),
        variant="default",
        elevated=True
    )

def recent_activity_section() -> rx.Component:
    """Recent activity section with activity list."""
    
    # Activity icon mapping
    activity_icons = {
        "client": "user",
        "order": "shopping-cart",
        "revenue": "dollar-sign",
        "system": "settings"
    }
    
    return Card(
        CardHeader(
            title="Recent Activity",
            subtitle="Latest updates from your business",
            actions=[
                IconButton(
                    icon="more-horizontal",
                    variant="ghost",
                    size="sm",
                    aria_label="More options"
                )
            ]
        ),
        CardBody(
            rx.box(
                children=[
                    rx.box(
                        rx.box(
                            rx.icon(
                                activity_icons.get(activity["type"], "activity"),
                                font_size="16px",
                                color=colors["accent"]
                            ),
                            width="32px",
                            height="32px",
                            border_radius="6px",
                            background=colors["surface_elevated"],
                            display="flex",
                            align_items="center",
                            justify_content="center"
                        ),
                        rx.box(
                            rx.text(
                                activity["message"],
                                size="2",
                                color=colors["text_primary"],
                                font_weight="500"
                            ),
                            rx.text(
                                activity["time"],
                                size="1",
                                color=colors["text_muted"]
                            ),
                            flex="1"
                        ),
                        **get_flex_styles(gap="sm", align="center"),
                        padding=spacing["sm"],
                        border_radius="8px",
                        _hover={"background": colors["hover_overlay"]},
                        transition="background 0.2s ease"
                    )
                    for activity in RECENT_ACTIVITIES
                ],
                **get_flex_styles(direction="column", gap="xs")
            )
        ),
        variant="default",
        elevated=True
    )

def dashboard_content() -> rx.Component:
    """Main dashboard content layout."""
    return rx.box(
        # Header
        dashboard_header(),
        
        # Stats section
        stats_section(),
        
        # Two-column layout for actions and activity
        rx.box(
            quick_actions_section(),
            recent_activity_section(),
            **get_grid_styles(
                columns="1fr 400px",
                gap="xl"
            )
        ),
        
        **get_container_styles(),
        padding_y=spacing["xl"]
    )

def dashboard_view() -> rx.Component:
    """
    Main dashboard view component using the new design system.
    
    This demonstrates:
    - Using design system colors, spacing, and typography
    - Leveraging reusable Card and Button components  
    - Consistent layout patterns with grid and flex utilities
    - Proper component composition and organization
    """
    return dashboard_content()


# Example of how to override styles when needed
def custom_dashboard_view() -> rx.Component:
    """Example showing how to customize styles while using the design system."""
    
    # You can still override specific styles while maintaining consistency
    custom_container_styles = get_container_styles()
    custom_container_styles.update({
        "max_width": "1400px",  # Wider container for this specific dashboard
        "background": colors["surface"],  # Custom background
        "border_radius": "12px",
        "border": f"1px solid {colors['border']}"
    })
    
    return rx.box(
        dashboard_header(),
        stats_section(),
        
        rx.box(
            quick_actions_section(),
            recent_activity_section(),
            **get_grid_styles(columns="1fr 1fr", gap="xl")  # Equal columns instead
        ),
        
        style=custom_container_styles,
        padding=spacing["xl"]
    )
