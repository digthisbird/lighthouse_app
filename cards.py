import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Set up display
width = 800
height = 600
SCREEN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Card Picker")

# Set colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Load card images 
card_folder = "assets/cards"

# Define ranks and suits
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['H', 'D', 'C', 'S']  # Hearts, Diamonds, Clubs, Spades
card_images = {}

for rank in ranks:
    for suit in suits:
        card_file_name = f"{rank}{suit}.png"
        card_image = pygame.image.load(os.path.join(card_folder, card_file_name))
        card_images[f"{rank}{suit}"] =pygame.transform.scale(card_image, (150, 150))



# Button settings
button_color = BLUE
button_hover_color = RED
button_width = 200
button_height = 50
button_x = (width - button_width) // 2
button_y = (height - button_height) // 2 + 150  # Position button below the card

# Create a button rectangle
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# Font for button text
font = pygame.font.SysFont(None, 36)

# Function to display button text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# Function to roll the dice
def pick_card():
    return random.choice(list(card_images.keys())) #picl a random card key

# Set the initial dice face to 1 (first image)
current_card_index = 'AH' #ace of hearts is defaul

# Run the game loop
running = True
while running:
    SCREEN.fill(WHITE)

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Draw the dice
    SCREEN.blit(card_images[current_card_index], (width // 2 - 50, height // 2 - 200))  # Adjust position as needed

    # Check if the mouse is over the button and change color if so
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(SCREEN, button_hover_color, button_rect)
    else:
        pygame.draw.rect(SCREEN, button_color, button_rect)

    # Display button text
    draw_text("Pick a Card!", font, WHITE, SCREEN, button_x + button_width // 2, button_y + button_height // 2)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check if the mouse button is pressed inside the button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(mouse_pos):
                # Roll the dice (select a new random face)
                random_card = pick_card()
                current_card_index = random_card  # Update the card
                print(f"{random_card}")

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()