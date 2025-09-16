import reflex as rx
from ...utils.colorPallet.colorPallet import ColorPallet

colors = ColorPallet().colors

def InputField(
    placeholder: str,
    value,
    on_change,
    type_: str = "text",
    icon: str | None = None,
    **kwargs
) -> rx.Component:
    """
    Generic input field with default styling, customizable via **kwargs.

    Args:
        placeholder (str): Placeholder text shown inside the input.
        value: Bound state value.
        on_change: State handler to update the value.
        type_ (str, optional): Input type. Defaults to "text".
        icon (str | None, optional): Lucide icon name. If None, no icon is rendered.
        **kwargs: Any extra props supported by `rx.input`.

    Returns:
        rx.Component: A styled Reflex input component.
    """

    default_style = {"cursor": "text", "transition": "all 0.2s ease"}
    default_hover = {"border_color": colors["primary"]}
    default_focus = {"border_color": colors["accent"]}

    # Children del input, construidos condicionalmente:
    input_children = []
    if icon:
        # Solo construimos el icono si hay string válido
        input_children.append(rx.input.slot(rx.icon(icon)))

    return rx.input(
        *input_children,
        placeholder=placeholder,
        value=value,
        on_change=on_change,
        type=type_,
        size="3",
        width="100%",
        background_color=colors["text"],       # blanco en tu paleta
        color=colors["background"],            # texto oscuro
        style=default_style,
        hover=default_hover,
        focus=default_focus,
        **kwargs,
    )
