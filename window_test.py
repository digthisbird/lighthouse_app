import pygame
from pygame.locals import *

#initializer Pygame
pygame.init()


#set dimensions
width = 800
height = 600

SCREEN = pygame.display.set_mode((width, height))

pygame.display.set_caption("Solo RPG Tracker")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
