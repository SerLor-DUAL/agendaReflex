"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


# app/backend/models/user/model.py

# Import necessary modules
from sqlmodel import SQLModel, Field, Column, Integer, String, TIMESTAMP         # Importing SQLModel for database operations
from datetime import datetime                                                    # Importing for timestamps management
from typing import Optional                                                      # Importing Optional for type hints
# PROVISORIO
import os
from dotenv import load_dotenv

from .pages.main_page import main_page

load_dotenv()           
# FIN PROVISORIO                 

# Importing users table settings

# ---------------------------------------------------------------------------------------------------------------------------------------------------- #
app = rx.App()
app.add_page(main_page)
