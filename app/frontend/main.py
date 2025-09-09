# app/frontend/main.py

import reflex as rx                             # Imports reflex to build the frontend

from ..backend.main import app as fastapi_app   # Imports the FastAPI app from the backend
from .pages.main_page2 import MainPage          # Imports the main page of the frontend


# Se importan los modelos para que las migraciones los tengan en cuenta.
from ..backend.models.event.model import Event
from ..backend.models.user.model import User

# --- App Entrypoint --- #
app = rx.App(api_transformer=fastapi_app)       # Integrates FastAPI with Reflex
app.add_page(MainPage, route="/")               # Add main_page
