import pygame
import json
from typing import Dict

class AssetManager:
    def __init__(self):
        self.images: Dict[str, pygame.Surface] = {}
        self.sounds: Dict[str, pygame.mixer.Sound] = {}
        self.music: Dict[str, str] = {} # only stores path to music

    def load_from_config(self, path: str):
        """
        This function loads and caches all the assets from a json config file
        """
        with open(path, 'r') as f:
            config: Dict[str, Dict[str, str]] = json.load(f)

        for key, file in config.get("images", {}).items():
            self.images[key] = pygame.image.load(file).convert_alpha()

        for key, file in config.get("sounds", {}).items():
            self.sounds[key] = pygame.mixer.Sound(file)

        for key, file in config.get("music", {}).items():
            self.music[key] = file

    def get_image(self, key: str) -> str | None:
        """
        This function is used to get an image by name
        """
        return self.images.get(key)

    def get_sound(self, key: str) -> str | None:
        """
        This function is used to get a sound effect by name
        """
        return self.sounds.get(key)

    def get_music_path(self, key: str) -> str | None:
        """
        This function is used to get music by name
        ONLY RETURNS PATH OF MUSIC
        """
        return self.music.get(key)