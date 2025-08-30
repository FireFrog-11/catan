from typing import TYPE_CHECKING
import pygame

if TYPE_CHECKING: # only for types. NOT IMPORTANT
    from managers.AssetManager.asset_manager import AssetManager

class AudioManager:
    """
    This class is responsible for handling all the music and other audio.
    """
    def __init__(self, asset_manager: AssetManager):
        pygame.mixer.init()
        self.asset_manager = asset_manager
        self.music_playing = False

    def play_sound(self, key: str):
        """
        This function plays a sound effect of the given key.

        The key must be a valid sound key in the asset manager.
        """
        sound = self.asset_manager.get_sound(key)
        sound.play()

    def stop_sound(self, key: str):
        """
        This function stops a sound effect of the given key.

        The key must be a valid sound key in the asset manager.
        """
        sound = self.asset_manager.get_sound(key)
        sound.stop()

    def play_music(self, key: str, loops: int=-1):
        """
        This function plays a music effect of the given key.

        The key must be a valid music key in the asset manager.
        """
        music_path = self.asset_manager.get_music_path(key)
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(loops=loops)

    def stop_music(self):
        """
        This function stops any music currently playing.
        """
        pygame.mixer.music.stop()

    def pause_music(self):
        """
        This function pauses any music currently playing.
        """
        pygame.mixer.music.pause()

    def resume_music(self):
        """
        This function resumes any music that was playing
        """
        pygame.mixer.music.unpause()

    def set_volume(self, volume: float):
        """
        This function changes the volume of the audio.

        The volume must be between 0 and 1.
        """
        pygame.mixer.music.set_volume(volume)