import reflex as rx

class PageState(rx.State):
    """State to track which form is currently displayed on the page."""
    
    current_form: str = ""

    @rx.event
    def show_form(self, form_name: str):
        """Muestra un formulario según su nombre."""
        self.current_form = form_name

    @rx.event
    def clear_form(self):
        """Oculta cualquier formulario."""
        self.current_form = ""
