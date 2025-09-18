from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from gamestates.template.game_state import GameState
    from pygame.event import Event
    import pygame

class GameStateManager:
    """
    This class is responsible for handling all the gamestates.
    """
    def __init__(self):
        self.state_stack: list[GameState] = []

    def push_state(self, state: GameState):
        """
        This function adds a new state to the stack.
        """
        if self.state_stack:
            self.state_stack[-1].pause()
        self.state_stack.append(state)
        state.enter()

    def pop_state(self):
        """
        This function removes a state from the stack.
        """
        if self.state_stack:
            self.state_stack[-1].exit()
            self.state_stack.pop()
        if self.state_stack:
            self.state_stack[-1].resume()

    def change_state(self, state: GameState):
        """
        This function changes the current state to a new state.
        """
        if self.state_stack:
            self.state_stack[-1].exit()
            self.state_stack.pop()
        self.state_stack.append(state)
        state.enter()

    def update(self, dt):
        """
        This function updates the current state.
        """
        if self.state_stack:
            self.state_stack[-1].update(dt)

    def render(self, screen: pygame.Surface):
        """
        This function renders all the states in the stack.
        """
        for state in self.state_stack:
            state.render(screen)

    def handle_event(self, event: Event):
        """
        This function handles the events of the current state.
        """
        if self.state_stack:
            self.state_stack[-1].handle_event(event)