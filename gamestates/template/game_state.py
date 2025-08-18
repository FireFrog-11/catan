from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from pygame.event import Event
    import pygame

class GameState(ABC):
    """
    This is a template for any gamestates.
    All gamestates should inherit from this class.
    """
    @abstractmethod
    def enter(self):
        """
        Called when state becomes active.
        """
        pass
    
    @abstractmethod
    def exit(self):
        """
        Called when state is removed.
        """
        pass

    @abstractmethod
    def pause(self):
        """
        Called when another state is pushed on top.
        """
        pass

    @abstractmethod
    def resume(self):
        """
        Called when returning to this state from a paused state.
        """
        pass

    @abstractmethod
    def update(self, dt: float):
        """
        Game logic updates.
        """
        pass


    @abstractmethod
    def render(self, screen: pygame.Surface):
        """
        Draw the state.
        """
        pass

    @abstractmethod
    def handle_event(self, event: Event):
        """
        Input events.
        """
        pass
