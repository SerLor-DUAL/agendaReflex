import reflex as rx

def Spinner(size: str = "md", color: str = "#00D2FF", **props):
    """
    Modern spinner/loader component.
    """
    size_map = {"sm": 16, "md": 24, "lg": 32}
    spinner_size = size_map.get(size, 24)

    return rx.spinner(size=spinner_size, color=color, **props)
