import pygame

from pygame.locals import *
from sense_hat import SenseHat

pygame.init()
pygame.display.set_mode((1,1))
sense = SenseHat()
sense.clear()

running = True

while running:
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            running = False
            print("BYE")