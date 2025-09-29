import reflex as rx
from ...state.app_state import AppState
from ...utils.styles.design_system import Layout, ComponentStyles, ColorSystem, Spacing, Typography
from ...utils.styles.colorPallet import ColorPallet

from ..navigation.sidebar import Sidebar
from ..views.dashboard_view import DashboardView
from ..views.clients_view import ClientsView
from ..views.orders_view import OrdersView

colors = ColorPallet().colors

def _analytics_placeholder() -> rx.Component:
    """Placeholder for analytics view."""
    return rx.center(
        rx.vstack(
            rx.icon("bar-chart-3", size=64, color=colors["textMuted"]),
            rx.text(
                "Analytics Coming Soon",
                style=Typography.get_text_style("h2")
            ),
            rx.text(
                "This section will contain detailed analytics and reporting.",
                style=Typography.get_text_style("body")
            ),
            spacing="6",
            align="center"
        ),
        style={
            "min_height": "60vh",
            "width": "100%"
        }
    )

def _toast_notification() -> rx.Component:
    """Simplified toast notification."""
    return rx.cond(
        AppState.toast_visible,
        rx.box(
            rx.hstack(
                rx.icon("info", size=18, color=colors["primary"]),
                rx.text(
                    AppState.toast_message,
                    style=Typography.get_text_style("body")
                ),
                rx.icon(
                    "x", 
                    size=16, 
                    on_click=AppState.hide_toast,
                    style={"cursor": "pointer"}
                ),
                justify="between",
                align="center",
                width="100%"
            ),
            style={
                **ComponentStyles.get_card_style(),
                "position": "fixed",
                "top": Spacing.lg,
                "right": Spacing.lg,
                "z_index": "1000",
                "max_width": "400px"
            }
        )
    )

def _main_content() -> rx.Component:
    """Main content area with view switching."""
    return rx.box(
        rx.cond(
            AppState.current_view == "dashboard",
            DashboardView(),
            rx.cond(
                AppState.current_view == "clients", 
                ClientsView(),
                rx.cond(
                    AppState.current_view == "orders",
                    OrdersView(),
                    _analytics_placeholder()
                )
            )
        ),
        style={
            **Layout.get_page_style(),
            "flex": "1",
            "width": "100%"
        }
    )

def SPALayout() -> rx.Component:
    """
    Simplified SPA layout with clean responsive design.
    
    Features:
    - Simple sidebar + content layout
    - Responsive mobile menu
    - Toast notifications
    - Clean z-index management
    """
    return rx.box(
        # Main desktop layout
        rx.desktop_only(
            rx.hstack(
                # Sidebar
                rx.box(
                    Sidebar(),
                    style={
                        "width": rx.cond(AppState.sidebar_collapsed, "80px", "280px"),
                        "transition": "width 0.3s ease",
                        "background": colors["cards"],
                        "border_right": f"1px solid {colors['border']}",
                        "height": "100vh",
                        "position": "fixed",
                        "left": "0",
                        "top": "0",
                        "z_index": "100"
                    }
                ),
                # Content area
                rx.box(
                    _main_content(),
                    style={
                        "flex": "1",
                        "margin_left": rx.cond(AppState.sidebar_collapsed, "80px", "280px"),
                        "transition": "margin-left 0.3s ease",
                        "min_height": "100vh"
                    }
                ),
                spacing="0",
                align="start",
                width="100%"
            )
        ),
        
        # Mobile layout
        rx.mobile_and_tablet(
            rx.vstack(
                # Mobile header
                rx.box(
                    rx.hstack(
                        rx.icon(
                            "menu", 
                            size=24, 
                            on_click=AppState.toggle_mobile_menu,
                            style={"cursor": "pointer"}
                        ),
                        rx.text(
                            AppState.page_title,
                            style=Typography.get_text_style("h3")
                        ),
                        rx.spacer(),
                        rx.icon("user", size=20),
                        justify="between",
                        align="center",
                        width="100%"
                    ),
                    style={
                        **ComponentStyles.get_card_style(),
                        "position": "fixed",
                        "top": "0",
                        "left": "0",
                        "right": "0",
                        "z_index": "200",
                        "border_radius": "0 0 12px 12px"
                    }
                ),
                # Content with top margin for header
                rx.box(
                    _main_content(),
                    style={
                        "margin_top": "80px",
                        "width": "100%"
                    }
                ),
                spacing="0",
                width="100%"
            )
        ),
        
        # Mobile sidebar overlay
        rx.mobile_and_tablet(
            rx.cond(
                AppState.mobile_menu_open,
                rx.vstack(
                    # Overlay background
                    rx.box(
                        on_click=AppState.toggle_mobile_menu,
                        style={
                            "position": "fixed",
                            "top": "0",
                            "left": "0",
                            "width": "100vw",
                            "height": "100vh",
                            "background": "rgba(0,0,0,0.5)",
                            "z_index": "300"
                        }
                    ),
                    # Sidebar
                    rx.box(
                        Sidebar(),
                        style={
                            "position": "fixed",
                            "top": "0",
                            "left": "0",
                            "width": "280px",
                            "height": "100vh",
                            "z_index": "400",
                            "background": colors["cards"]
                        }
                    ),
                    spacing="0"
                )
            )
        ),
        
        # Toast notifications
        _toast_notification(),
        
        style={
            "background": colors["generalBackground"],
            "min_height": "100vh",
            "width": "100%",
            "position": "relative"
        }
    )
