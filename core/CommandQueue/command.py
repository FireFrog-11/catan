from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from EventBus.event_bus import EventBus

class Command(ABC):
    """
    This class is just used as a structure for commands
    """
    @abstractmethod
    def validate(self, game_state: any) -> bool:
        pass  # subclasses must override this

    @abstractmethod
    def execute(self, game_state: any, event_bus: EventBus):
        pass  # subclasses must override this