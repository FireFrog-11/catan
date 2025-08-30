from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from core.EventBus.event_bus import EventBus
    from game.GameSession.game_session import GameSession

class Command(ABC):
    """
    This class is just used as a structure for commands.

    All commands should inherit from this class.
    """
    @abstractmethod
    def validate(self, game_session: GameSession) -> bool:
        """
        This function validates the function.

        The command will not run if it doesn't pass the validation.
        """
        pass  # subclasses must override this

    @abstractmethod
    def execute(self, game_session: GameSession, event_bus: EventBus):
        """
        This function contains what should happen if the command passes validation.
        """
        pass  # subclasses must override this