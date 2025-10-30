from components.UI.template.ui_component import UIComponent
from components.UI.text_label import TextLabel
from components.UI.frame import Frame
import pygame

pygame.init()

class Button(UIComponent):
    def __init__(self, name: str, pos: tuple[float, float], size: tuple[float, float], colour: tuple[int, int, int], action, border_radius: int=0, border_colour: tuple[int, int, int]=(), border_width: int=0, text: str="", text_colour: tuple[int, int, int]=(), text_size: int=0, bold: bool=False, italic: bool=False):
        super().__init__(name)
        self.pos: tuple[float, float] = pos
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

        self.frame = Frame(self.name, self.size, self.pos, self.colour, self.border_colour, self.border_width, self.border_radius)

        self.rect: pygame.Rect = pygame.FRect(self.pos[0], self.pos[1], self.size[0], self.size[1])

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