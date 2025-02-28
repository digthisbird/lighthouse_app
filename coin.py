import pygame
import random
import os

class CoinFlipper:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.coin_folder = "assets/coin"
        
        # Set colors
        self.WHITE = (255, 255, 255)
        self.BEIGE = (166, 147, 126)
        self.BLACK = (0, 0, 0)

        # Load the coin images (heads and tails)
        self.coin_images = {
            "heads": pygame.transform.scale(pygame.image.load(os.path.join(self.coin_folder, "heads.png")), (100, 100)),
            "tails": pygame.transform.scale(pygame.image.load(os.path.join(self.coin_folder, "tails.png")), (100, 100))
        }
        
        self.current_side = None  # No coin flip result initially
        
        # Button settings for flipping the coin
        self.button_color = self.BEIGE
        self.button_hover_color = self.BLACK
        self.button_width = 200
        self.button_height = 50
        self.button_x = width - self.button_width - 50
        self.button_y = 150
        self.button_rect = pygame.Rect(self.button_x, self.button_y, self.button_width, self.button_height)
        
        # Font settings
        self.font = pygame.font.SysFont(None, 24)

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
        self.draw_text("Flip Coin", self.button_x + self.button_width // 2, self.button_y + self.button_height // 2)

    def flip_coin(self):
        """Flip the coin and randomly show heads or tails."""
        self.current_side = random.choice(["heads", "tails"])

    def draw_coin(self):
        """Draw the coin's current side on the screen if it's been flipped."""
        if self.current_side:
            self.screen.blit(self.coin_images[self.current_side], (self.width - 150, 230))

    def handle_event(self, event):
        """Handle the coin flip event on button click."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.flip_coin()
                return True
        return True
