import pygame
import random
import os
class CardPicker:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.card_folder = "assets/cards"
        
        # Set colors
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)

        # Load card images
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.suits = ['H', 'D', 'C', 'S']  # Hearts, Diamonds, Clubs, Spades
        self.card_images = {}
        
        # Load the card images and scale them
        for rank in self.ranks:
            for suit in self.suits:
                card_file_name = f"{rank}{suit}.png"
                card_image = pygame.image.load(os.path.join(self.card_folder, card_file_name))
                self.card_images[f"{rank}{suit}"] = pygame.transform.scale(card_image, (150, 150))

        # Button settings
        self.button_color = self.BLUE
        self.button_hover_color = self.RED
        self.button_width = 200
        self.button_height = 50
        self.button_x = (self.width - self.button_width) // 2
        self.button_y = (self.height - self.button_height) // 2 + 150
        self.button_rect = pygame.Rect(self.button_x, self.button_y, self.button_width, self.button_height)
        
        # Font settings
        self.font = pygame.font.SysFont(None, 36)
        
        self.num_cards = 0  # Initialize the number of cards to draw
        self.cards_drawn = []  # Keep track of which cards have been drawn
        self.draw_start_time = None  # Time to start drawing cards from
        self.draw_delay = 500  # Delay in milliseconds between drawing cards
    
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
        self.draw_text("Draw Cards!", self.button_x + self.button_width // 2, self.button_y + self.button_height // 2)

    def draw_cards(self):
        """Draw the cards one by one with a delay between each card."""
        if self.draw_start_time is None:
            return
        
        elapsed_time = pygame.time.get_ticks() - self.draw_start_time
        num_cards_to_draw = min(self.num_cards, len(self.cards_drawn) + 1)
        
        # Only draw one more card if enough time has passed
        if elapsed_time >= len(self.cards_drawn) * self.draw_delay:
            card_key = random.choice(list(self.card_images.keys()))  # Randomly pick a card
            self.cards_drawn.append(card_key)  # Add it to the list of drawn cards
            
        # Draw all drawn cards so far
        x_offset = self.width // 2 - (75 * num_cards_to_draw)  # To center the cards
        for i in range(num_cards_to_draw):
            self.screen.blit(self.card_images[self.cards_drawn[i]], (x_offset + 150 * i, self.height // 2 - 100))

    def handle_event(self, event):
        """Handle events for quitting and drawing cards on button click."""
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.num_cards = random.randint(1, 6)  # Roll the dice (1-6)
                print(f"Number of cards to draw: {self.num_cards}")
                self.cards_drawn = []  # Reset the cards drawn
                self.draw_start_time = pygame.time.get_ticks()  # Start drawing the cards
        return True