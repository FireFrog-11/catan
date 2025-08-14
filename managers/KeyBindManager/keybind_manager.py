from __future__ import annotations
from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from CommandQueue.command import Command

class KeybindManager:
    """
    This class handles binding and unbinding keys to different actions
    """
    def __init__(self):
        self._bindings: dict[int, Callable[[], Command]] = {}  # Maps key -> command factory

    def bind_key(self, key: int, command_factory: Callable[[], Command]):
        """
        This function binds key to action
        """
        self._bindings[key] = command_factory

    def unbind_key(self, key: int):
        """
        This function unbinds key from action
        """
        if key in self._bindings:
            del self._bindings[key]

    def get_action(self, key: int) -> Command | None:
        """
        This function returns the action mapped to a key
        """
        factory = self._bindings.get(key)

        if factory:
            return factory()
        return None