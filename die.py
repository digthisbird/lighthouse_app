import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Set up display
width = 800
height = 600
SCREEN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dice Roller")

# Set colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Load dice images (ensure your dice images are named dice1.png, dice2.png, etc.)
dice_folder = "assets/dice_assets"



dice_images = [
    pygame.image.load(os.path.join(dice_folder, f"white{i}.png")) for i in range(1, 7)
]

# Scale dice images to fit on the screen (adjust size as needed)
dice_images = [pygame.transform.scale(dice, (100, 100)) for dice in dice_images]

# Button settings
button_color = BLUE
button_hover_color = RED
button_width = 200
button_height = 50
button_x = (width - button_width) // 2
button_y = (height - button_height) // 2 + 150  # Position button below the dice

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
def roll_dice():
    return random.randint(1, 6)  # Random number between 1 and 6

# Set the initial dice face to 1 (first image)
current_dice_index = 0

# Run the game loop
running = True
while running:
    SCREEN.fill(WHITE)

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Draw the dice
    SCREEN.blit(dice_images[current_dice_index], (width // 2 - 50, height // 2 - 200))  # Adjust position as needed

    # Check if the mouse is over the button and change color if so
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(SCREEN, button_hover_color, button_rect)
    else:
        pygame.draw.rect(SCREEN, button_color, button_rect)

    # Display button text
    draw_text("Roll the Dice!", font, WHITE, SCREEN, button_x + button_width // 2, button_y + button_height // 2)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check if the mouse button is pressed inside the button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(mouse_pos):
                # Roll the dice (select a new random face)
                rolled_number = roll_dice()
                current_dice_index = rolled_number - 1  # Update the dice index based on the rolled number
                print(f"{rolled_number}")

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()