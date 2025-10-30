from components.UI.template.ui_component import UIComponent
import pygame

pygame.init()

class TextLabel(UIComponent):
    def __init__(self, name, text: str, position: tuple[float, float], font_colour: tuple[int, int, int], font_size: int, bold: bool=False, italic: bool=False):
        super().__init__(name)
        self.text: str = text
        self.font_colour: tuple[int, int, int] = font_colour
        self.font_size: int = font_size
        self.bold: bool = bold
        self.italic: bool = italic

        self.font: pygame.Font = pygame.font.SysFont("Arial", self.font_size, self.bold, self.italic)
        self.text_surface: pygame.Surface = self.font.render(self.text, True, self.font_colour)

        self.rect = self.text_surface.get_frect(topleft=position)

    def set_text(self, new_text: str):
        if new_text != self.text:
            self.text = new_text
            self.text_surface = self.font.render(self.text, True, self.font_colour)
            self.rect.size = self.text_surface.get_size()

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