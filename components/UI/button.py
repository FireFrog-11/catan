from components.UI.template.ui_component import UIComponent
from components.UI.text_label import TextLabel
from components.UI.frame import Frame
from globals.scale_factor import get_scale_factors
import pygame

pygame.init()

class Button(UIComponent):
    def __init__(self, name: str, position: tuple[float, float], size: tuple[float, float], colour: tuple[int, int, int], action, border_radius: int=0, border_colour: tuple[int, int, int]=(), border_width: int=0, text: str="", text_colour: tuple[int, int, int]=(), text_size: int=0, bold: bool=False, italic: bool=False):
        super().__init__(name)
        self.position: tuple[float, float] = position
        self.size: tuple[float, float] = size
        self.action = action
        self.colour: tuple[int, int, int] = colour
        self.border_radius: int = border_radius
        self.border_colour: tuple[int, int, int] = border_colour
        self.border_width: int = border_width
        self.text: str = text
        self.text_colour: tuple[int, int, int] = text_colour
        self.text_size: int = text_size
        self.bold: bool = bold
        self.italic: bool = italic

        self.frame = Frame(self.name, self.size, self.position, self.colour, self.border_colour, self.border_width, self.border_radius)

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

        self.rect: pygame.Rect = pygame.FRect(self.scaled_position[0], self.scaled_position[1], self.scaled_size[0], self.scaled_size[1])

        # below is the code to format the text label into the center of the frame
        if self.text != "":
            self.text_label = TextLabel(self.name, self.text, (0, 0), self.text_colour, self.text_size, self.bold, self.italic)
            frame_centerx, frame_centery = self.rect.center
            x,y = self.text_label.rect.size
            text_label_pos = (frame_centerx - x/2, frame_centery - y/2)

            self.text_label.change_pos(text_label_pos)

    def render(self, surface: pygame.Surface):
        if not super().render(surface):
            return
        
        self.frame.render(surface)
        if self.text != "":
            self.text_label.render(surface)

    def update(self, dt):
        pass

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(mouse_pos):
                self.action()

    def change_colour(self, new_colour: tuple[int, int, int], new_border_colour: tuple[int, int, int]):
        self.colour = new_colour
        self.border_colour = new_border_colour

        self.frame.fill_colour = new_colour
        self.frame.border_colour = new_border_colour