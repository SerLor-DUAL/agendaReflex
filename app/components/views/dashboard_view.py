import reflex as rx
from ...state.app_state import AppState
from ...utils.styles.design_system import Layout, Spacing, Typography
from ...utils.styles.colorPallet import ColorPallet
from ..ui import StatsCard, DataCard, ActionButton, EmptyState

colors = ColorPallet().colors

def _dashboard_stats() -> rx.Component:
    """Dashboard statistics grid."""
    return rx.vstack(
        rx.text(
            "Overview",
            style=Typography.get_text_style("h3")
        ),
        rx.grid(
            StatsCard(
                title="Total Clients",
                value=AppState.clients_stats["total"],
                icon="users",
                color="primary",
                subtitle=f"{AppState.clients_stats['active']} active"
            ),
            StatsCard(
                title="Total Orders",
                value=AppState.orders_stats["total"],
                icon="shopping-bag", 
                color="success",
                subtitle=f"{AppState.orders_stats['pending']} pending"
            ),
            StatsCard(
                title="Completed",
                value=AppState.orders_stats["completed"],
                icon="check",
                color="success"
            ),
            StatsCard(
                title="Revenue",
                value="€12,500",
                icon="trending-up",
                color="warning",
                subtitle="This month"
            ),
            columns="4",
            spacing="6",
            width="100%"
        ),
        spacing="4",
        align="start",
        width="100%",
        style={"margin_bottom": Spacing.xxl}
    )

def _quick_actions() -> rx.Component:
    """Quick actions section."""
    actions = [
        {
            "title": "Add Client",
            "icon": "user-plus",
            "action": lambda: AppState.navigate_to("clients")
        },
        {
            "title": "Create Order", 
            "icon": "plus",
            "action": lambda: AppState.navigate_to("orders")
        },
        {
            "title": "View Analytics",
            "icon": "bar-chart-3", 
            "action": lambda: AppState.navigate_to("analytics")
        },
        {
            "title": "Load Sample Data",
            "icon": "database",
            "action": AppState.load_sample_data
        }
    ]
    
    return DataCard(
        title="Quick Actions",
        children=rx.grid(
            *[
                ActionButton(
                    text=action["title"],
                    icon=action["icon"],
                    on_click=action["action"],
                    variant="ghost",
                    style={"justify_content": "start"}
                ) for action in actions
            ],
            columns="2",
            spacing="4",
            width="100%"
        )
    )

def DashboardView() -> rx.Component:
    """Clean, simple dashboard view."""
    return rx.vstack(
        # Page header
        rx.vstack(
            rx.text(
                "Dashboard",
                style=Typography.get_text_style("h1")
            ),
            rx.text(
                "Welcome back! Here's an overview of your business.",
                style=Typography.get_text_style("body")
            ),
            ActionButton(
                text="Load Sample Data",
                icon="database",
                on_click=AppState.load_sample_data,
                variant="secondary"
            ),
            spacing="4",
            align="start",
            style={"margin_bottom": Spacing.xxl}
        ),
        
        # Statistics
        _dashboard_stats(),
        
        # Quick actions and recent activity
        rx.grid(
            _quick_actions(),
            DataCard(
                title="Recent Activity",
                children=rx.cond(
                    AppState.clients_stats["total"] > 0,
                    rx.vstack(
                        rx.text("• New client added: Sample Client"),
                        rx.text("• Order created: #1001"),
                        rx.text("• Order completed: #1000"),
                        spacing="2"
                    ),
                    EmptyState(
                        icon="activity",
                        title="No recent activity",
                        description="Activity will appear here as you use the system."
                    )
                )
            ),
            columns="2",
            spacing="8",
            width="100%"
        ),
        
        spacing="8",
        align="start",
        width="100%",
        style=Layout.get_container_style()
    )
