# app/frontend/main.py

import reflex as rx                             # Imports reflex to build the frontend

from .pages.main_page import MainPage          # Imports the main page of the frontend

# Se importan los modelos para que las migraciones los tengan en cuenta.
from .db.models.event.model import Event
from .db.models.user.model import User

from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

# Import CORS middleware to handle cross-origin requests
from .api.utils.cors import setup_cors, is_origin_allowed

# Import APIs endopints
from .api.routes import events, events_admin, users_admin, auth

# Import routes (pages)
#from frontend.routes import home, login, register, diary

# Import database initializer
from .db.db_handler import close_db, init_db

# Import modules to load and access environment variables
from dotenv import load_dotenv                                
import os                                                     

# Load environment variables from .env file
load_dotenv()

# ============================================================================================================================= #
#                                                Database initialization                                                        #
# ============================================================================================================================= #

# Inicialize database when FastAPI instance starts
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Before starting the app (startup)
    try:
        await init_db()  # Initialize the database connection or any other resources
        print("Database initialized")
    except Exception as e:
        print(f"Error initializing DB: {e}")
        # Here you could decide to stop the app or continue as needed
    yield
    # When the app stops (shutdown)
    try:
        await close_db()  # Release resources, DB connections, etc. (if you have any)
        print("Database connection closed")
    except Exception as e:
        print(f"Error closing DB: {e}")


# ============================================================================================================================= #
#                                              FastAPI initial integration                                                      #
# ============================================================================================================================= #

# Create FastAPI instance
app_fastapi = FastAPI(title="Integra", lifespan=lifespan)

# Injects CORS middleware into the FastApi instance
setup_cors(app_fastapi)

# This is a WebSocket endpoint for handling real-time events
@app_fastapi.websocket("/api/_event/")
async def websocket_endpoint(websocket: WebSocket):
    
    # Get the 'origin' header from the incoming WebSocket connection request
    origin = websocket.headers.get("origin")
    print(f"WebSocket connection origin: {origin}")

    # Check if the origin is allowed (valid and whitelisted)
    if not is_origin_allowed(origin):
        # If origin is not allowed, close the connection with 403 Forbidden
        print(f"Origin not allowed: {origin}")
        await websocket.close(code=403)
        return

    # Accept the WebSocket connection (handshake success)
    await websocket.accept()

    try:
        # Keep the connection open to receive and send messages
        while True:
            # Wait to receive a text message from the client
            data = await websocket.receive_text()

            # Echo the received message back to the client with a prefix
            await websocket.send_text(f"Received: {data}")

    # Handle client disconnect event gracefully
    except WebSocketDisconnect:
        pass

# Include all the needed routes to FastAPI
app_fastapi.include_router(users_admin.user_admin_router)       # Administration of users API
app_fastapi.include_router(auth.auth_router)                    # Authentication API
app_fastapi.include_router(events.event_router)                 # Events API
app_fastapi.include_router(events_admin.event_admin_router)     # Administration of events API

# ============================================================================================================================= #
#                                                Routes configuration                                                           #
# ============================================================================================================================= #

@app_fastapi.get("/")
async def root():
    return {"message": "FastAPI corriendo"}


# --- Reflex Entrypoint --- #
app = rx.App(api_transformer=app_fastapi)       # Integrates FastAPI with Reflex
app.add_page(MainPage, route="/")               # Add main_page
