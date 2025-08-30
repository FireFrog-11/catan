from typing import TYPE_CHECKING

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    import pygame
    from components.UI.template.ui_component import UIComponent

class UIManager:
    """
    This class handles updating and rendering all UI elements.
    """
    def __init__(self):
        self.components: list[UIComponent] = []
        
    def add_component(self, component: UIComponent):
        """
        This function adds a UI component to the list of components.
        """
        self.components.append(component)

    def remove_component(self, component: UIComponent):
        """
        This function removes a UI component to the list of components.
        """
        if component in self.components:
            self.components.remove(component)

    def enable_component(self, component: UIComponent):
        """
        This function enables a certain component.

        If a component is enabled, it will accept user input.
        """
        if hasattr(component, "enabled"):
            component.enabled = True

    def disable_component(self, component: UIComponent):
        """
        This function disables a certain component.

        If a component is disabled, it will not accept user input but will still be visible.
        """
        if hasattr(component, "enabled"):
            component.enabled = False

    def enable_all(self):
        """
        This function enables all components.
        """
        for component in self.components:
            if hasattr(component, "enabled"):
                component.enabled = True

    def disable_all(self):
        """
        This function disables all components.
        """
        for component in self.components:
            if hasattr(component, "enabled"):
                component.enabled = False

    def show_component(self, component: UIComponent):
        """
        This function shows a certain component.

        If a component is visible, it will accept user input and be visible.
        """
        if hasattr(component, "visible"):
            component.visible = True

    def hide_component(self, component: UIComponent):
        """
        This function hides a certain component.

        If a component is hidden, it will not accept user input and will not be visible.
        """
        if hasattr(component, "visible"):
            component.visible = False

    def show_all(self):
        """
        This function shows all components.
        """
        for component in self.components:
            if hasattr(component, "visible"):
                component.visible = True

    def hide_all(self):
        """
        This function hides all components.
        """
        for component in self.components:
            if hasattr(component, "visible"):
                component.visible = False

    def bring_to_front(self, component: UIComponent):
        """
        This function makes a certain component get drawn above everything else.
        """
        if component in self.components:
            self.components.remove(component)
            self.components.append(component)

    def send_to_back(self, component: UIComponent):
        """
        This function makes a certain component get drawn below everything else.
        """
        if component in self.components:
            self.components.remove(component)
            self.components.insert(0, component)

    def handle_event(self, event: pygame.event.Event):
        """
        This function sends any pygame event to all components.

        The component will automatically block out any events if it is disabled or hidden.
        """
        for component in self.components:
            if hasattr(component, "handle_event"):
                component.handle_event(event)

    def update(self, dt: float):
        """
        This function updates all components.
        """
        for component in self.components:
            if hasattr(component, "update"):
                component.update(dt)

    def render(self, surface: pygame.Surface):
        """
        This function renders all components.
        """
        for component in self.components:
            if hasattr(component, "render"):
                component.render(surface)

    def clear(self):
        """
        This function clears all components.

        This will wipe all UI from the screen.
        """
        self.components = []