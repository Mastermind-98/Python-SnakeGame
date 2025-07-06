import pygame
import os

class Sound:
    def __init__(self):
        pygame.mixer.init()
        base_path = os.path.dirname(__file__)
        sound_path = lambda name: os.path.join(base_path, "sounds", name)
        self.sound_effects = {
            'consumption': pygame.mixer.Sound(os.path.join(base_path,'sounds/consumption.mp3')),
            'game_over': pygame.mixer.Sound(os.path.join(base_path,'sounds/gameOver.mp3')),
            'speedIncrease': pygame.mixer.Sound(os.path.join(base_path,'sounds/speedIncrease.mp3')),
            'ultraconsumption': pygame.mixer.Sound(os.path.join(base_path,'sounds/ultraconsumption.mp3')),
        }
        self.background_music = pygame.mixer.Sound('sounds/backgroundMusic.mp3')
        self.background_music.set_volume(0.5)
        self.background_music.play(-1)  

    def play_sound(self, sound_name):
        if sound_name in self.sound_effects:
            self.sound_effects[sound_name].play()

    def stop_background_music(self):
        self.background_music.stop()