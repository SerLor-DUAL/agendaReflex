"""
Shared UI Components Library

This module provides a comprehensive set of reusable UI components
that follow the design system for consistent styling and behavior.
"""

# Import all UI components
from .button import Button, IconButton
from .card import Card, CardHeader, CardBody, CardFooter, StatsCard
from .input import Input, TextArea
from .alert import Alert, Toast
from .text import Text, Heading, Caption, Label
from .modal import Modal, ModalHeader, ModalBody, ModalFooter, AlertDialog
from .spinner import Spinner, LoadingOverlay
from .badge import Badge, StatusBadge, NotificationBadge

__all__ = [
    # Button components
    "Button",
    "IconButton",
    
    # Card components
    "Card",
    "CardHeader",
    "CardBody", 
    "CardFooter",
    "StatsCard",
    
    # Input components
    "Input",
    "TextArea",
    
    # Alert components
    "Alert",
    "Toast",
    
    # Text components
    "Text",
    "Heading",
    "Caption",
    "Label",
    
    # Modal components
    "Modal",
    "ModalHeader",
    "ModalBody",
    "ModalFooter",
    "AlertDialog",
    
    # Loading components
    "Spinner",
    "LoadingOverlay",
    
    # Badge components
    "Badge",
    "StatusBadge",
    "NotificationBadge",
]
