from __future__ import annotations
from typing import TYPE_CHECKING
from gamestates.template.game_state import GameState
from game.GameSession.game_session import GameSession
from renderer.BoardRenderer.board_renderer import BoardRenderer
from globals.uimanager import ui_manager
from components.UI.button import Button
from components.UI.frame import Frame
from components.UI.text_label import TextLabel
import pygame

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from pygame.event import Event

class CatanState(GameState):
    def enter(self):
        self.game_session = GameSession()
        self.board_renderer = BoardRenderer(self.game_session)

        # build selection variables
        self.building_road = False
        self.building_settlement = False
        self.building_city = False
        self.building_devcard = False

        # build UI panel
        build_ui_background = Frame(name="build_ui_background", size=(250,600), position=(0,50), fill_colour=(0,0,0), border_colour=(255,255,255), border_thickness=8, border_radius=8)
        ui_manager.add_component(build_ui_background)

        self.build_road_button = Button(name="build_road_button", position=(25, 75), size=(75, 75), colour=(255,0,0), action=self.build_road_button_function, border_radius=8, border_colour=(255,0,0), border_width=8)
        ui_manager.add_component(self.build_road_button)
        self.build_road_text = TextLabel(name="build_road_text", text="Road", position=(115, 75), font_colour=(255,255,255), font_size=20, bold=True)
        ui_manager.add_component(self.build_road_text)
        self.build_road_cost = TextLabel(name="build_road_cost", text="Cost: \n 1 wood, 1 brick", position=(115, 105), font_colour=(255,255,255), font_size=13, bold=True)
        ui_manager.add_component(self.build_road_cost)

        self.build_settlement_button = Button(name="build_settlement_button", position=(25, 215), size=(75, 75), colour=(255,0,0), action=self.build_settlement_button_function, border_radius=8, border_colour=(255,0,0), border_width=8)
        ui_manager.add_component(self.build_settlement_button)
        self.build_settlement_text = TextLabel(name="build_settlement_text", text="Settlement", position=(115, 215), font_colour=(255,255,255), font_size=20, bold=True)
        ui_manager.add_component(self.build_settlement_text)
        self.build_settlement_cost = TextLabel(name="build_settlement_cost", text="Cost: \n 1 wood, 1 brick \n 1 sheep, 1 wheat", position=(115, 245), font_colour=(255,255,255), font_size=13, bold=True)
        ui_manager.add_component(self.build_settlement_cost)

        self.build_city_button = Button(name="build_city_button", position=(25, 355), size=(75, 75), colour=(255,0,0), action=self.build_city_button_function, border_radius=8, border_colour=(255,0,0), border_width=8)
        ui_manager.add_component(self.build_city_button)
        self.build_city_text = TextLabel(name="build_city_text", text="City", position=(115, 355), font_colour=(255,255,255), font_size=20, bold=True)
        ui_manager.add_component(self.build_city_text)
        self.build_city_cost = TextLabel(name="build_city_cost", text="Cost: \n 2 wheat, 3 ore", position=(115, 385), font_colour=(255,255,255), font_size=13, bold=True)
        ui_manager.add_component(self.build_city_cost)

        self.build_devcard_button = Button(name="build_devcard_button", position=(25, 495), size=(75, 75), colour=(255,0,0), action=self.build_devcard_button_function, border_radius=8, border_colour=(255,0,0), border_width=8)
        ui_manager.add_component(self.build_devcard_button)
        self.build_devcard_text = TextLabel(name="build_devcard_text", text="Devcard", position=(115, 495), font_colour=(255,255,255), font_size=20, bold=True)
        ui_manager.add_component(self.build_devcard_text)
        self.build_devcard_cost = TextLabel(name="build_devcard_cost", text="Cost: \n 1 wool, 1 wheat \n 1 ore", position=(115, 525), font_colour=(255,255,255), font_size=13, bold=True)
        ui_manager.add_component(self.build_devcard_cost)

        # resources panel
        resource_ui_background = Frame(name="resource_ui_background", size=(425,200), position=(0,650), fill_colour=(0,0,0), border_colour=(255,255,255), border_thickness=8, border_radius=8)
        ui_manager.add_component(resource_ui_background)

        # player panel
        player_ui_background = Frame(name="player_ui_background", size=(250,700), position=(1275,50), fill_colour=(0,0,0), border_colour=(255,255,255), border_thickness=8, border_radius=8)
        ui_manager.add_component(player_ui_background)

        # end button
        self.end_button = Button(name="end_button", position=(1425, 762.5), size=(100, 100), colour=(255,0,0), action=self.end_button_function, border_radius=8, border_colour=(255,0,0), border_width=8, text="End Turn", text_colour=(255,255,255), text_size=25, bold=True)
        ui_manager.add_component(self.end_button)

        # trade button
        self.trade_button = Button(name="trade_button", position=(1300, 762.5), size=(100, 100), colour=(0,255,0), action=self.trade_button_function, border_radius=8, border_colour=(0,255,0), border_width=8, text="Trade", text_colour=(255,255,255), text_size=25, bold=True)
        ui_manager.add_component(self.trade_button)

        # use dev-card button
        self.devcard_button = Button(name="devcard_button", position=(1175, 762.5), size=(100, 100), colour=(255,165,0), action=self.devcard_button_function, border_radius=8, border_colour=(255,165,0), border_width=8, text="Devcard", text_colour=(255,255,255), text_size=25, bold=True)
        ui_manager.add_component(self.devcard_button)
        

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
        self.end_button.handle_event(event)
        self.trade_button.handle_event(event)
        self.devcard_button.handle_event(event)
        self.build_road_button.handle_event(event)
        self.build_settlement_button.handle_event(event)
        self.build_city_button.handle_event(event)
        self.build_devcard_button.handle_event(event)

    def end_button_function(self):
        print("end turn")

    def trade_button_function(self):
        print("trade")

    def devcard_button_function(self):
        print("devcard")

    def build_road_button_function(self):
        # set all building variables false
        self.building_road = False
        self.building_settlement = False
        self.building_city = False
        self.building_devcard = False

        # set all button colours to red
        self.build_road_button.change_colour((255, 0, 0), (255, 0, 0))
        self.build_settlement_button.change_colour((255, 0, 0), (255, 0, 0))
        self.build_city_button.change_colour((255, 0, 0), (255, 0, 0))
        self.build_devcard_button.change_colour((255, 0, 0), (255, 0, 0))

        # set road building variable to true
        self.building_road = True

        # set road button to green
        self.build_road_button.change_colour((0, 255, 0), (0, 255, 0))
    
    def build_settlement_button_function(self):
        # set all building variables false
        self.building_road = False
        self.building_settlement = False
        self.building_city = False
        self.building_devcard = False

        # set all button colours to red
        self.build_road_button.change_colour((255, 0, 0), (255, 0, 0))
        self.build_settlement_button.change_colour((255, 0, 0), (255, 0, 0))
        self.build_city_button.change_colour((255, 0, 0), (255, 0, 0))
        self.build_devcard_button.change_colour((255, 0, 0), (255, 0, 0))

        # set settlement building variable to true
        self.building_settlement = True

        # set settlement button to green
        self.build_settlement_button.change_colour((0, 255, 0), (0, 255, 0))

    def build_city_button_function(self):
        # set all building variables false
        self.building_road = False
        self.building_settlement = False
        self.building_city = False
        self.building_devcard = False

        # set all button colours to red
        self.build_road_button.change_colour((255, 0, 0), (255, 0, 0))
        self.build_settlement_button.change_colour((255, 0, 0), (255, 0, 0))
        self.build_city_button.change_colour((255, 0, 0), (255, 0, 0))
        self.build_devcard_button.change_colour((255, 0, 0), (255, 0, 0))

        # set city building variable to true
        self.building_city = True

        # set city button to green
        self.build_city_button.change_colour((0, 255, 0), (0, 255, 0))

    def build_devcard_button_function(self):
        # set all building variables false
        self.building_road = False
        self.building_settlement = False
        self.building_city = False
        self.building_devcard = False

        # set all button colours to red
        self.build_road_button.change_colour((255, 0, 0), (255, 0, 0))
        self.build_settlement_button.change_colour((255, 0, 0), (255, 0, 0))
        self.build_city_button.change_colour((255, 0, 0), (255, 0, 0))
        self.build_devcard_button.change_colour((255, 0, 0), (255, 0, 0))

        # set devcard building variable to true
        self.building_devcard = True

        # set devcard button to green
        self.build_devcard_button.change_colour((0, 255, 0), (0, 255, 0))