# app/state/app_state.py
import reflex as rx
from typing import Literal, Dict, List, Optional, Any
from datetime import datetime

ViewType = Literal["dashboard", "clients", "orders", "analytics"]

class AppState(rx.State):
    """
    Main application state for SPA navigation and data management.
    Handles view switching without page reloads.
    """
    
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    # NAVIGATION STATE                                                                                                                   #
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    
    current_view: ViewType = "dashboard"
    previous_view: ViewType = "dashboard"
    sidebar_collapsed: bool = False
    mobile_menu_open: bool = False
    
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    # CLIENT DATA STATE                                                                                                                  #
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    
    # Client data (you will populate this from your FastAPI)
    clients: List[Dict[str, Any]] = []
    selected_client: Optional[Dict[str, Any]] = None
    clients_loading: bool = False
    clients_error: str = ""
    
    # Client filters and pagination
    clients_search_query: str = ""
    clients_page: int = 1
    clients_per_page: int = 10
    clients_total: int = 0
    
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    # ORDERS DATA STATE                                                                                                                  #
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    
    # Orders data (you will populate this from your FastAPI)
    orders: List[Dict[str, Any]] = []
    selected_order: Optional[Dict[str, Any]] = None
    orders_loading: bool = False
    orders_error: str = ""
    
    # Orders filters and pagination
    orders_search_query: str = ""
    orders_page: int = 1
    orders_per_page: int = 10
    orders_total: int = 0
    orders_status_filter: str = "all"  # "all", "pending", "completed", "cancelled"
    
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    # UI STATE                                                                                                                           #
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    
    # Modal states
    client_modal_open: bool = False
    order_modal_open: bool = False
    confirm_dialog_open: bool = False
    
    # Form states
    client_form_data: Dict[str, str] = {}
    order_form_data: Dict[str, str] = {}
    
    # Notification system
    toast_message: str = ""
    toast_type: Literal["success", "error", "warning", "info"] = "info"
    toast_visible: bool = False
    
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    # COMPUTED PROPERTIES                                                                                                                #
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    
    @rx.var
    def filtered_clients(self) -> List[Dict[str, Any]]:
        """Return filtered clients based on search query."""
        if not self.clients_search_query:
            return self.clients
        
        query = self.clients_search_query.lower()
        return [
            client for client in self.clients
            if query in client.get("name", "").lower() or 
               query in client.get("email", "").lower() or
               query in client.get("phone", "").lower()
        ]
    
    @rx.var
    def filtered_orders(self) -> List[Dict[str, Any]]:
        """Return filtered orders based on search query and status."""
        filtered = self.orders
        
        # Filter by status
        if self.orders_status_filter != "all":
            filtered = [
                order for order in filtered
                if order.get("status", "").lower() == self.orders_status_filter
            ]
        
        # Filter by search query
        if self.orders_search_query:
            query = self.orders_search_query.lower()
            filtered = [
                order for order in filtered
                if query in str(order.get("id", "")).lower() or
                   query in order.get("client_name", "").lower() or
                   query in order.get("description", "").lower()
            ]
        
        return filtered
    
    @rx.var
    def clients_stats(self) -> Dict[str, int]:
        """Calculate client statistics."""
        total = len(self.clients)
        active = len([c for c in self.clients if c.get("status") == "active"])
        inactive = total - active
        
        return {
            "total": total,
            "active": active,
            "inactive": inactive
        }
    
    @rx.var
    def orders_stats(self) -> Dict[str, int]:
        """Calculate order statistics."""
        total = len(self.orders)
        pending = len([o for o in self.orders if o.get("status") == "pending"])
        completed = len([o for o in self.orders if o.get("status") == "completed"])
        cancelled = len([o for o in self.orders if o.get("status") == "cancelled"])
        
        return {
            "total": total,
            "pending": pending,
            "completed": completed,
            "cancelled": cancelled
        }
    
    @rx.var
    def page_title(self) -> str:
        """Get current page title."""
        titles = {
            "dashboard": "Dashboard",
            "clients": "Client Management",
            "orders": "Order Management",
            "analytics": "Analytics"
        }
        return titles.get(self.current_view, "Dashboard")
    
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    # NAVIGATION EVENTS                                                                                                                  #
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    
    @rx.event
    def navigate_to(self, view: ViewType):
        """Navigate to a specific view."""
        if view != self.current_view:
            self.previous_view = self.current_view
            self.current_view = view
            
            # Close mobile menu when navigating
            self.mobile_menu_open = False
            
            # Clear any error states when navigating
            self.clients_error = ""
            self.orders_error = ""
    
    @rx.event
    def toggle_sidebar(self):
        """Toggle sidebar collapsed state."""
        self.sidebar_collapsed = not self.sidebar_collapsed
    
    @rx.event
    def toggle_mobile_menu(self):
        """Toggle mobile menu."""
        self.mobile_menu_open = not self.mobile_menu_open
    
    @rx.event
    def go_back(self):
        """Navigate back to previous view."""
        current = self.current_view
        self.current_view = self.previous_view
        self.previous_view = current
    
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    # CLIENT MANAGEMENT EVENTS                                                                                                           #
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    
    @rx.event
    def set_clients_search_query(self, query: str):
        """Set client search query."""
        self.clients_search_query = query
        self.clients_page = 1  # Reset to first page when searching
    
    @rx.event
    def set_clients_page(self, page: int):
        """Set current clients page."""
        self.clients_page = max(1, page)
    
    @rx.event
    def select_client(self, client_id: str):
        """Select a client by ID."""
        client = next((c for c in self.clients if str(c.get("id")) == str(client_id)), None)
        if client:
            self.selected_client = client
    
    @rx.event
    def open_client_modal(self, client_id: str = ""):
        """Open client modal for create/edit."""
        if client_id:
            self.select_client(client_id)
            # Populate form with client data
            if self.selected_client:
                self.client_form_data = {
                    "name": self.selected_client.get("name", ""),
                    "email": self.selected_client.get("email", ""),
                    "phone": self.selected_client.get("phone", ""),
                    "address": self.selected_client.get("address", ""),
                    "company": self.selected_client.get("company", ""),
                }
        else:
            # Clear form for new client
            self.selected_client = None
            self.client_form_data = {
                "name": "",
                "email": "",
                "phone": "",
                "address": "",
                "company": "",
            }
        
        self.client_modal_open = True
    
    @rx.event
    def close_client_modal(self):
        """Close client modal."""
        self.client_modal_open = False
        self.selected_client = None
        self.client_form_data = {}
    
    @rx.event
    def update_client_form(self, field: str, value: str):
        """Update client form field."""
        self.client_form_data[field] = value
    
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    # ORDER MANAGEMENT EVENTS                                                                                                            #
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    
    @rx.event
    def set_orders_search_query(self, query: str):
        """Set order search query."""
        self.orders_search_query = query
        self.orders_page = 1  # Reset to first page when searching
    
    @rx.event
    def set_orders_status_filter(self, status: str):
        """Set order status filter."""
        self.orders_status_filter = status
        self.orders_page = 1  # Reset to first page when filtering
    
    @rx.event
    def set_orders_page(self, page: int):
        """Set current orders page."""
        self.orders_page = max(1, page)
    
    @rx.event
    def select_order(self, order_id: str):
        """Select an order by ID."""
        order = next((o for o in self.orders if str(o.get("id")) == str(order_id)), None)
        if order:
            self.selected_order = order
    
    @rx.event
    def open_order_modal(self, order_id: str = ""):
        """Open order modal for create/edit."""
        if order_id:
            self.select_order(order_id)
            # Populate form with order data
            if self.selected_order:
                self.order_form_data = {
                    "client_id": str(self.selected_order.get("client_id", "")),
                    "description": self.selected_order.get("description", ""),
                    "amount": str(self.selected_order.get("amount", "")),
                    "status": self.selected_order.get("status", "pending"),
                }
        else:
            # Clear form for new order
            self.selected_order = None
            self.order_form_data = {
                "client_id": "",
                "description": "",
                "amount": "",
                "status": "pending",
            }
        
        self.order_modal_open = True
    
    @rx.event
    def close_order_modal(self):
        """Close order modal."""
        self.order_modal_open = False
        self.selected_order = None
        self.order_form_data = {}
    
    @rx.event
    def update_order_form(self, field: str, value: str):
        """Update order form field."""
        self.order_form_data[field] = value
    
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    # NOTIFICATION SYSTEM                                                                                                                #
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    
    @rx.event
    def show_toast(self, message: str, toast_type: Literal["success", "error", "warning", "info"] = "info"):
        """Show toast notification."""
        self.toast_message = message
        self.toast_type = toast_type
        self.toast_visible = True
    
    @rx.event
    def hide_toast(self):
        """Hide toast notification."""
        self.toast_visible = False
        self.toast_message = ""
    
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    # PLACEHOLDER DATA LOADING (YOU WILL REPLACE WITH FastAPI CALLS)                                                                    #
    # ---------------------------------------------------------------------------------------------------------------------------------- #
    
    @rx.event
    def load_sample_data(self):
        """Load sample data for demonstration purposes."""
        # Sample clients data
        self.clients = [
            {
                "id": 1,
                "name": "Juan Pérez",
                "email": "juan@example.com",
                "phone": "+34 123 456 789",
                "company": "Tech Solutions S.L.",
                "address": "Calle Mayor 123, Madrid",
                "status": "active",
                "created_at": "2024-01-15T10:30:00Z"
            },
            {
                "id": 2,
                "name": "María García",
                "email": "maria@example.com",
                "phone": "+34 987 654 321",
                "company": "Innovate Corp",
                "address": "Avenida de la Paz 456, Barcelona",
                "status": "active",
                "created_at": "2024-02-10T14:20:00Z"
            },
            {
                "id": 3,
                "name": "Carlos López",
                "email": "carlos@example.com",
                "phone": "+34 555 123 789",
                "company": "Digital Works",
                "address": "Plaza España 789, Valencia",
                "status": "inactive",
                "created_at": "2024-01-28T09:15:00Z"
            }
        ]
        
        # Sample orders data
        self.orders = [
            {
                "id": 1001,
                "client_id": 1,
                "client_name": "Juan Pérez",
                "description": "Desarrollo de aplicación web",
                "amount": 5500.00,
                "status": "pending",
                "created_at": "2024-03-01T10:00:00Z",
                "due_date": "2024-03-30T10:00:00Z"
            },
            {
                "id": 1002,
                "client_id": 2,
                "client_name": "María García",
                "description": "Consultoría IT y migración de datos",
                "amount": 8200.00,
                "status": "completed",
                "created_at": "2024-02-15T14:30:00Z",
                "due_date": "2024-03-15T14:30:00Z"
            },
            {
                "id": 1003,
                "client_id": 1,
                "client_name": "Juan Pérez",
                "description": "Mantenimiento sistema legacy",
                "amount": 2100.00,
                "status": "cancelled",
                "created_at": "2024-01-20T11:45:00Z",
                "due_date": "2024-02-20T11:45:00Z"
            },
            {
                "id": 1004,
                "client_id": 3,
                "client_name": "Carlos López",
                "description": "Implementación CRM",
                "amount": 12500.00,
                "status": "pending",
                "created_at": "2024-03-05T16:20:00Z",
                "due_date": "2024-04-05T16:20:00Z"
            }
        ]
        
        self.clients_total = len(self.clients)
        self.orders_total = len(self.orders)
        
        self.show_toast("Sample data loaded successfully!", "success")
