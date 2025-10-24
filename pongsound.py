import pygame
import time

pygame.init()
pygame.mixer.init()

class Sound:
    def __init__(self):
        self.pong_sound = pygame.mixer.Sound('pong_.wav')
        self.sound_touch_limit = pygame.mixer.Sound('pong.wav')
    def play_ping_sound(self):
        self.pong_sound.play()
        time.sleep(0.001)
    def play_sound_touch_limit(self):
        self.sound_touch_limit.play()
        time.sleep(0.001)

if __name__ == '__main__':
    r = Sound()
    r.play_ping_sound()

