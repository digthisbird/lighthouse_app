import pygame
import sys
import random
import os
from pygame.locals import *

#initializer Pygame
pygame.init()

# Predefined colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BEIGE = (166, 147, 126)

#set dimensions
width = 1000
height = 800

#set up display
SCREEN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Solo RPG Tracker")
# set icon
icon = pygame.image.load(os.path.join("Lighthouse.png"))
pygame.display.set_icon(icon)

#set bg image
bg = pygame.image.load(os.path.join("map_bg.jpg"))

#scale bg
bg = pygame.transform.scale(bg, (width, height))

#button settings
button_color = BEIGE
button_hover_color = WHITE
button_width = 100
button_height = 50
button_x = (width-button_width) // 2
button_y = (height - button_height) //2

#create button rectangle
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

#set font
font = pygame.font.SysFont("zapfino", 36)

#funtoin to display button text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x,y))
    surface.blit(text_obj, text_rect)

running = True
while running:
    # Blit the background to the screen
    SCREEN.blit(bg, (0,0))

    # get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # check if the mouse is over the button
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(SCREEN, button_hover_color, button_rect) # changes color
    else:
        pygame.draw.rect(SCREEN, button_color, button_rect)

    #Display button text
    draw_text("Roll A Die To Begin", font, BLACK, SCREEN, button_x + button_width // 2, button_y + button_height // 2)

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #check if the mouse button is pressed inside the button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(mouse_pos):
                print ("Yay!")

    pygame.display.flip()

pygame.quit()
