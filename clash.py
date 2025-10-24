import pygame
pygame.init()
import time 
class Clash:
    def __init__ (self):
        self.clash_image1  = pygame.image.load('clash.png')
        self.clash_image2  = pygame.transform.scale(self.clash_image1,(100,100))
        self.clash_xy = self.clash_image2.get_rect()
        self.clsh   = 10
    def show_clash(self,screen,pos):
        screen.blit(self.clash_image2,pos)

