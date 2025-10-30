import pygame
from abc import ABC, abstractmethod

class UIComponent(ABC):
    """
    This class is a template for a UI component.

    All UI Components must inherit from this class.
    """
    @abstractmethod
    def __init__(self, name: str=None, visible: bool=True, enabled: bool=True):
        self.name = name
        self.visible = visible
        self.enabled = enabled
        self.rect: pygame.Rect = pygame.FRect(0, 0, 0, 0,) # Override in subclasses

    def set_position(self, x: float, y: float):
        """
        Sets the position of the UI component.
        """
        self.rect.topleft = (x, y)

    def move(self, dx: float, dy: float):
        """
        Moves the UI component relative to its current position.
        """
        self.rect.move_ip(dx, dy)

    @abstractmethod
    def handle_event(self, event: pygame.event.Event):
        """
        Handles pygame events.
        """
        if not self.visible or not self.enabled:
            return False
        return True
    
    @abstractmethod
    def update(self, dt: float):
        """
        Updates the UI component.
        """
        pass
    
    @abstractmethod
    def render(self, surface: pygame.Surface):
        """
        Renders the UI component.
        """
        if not self.visible:
            return False
        return True