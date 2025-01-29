import pygame
import random
import os

class DiceRoller:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.dice_folder = "assets/dice_assets"
        
        # Set colors
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)

        # Load and scale dice images
        self.dice_images = [
            pygame.transform.scale(
                pygame.image.load(os.path.join(self.dice_folder, f"white{i}.png")), (100, 100)
            ) for i in range(1, 7)
        ]

        # Button settings
        self.button_color = self.BLUE
        self.button_hover_color = self.RED
        self.button_width = 200
        self.button_height = 50
        self.button_x = (self.width - self.button_width) // 2
        self.button_y = (self.height - self.button_height) // 2 + 250
        self.button_rect = pygame.Rect(self.button_x, self.button_y, self.button_width, self.button_height)
        
        # Font settings
        self.font = pygame.font.SysFont(None, 36)

        # Set the initial dice face to 1 (first image)
        self.current_dice_index = 0

    def draw_text(self, text, x, y):
        """Helper function to draw text on the screen."""
        text_obj = self.font.render(text, True, (255, 255, 255))
        text_rect = text_obj.get_rect(center=(x, y))
        self.screen.blit(text_obj, text_rect)

    def draw_button(self):
        """Draw the button on the screen."""
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, self.button_hover_color, self.button_rect)
        else:
            pygame.draw.rect(self.screen, self.button_color, self.button_rect)
        self.draw_text("Roll the Dice!", self.button_x + self.button_width // 2, self.button_y + self.button_height // 2)

    def draw_dice(self):
        """Draw the current dice face on the screen."""
        self.screen.blit(self.dice_images[self.current_dice_index], (self.width // 2 - 50, self.height // 2 - 200))

    def roll_dice(self):
        """Roll a random dice and update the current dice face."""
        rolled_number = random.randint(1, 6)
        self.current_dice_index = rolled_number - 1
        print(f"Rolled: {rolled_number}")
        return rolled_number

    def handle_event(self, event):
        """Handle events for quitting and rolling dice on button click."""
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(pygame.mouse.get_pos()):
                return self.roll_dice()  # Roll the dice and return the result
        return True
