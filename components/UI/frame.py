from components.UI.template.ui_component import UIComponent
import pygame

pygame.init()

class Frame(UIComponent):
    def __init__(self, name, size: tuple[float, float], position: tuple[float, float], fill_colour: tuple[int, int, int], border_colour: tuple[int, int, int], border_thickness: int, border_radius: int=0):
        super().__init__(name)
        self.size: tuple[float, float] = size
        self.position: tuple[float, float] = position
        self.fill_colour: tuple[int, int, int] = fill_colour
        self.border_colour: tuple[int, int, int] = border_colour
        self.border_thickness: int = border_thickness
        self.border_radius: int = border_radius

        self.rect = pygame.FRect((self.position, self.size))

    def render(self, surface: pygame.Surface):
        if not super().render(surface):
            return

        pygame.draw.rect(surface, self.fill_colour, self.rect, border_radius=self.border_radius)

        if self.border_thickness > 0:
            pygame.draw.rect(surface, self.border_colour, self.rect, self.border_thickness, self.border_radius)

    def update(self, dt):
        pass

    def handle_event(self, event):
        pass