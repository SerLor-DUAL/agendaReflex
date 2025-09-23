from .alert import Alert
from typing import Literal

AlertVariant = Literal["info", "success", "warning", "error"]

def Toast(message: str, variant: AlertVariant = "info", duration: int = 3000, **props):
    """
    Toast notification component that reuses Alert.
    """
    return Alert(
        children=message,
        variant=variant,
        dismissible=True,
        style={
            "position": "fixed",
            "top": "20px",
            "right": "20px",
            "max_width": "400px",
            "z_index": "1000",
        },
        **props
    )
