#importamos la biblioteca XD
import pygame
from pygame.locals import *
import sys
import os #esto es para dirname
import math
import random




direcciones = [[0,1],[1.0],[0,-1], [-1,0], [math.sqrt(2)/2, math.sqrt(2)/2], [math.sqrt(2)/2, -math.sqrt(2)/2], [-math.sqrt(2)/2, math.sqrt(2)/2], [-math.sqrt(2)/2, -math.sqrt(2)/2]]


class NPC:
    def __init__(self, position_x, position_y):
        self.x = position_x
        self.y = position_y
        self.vx = 0
        self.vy = 0

    def movimiento(self, delta):
        self.x = self.x + self.vx*delta 
        self.y = self.y + self.vy*delta

print(random.choice(direcciones))