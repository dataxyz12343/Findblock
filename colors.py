import pygame as pg
import random
class Therect:
    def __init__(self):
        self.rect  = pg.Rect(100, 100, 50, 50)
        self.rectx = 0
        self.recty = 0
        self.rgb   = (230,230,230)
        self.speed_move = 40



#2 random rgb 

def get_random_rgb():
    colors = [

    (255, 255, 0),
    (0, 255, 255),
    (255, 0, 255),
    (0,0,0),
    (0,0,0),
    (0,0,0),
    (0,0,0),
    (0,0,0),
    (0,0,0),
    (255, 255, 255),
    (128, 0, 128)
    ]
    return tuple(random.choice(colors))
