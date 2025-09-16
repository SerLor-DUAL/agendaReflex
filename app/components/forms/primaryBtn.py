import reflex as rx

from ...utils.colorPallet.colorPallet import ColorPallet

colors = ColorPallet().colors

def PrimaryBtn(
        text: str, 
        size: str = "3",
        variant: str = "surface",
        width: str = "100%",
        style = {
            "cursor": "pointer",
            "transition": "all 0.3s ease",
            "_hover": {
                        "bg": colors["primaryHover"],
                    },
            "_active": {
                        "bg": colors["primaryActive"],
                        }
        }, 
        background_color: str = colors["primary"], 
        color: str = colors["text"],
        loading = None,
        on_submit = None,
        **kwargs # Additional keyword arguments for the button (e.g., on_click, type_    
    ) -> rx.Component:
    
    """
    PrimaryBtn: A reusable wrapper around Reflex's `rx.button` component.

    This component standardizes the styling of primary action buttons across 
    the application, using the predefined color palette.

    Features:
        - Consistent primary, hover, and active colors from `ColorPallet`.
        - Default styles for pointer cursor and smooth transitions.
        - Full support for all `rx.button` props via `**kwargs`.

    Args:
        text (str): The text label displayed on the button.
        size (str, optional): Button size (Radix scale). Defaults to "3".
        variant (str, optional): Button variant. Defaults to "surface".
        width (str, optional): Width of the button (CSS value). Defaults to "100%".
        style (dict, optional): Custom CSS style, including hover/active states.
            Defaults to a style dict with cursor, transition, hover, and active.
        background_color (str, optional): Background color. Defaults to colors["primary"].
        color (str, optional): Text color. Defaults to colors["text"].
        loading (bool, optional): Loading state indicator. If None, ignored.
        on_submit (callable, optional): Callback triggered on submit. If None, ignored.
        **kwargs: Any additional keyword arguments supported by `rx.button`
            (e.g., on_click, type_).

    Returns:
        rx.Component: A Reflex button component styled as the primary button.
    """

    button_props = dict(
        size=size,
        variant=variant,
        style=style,
        background_color=background_color,
        color=color,
        width=width,
        **kwargs
    )

    if loading is not None:
        button_props["loading"] = loading

    if on_submit is not None:
        button_props["on_submit"] = on_submit

    return rx.button(
        text,
        **button_props
    )