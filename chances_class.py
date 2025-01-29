import pygame
import random
import os

class Chances:
    def __init__(self, screen, width, height):
         self.screen = screen
         self.width = width
         self.height = height

         #Set Colors
         WHITE = (255, 255, 255)
         BLACK = (0, 0, 0)
         RED = (224, 67, 56)
         GREEN = (65, 173, 55)
         YELLOW = (242, 205, 41)
         BLUE = (59, 114, 196)

         #Font Settings
         self.font = pygame.font.SysFont(zapfino, 14)

        # set initial number of dice to 100
         self.total_jenga_dice = 100

    def draw_text(self, text, x, y):
        text_obj = self.font.render(text, True, (255, 255, 255))
        text_rect = text_obj.get_rect(center=(x, y))
        self.screen.blit(text_obj, text_rect)

    def roll_jenga_dice(self):
        rounds = 0
        while total_jenga_dice > 0:
            rounds += 1
            rolled_results = [random.randint(1,6) for _ in range(total_dice)]
            ones_count = rolled_results.count(1)
            total_jenga_dice -= ones_count

