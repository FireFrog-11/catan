from components.UI.template.ui_component import UIComponent
from globals.scale_factor import get_scale_factors
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

        # scale factors
        scale_factor_x, scale_factor_y = get_scale_factors(pygame.display.get_surface())

        # get scaled position
        x, y = self.position
        scaled_x = x * scale_factor_x
        scaled_y = y * scale_factor_y
        self.scaled_position = (scaled_x, scaled_y)

        # get scaled size
        x, y = self.size
        scaled_x = x * scale_factor_x
        scaled_y = y * scale_factor_y
        self.scaled_size = (scaled_x, scaled_y)

        self.rect = pygame.FRect((self.scaled_position, self.scaled_size))

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