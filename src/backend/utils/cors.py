# backend/utils/cors.py

import os                                               # Importing os for accessing environment variables
from urllib.parse import urlparse                       # Importing urlparse to parse URLs                       
from fastapi import FastAPI                             # Importing FastAPI
from fastapi.middleware.cors import CORSMiddleware      # Importing CORSMiddleware

# NOTE: This function is used to configure CORS (Cross-Origin Resource Sharing) for the FastAPI application.
def setup_cors(app: FastAPI):
    """ Configure CORS middleware for FastAPI app based on env vars: CORS_ORIGINS, BACKEND_PORT, FRONTEND_PORT."""
    backend_port = os.getenv("BACKEND_PORT", "8000")
    frontend_port = os.getenv("FRONTEND_PORT", "3000")

    # Get raw origins from env, split and strip
    cors_origins_raw = os.getenv("CORS_ORIGINS", "*")
    cors_bases = [o.strip().replace("http://", "").replace("https://", "") for o in cors_origins_raw.split(",") if o.strip()]

    # If wildcard, allow all origins without credentials
    if cors_bases == ["*"]:
        allow_origins = ["*"]
        allow_credentials = False
    else:
        # Build allowed origins with backend port for REST calls
        allow_origins = [f"http://{base}:{backend_port}" for base in cors_bases]
        
        # Also allow frontend origins with frontend port (for websockets etc)
        allow_origins += [f"http://{base}:{frontend_port}" for base in cors_bases if f"http://{base}:{frontend_port}" not in allow_origins]
        
        allow_credentials = True

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=allow_credentials,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
# Add a custom function to validate WebSocket origin header
def is_origin_allowed(origin: str | None) -> bool:
    """ Validates WebSocket origin header.
        Returns True if origin matches one of the allowed frontend origins (host + frontend_port) configured in environment variables."""
        
    if not origin:
        return False

    frontend_port = os.getenv("FRONTEND_PORT", "3000")
    cors_origins_raw = os.getenv("CORS_ORIGINS", "")
    cors_bases = [o.strip().replace("http://", "").replace("https://", "") for o in cors_origins_raw.split(",") if o.strip()]

    parsed = urlparse(origin)
    origin_host = parsed.hostname or ""
    origin_port = str(parsed.port or "")

    # Here we expand the filter to accept cors_bases hosts and also localhost and 127.0.0.1 directly (in case they are not in env)
    allowed_hosts = set(cors_bases) | {"localhost", "127.0.0.1"}

    if origin_host in allowed_hosts and origin_port == frontend_port:
        return True

    return False

