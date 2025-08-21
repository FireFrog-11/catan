from __future__ import annotations
import pygame
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

class UIComponent(ABC):
    @abstractmethod
    def __init__(self, name: str=None, visible: bool=True, enabled: bool=True):
        self.name = name
        self.visible = visible
        self.enabled = enabled
        self.rect = pygame.FRect(0, 0, 0, 0,) # Override in subclasses

    @abstractmethod
    def set_position(self, x: float, y: float):
        self.rect.topleft = (x, y)

    @abstractmethod
    def move(self, dx: float, dy: float):
        self.rect.move_ip(dx, dy)

    @abstractmethod
    def handle_event(self, event: pygame.event.Event):
        if not self.visible or not self.enabled:
            return
    
    @abstractmethod
    def update(self, dt: float):
        pass
    
    @abstractmethod
    def render(self, surface: pygame.Surface):
        if not self.visible:
            return