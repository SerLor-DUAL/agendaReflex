# src/frontend/main.py

import reflex as rx                             # Imports reflex to build the frontend
from ..backend.main import app as fastapi_app   # Imports the FastAPI app from the backend  
from .pages.main_page import main_page          # Imports the main page of the frontend

# --- App Entrypoint --- #
app = rx.App(api_transformer=fastapi_app)       # Integrates FastAPI with Reflex
app.add_page(main_page, route="/")              # Add main_page
