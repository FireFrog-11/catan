from components.UI.template.ui_component import UIComponent
import pygame
from globals.scale_factor import get_scale_factors

pygame.init()

class TextLabel(UIComponent):
    def __init__(self, name, text: str, position: tuple[float, float], font_colour: tuple[int, int, int], font_size: int, bold: bool=False, italic: bool=False):
        # scale factors
        scale_factor_x, scale_factor_y = get_scale_factors(pygame.display.get_surface())
        
        super().__init__(name)
        self.text: str = text
        self.font_colour: tuple[int, int, int] = font_colour
        self.font_size: int = int(font_size * min(scale_factor_x, scale_factor_y)) # multiplies by whichever factor is smaller
        self.bold: bool = bold
        self.italic: bool = italic

        self.font: pygame.Font = pygame.font.SysFont("Arial", self.font_size, self.bold, self.italic)
        self.text_surface: pygame.Surface = self.font.render(self.text, True, self.font_colour)

        # get scaled position
        x, y = position
        scaled_x = x * scale_factor_x
        scaled_y = y * scale_factor_y
        self.scaled_position = (scaled_x, scaled_y)

        self.rect = self.text_surface.get_frect(topleft=self.scaled_position)

    def set_text(self, new_text: str):
        if new_text != self.text:
            self.text = new_text
            self.text_surface = self.font.render(self.text, True, self.font_colour)
            self.rect.size = self.text_surface.get_size()

    def change_colour(self, new_colour):
        self.font_colour = new_colour
        self.text_surface = self.font.render(self.text, True, self.font_colour)

    def change_pos(self, new_pos: tuple[int, float]):
        if new_pos != self.rect.topleft:
            self.rect.topleft = (new_pos[0], new_pos[1])

    def render(self, surface: pygame.Surface):
        if not super().render(surface):
            return

        surface.blit(self.text_surface, self.rect)

    def update(self, dt):
        pass

    def handle_event(self, event):
        pass