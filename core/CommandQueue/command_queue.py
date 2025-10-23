from typing import TYPE_CHECKING

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from commands.templates.command import Command
    from commands.templates.delayed_command import DelayedCommand

class CommandQueue:
    """
    This class is a simple command queue which executes commands if they pass validation.

    It contains functionality for delayed commands (useful for animations).
    """
    def __init__(self):
        self._queue: list[Command | DelayedCommand] = []

    def add(self, command: Command | DelayedCommand, game_state: any):
        """
        This function adds command to command queue if it passes validation.
        """
        if command.validate(game_state):
            self._queue.append(command)
        else:
            print("Command failed validation")

    def process_commands(self, game_state: any, dt: float):
        """
        This function will process all current commands.
        """
        ready: list[Command] = []
        for command in self._queue:
            if not hasattr(command, "is_ready") or command.is_ready():
                ready.append(command)
            
            if hasattr(command, "is_ready") and not command.is_ready():
                command.update(dt)
        
        for command in ready:
            self._queue.remove(command)
            command.execute(game_state)