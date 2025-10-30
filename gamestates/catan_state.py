from __future__ import annotations
from typing import TYPE_CHECKING
from gamestates.template.game_state import GameState
from game.GameSession.game_session import GameSession
from renderer.BoardRenderer.board_renderer import BoardRenderer
from globals.uimanager import ui_manager
from components.UI.button import Button
import pygame

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from pygame.event import Event

class CatanState(GameState):
    def enter(self):
        self.game_session = GameSession()
        self.board_renderer = BoardRenderer(self.game_session)

        button = Button("test_button", (200, 200), (100, 100), (255, 0, 0), self.rand_function, 5, (255, 255, 255), 3, "test", (255, 255, 255), text_size=30, bold=True)

        ui_manager.add_component(button)

    def exit(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def update(self, dt: float):
        pass

    def render(self, screen: pygame.Surface):
        self.board_renderer.render_board(screen)
        ui_manager.render(screen)

    def handle_event(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("yes")

    def rand_function():
        pass