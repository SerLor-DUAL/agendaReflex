# agendaReflex/rxconfig.py

import reflex as rx                         
import os                                   

# -------- URL AND PORT CONFIG --------#

# Get the base URL from environment (e.g., "http://localhost:" or "https://myapp.com:")
# This makes the app adaptable to different environments (local, staging, production)
base_url = os.getenv("BASE_URL", "http://localhost:")

backend_port = int(os.getenv("BACKEND_PORT", 8000))     # Backend port (default: 8000 if not set in environment)
frontend_port = int(os.getenv("FRONTEND_PORT", 3000))   # Frontend port (default: 3000 if not set in environment)

# These full url are later used for CORS and deployment config
back_url = f"{base_url}{backend_port}"
front_url = f"{base_url}{frontend_port}"

# -------- REFLEX MAIN CONFIG -------- #

config = rx.Config(
    # Name of your Reflex app (can be anything)
    app_name="agendaReflex",                

    # Path to the module where your Reflex app is defined
    # Reflex will import this and look for the rx.App() instance
    app_module_import="app.frontend.main",

    # Optional but useful plugins:
    plugins=[
        rx.plugins.SitemapPlugin(),         # Automatically generates sitemap.xml (great for SEO)
        rx.plugins.TailwindV4Plugin(),      # Enables Tailwind CSS v4 support
    ],

    # Allowed origins for CORS (Cross-Origin Resource Sharing)
    # NOTE: This CORS config is different from the backend FastAPI CORS 
    # 
    # WHY YOU NEED THIS EVEN USING FASTAPI CORS:
    # ============================================
    #
    # When Reflex starts, it creates TWO independent servers:
    #
    # 1) HTTP Server (the FastAPI app):
    #    ├── Handles: /api/*, static files, page routes
    #    ├── CORS: The FastAPI CORSMiddleware in the backend applies to this server
    #    └── Protocol: HTTP/HTTPS
    #
    # 2) WebSocket Server (the Socket.IO server):
    #    ├── Handles: /socket.io/*, real-time state updates
    #    ├── CORS: The config below is the one that applies to the WebSocket server!
    #    └── Protocol: WebSocket handshake + WebSocket
    
    cors_allowed_origins=[
        back_url,   
        front_url    
    ],

    # Ports used when running the dev server
    backend_port=backend_port,
    frontend_port=frontend_port,

    # NOTE: Optional parameters for deployment and production settings
    # back_url=back_url,                   # Public or internal backend API URL (useful in prod)
    # deploy_url=front_url,                # Final deployed frontend URL (used for redirects, links, etc.)
)
