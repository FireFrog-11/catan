from __future__ import annotations
from commands.templates.command import Command
from typing import TYPE_CHECKING

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from core.EventBus.event_bus import EventBus
    from game.GameSession.game_session import GameSession

class BuildRoadCommand(Command):
    def validate(self, game_session: GameSession):
        # check if player has enough resources
        current_player = game_session.player_turn
        resource_cards = game_session.players[current_player-1].resource_cards # gets player from list of players (needs to minus 1 for index)

        # gets required resources
        wood_amount = resource_cards.get("wood")
        brick_amount = resource_cards.get("brick")

        if wood_amount >= 1 and brick_amount >= 1:
            return True
        return False

    def execute(self, game_session: GameSession, event_bus: EventBus):
        pass