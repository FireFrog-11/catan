from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from commands.templates.command import Command
    from core.EventBus.event_bus import EventBus

class DelayedCommand:
    """
    This class turns a command into a delayed command
    """
    def __init__(self, command: Command, delay: int):
        """
        Delay parameter should be in ms
        """
        self.command: Command = command
        self.delay: float = delay / 1000 # convert to seconds
        self.elapsed: float = 0
        self._validated: bool = False

    def validate(self, game_state: any) -> bool:
        """
        This function validates the command
        """
        if self.command.validate(game_state):
            self._validated = True
            self.elapsed = 0
            return True
        return False
    
    def is_ready(self) -> bool:
        """
        This function determines if command is ready to be called in command queue.
        """
        if self._validated and self.elapsed >= self.delay:
            return True
        return False
    
    def update(self, dt: float):
        self.elapsed += dt
        
    def execute(self, game_state: any, event_bus: EventBus):
        """
        This function executes command if validated
        """
        if self._validated:
            self.command.execute(game_state, event_bus)