import pygame
import json
from typing import Dict
import os

class AssetManager:
    """
    This class is responsible for importing and storing all the assets.
    """
    def __init__(self, base_path="assets"):
        self.base_path = base_path
        self.images: Dict[str, pygame.Surface] = {}
        self.sounds: Dict[str, pygame.mixer.Sound] = {}
        self.music: Dict[str, str] = {} # only stores path to music

    def load_from_config(self, path: str):
        """
        This function loads and caches all the assets from a json config file.
        """
        with open(path, 'r') as f:
            config: Dict[str, Dict[str, str]] = json.load(f)

        for key, file in config.get("images", {}).items():
            image_path = os.path.join(self.base_path, file)
            self.images[key] = pygame.image.load(image_path).convert_alpha()

        for key, file in config.get("sounds", {}).items():
            sound_path = os.path.join(self.base_path, file)
            self.sounds[key] = pygame.mixer.Sound(sound_path)

        for key, file in config.get("music", {}).items():
            music_path = os.path.join(self.base_path, file)
            self.music[key] = music_path

    def get_image(self, key: str) -> pygame.Surface | None:
        """
        This function is used to get an image by name.
        """
        return self.images.get(key)

    def get_sound(self, key: str) -> pygame.mixer.Sound | None:
        """
        This function is used to get a sound effect by name.
        """
        return self.sounds.get(key)

    def get_music_path(self, key: str) -> str | None:
        """
        This function is used to get music by name.

        ONLY RETURNS PATH OF MUSIC.
        """
        return self.music.get(key)