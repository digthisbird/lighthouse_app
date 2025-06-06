import pygame
import random
import os

class CardPicker:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.card_folder = "assets/cards"
        
        # user messaging
        self.message = ""
        self.message_timer = 0
        self.message_duration = 2000 # 2seconds
        
        # Set colors
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.BEIGE = (166, 147, 126)
        self.BLACK = (0, 0, 0)

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
        self.button_color = self.BEIGE
        self.button_hover_color = self.BLACK
        self.button_width = 200
        self.button_height = 50
        self.button_x = (self.width - self.button_width) // 2
        self.button_y = 275
        self.button_rect = pygame.Rect(self.button_x, self.button_y, self.button_width, self.button_height)
        
        # Font settings
        self.font = pygame.font.SysFont(None, 36)
        
        self.num_cards = 0  # Initialize the number of cards to draw
        self.cards_drawn = []  # Keep track of which cards have been drawn
        self.draw_start_time = None  # Time to start drawing cards from
        self.draw_delay = 500  # Delay in milliseconds between drawing cards
        self.used_cards = []
        self.storage_cards = []

    def draw_message(self):
        if self.message and pygame.time.get_ticks() < self.message_timer + self.message_duration:
            text_obj = self.font.render(self.message, True, (255, 255,255))
            text_rect = text_obj.get_rect(center=(self.width //2, self.height -50))
            self.screen.blit(text_obj, text_rect)
    
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
        self.draw_text("Draw a Card", self.button_x + self.button_width // 2, self.button_y + self.button_height // 2)
       
    def draw_storage_area(self):
        #save drawn aces and kings in a separate area 
        storage_x = 50
        storage_y = self.height - 200
        available_width = self.width - 100
        num_cards = len(self.storage_cards)

        if num_cards > 0:
            card_width = 150
            min_spacing = 10
            dynamic_spacing = max(min_spacing, (available_width / num_cards))
            

            for i, card_key in enumerate(self.storage_cards):
                x_position = storage_x + i * dynamic_spacing
                if x_position > (self.width - card_width):
                    x_position = (self.width - card_width) -((num_cards - i - 1) * (card_width + min_spacing))

                self.screen.blit(self.card_images[card_key], (x_position, storage_y))
   
    def draw_cards(self):
        """Draw the cards one by one with a delay between each card."""
        card_row_y = 400
        total_card_width = len(self.cards_drawn) * 150
        x_offset = (self.width - total_card_width) // 2

        for i, card_key in enumerate(self.cards_drawn):
            self.screen.blit(self.card_images[card_key], (x_offset + 150 * i, card_row_y))
        

    def handle_event(self, event):
        """Handle events for quitting and drawing cards on button click."""
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(pygame.mouse.get_pos()):
                    if self.num_cards == 0:
                        self.message = "Roll the dice to start the week!"
                        self.message_timer = pygame.time.get_ticks()
                    elif len(self.cards_drawn) >= self.num_cards:
                        self.message = "No more cards can be drawn."
                        self.message_timer = pygame.time.get_ticks()
                    else:
                        available_cards = [key for key in self.card_images.keys() if key not in self.used_cards]
                        if not available_cards:
                            self.message = "All cards have been drawn!"
                            self.message_timer = pygame.time.get_ticks()
                            return True
                        card_key = random.choice(available_cards)
                        self.cards_drawn.append(card_key)
                        self.used_cards.append(card_key) #ensure the card is added to the used cards list.

                        rank = card_key[:-1]
                        if rank in ['A', 'K']:
                            self.storage_cards.append(card_key)
                        self.message = ""
        return True


class DiceRoller:
    def __init__(self, screen, width, height, card_picker):
        self.screen = screen
        self.width = width
        self.height = height
        self.card_picker = card_picker
        self.dice_folder = "assets/dice_assets"
        
        # Set colors
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.BEIGE = (166, 147, 126)
        self.BLACK = (0, 0, 0)

        # Load and scale dice images
        self.dice_images = [
            pygame.transform.scale(
                pygame.image.load(os.path.join(self.dice_folder, f"white{i}.png")), (100, 100)
            ) for i in range(1, 7)
        ]

        # Button settings
        self.button_color = self.BEIGE
        self.button_hover_color = self.BLACK
        self.button_width = 250
        self.button_height = 50
        self.button_x = ((self.width - self.button_width) // 2)
        self.button_y = 50
        self.button_rect = pygame.Rect(self.button_x, self.button_y, self.button_width, self.button_height)
        
        # Font settings
        self.font = pygame.font.SysFont(None, 24)

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
        self.draw_text("Roll A Die To Start The Week", self.button_x + self.button_width // 2, self.button_y + self.button_height // 2)

    def draw_dice(self):
        """Draw the current dice face on the screen."""
        dice_x = 450
        dice_y = 125
        self.screen.blit(self.dice_images[self.current_dice_index], (dice_x, dice_y))

    def roll_dice(self):
        """Roll a random dice and update the current dice face."""
        rolled_number = random.randint(1, 6)
        self.current_dice_index = rolled_number - 1
        print(f"Rolled: {rolled_number}")
        return rolled_number

    def handle_event(self, event):
    # Handle events for quitting and rolling dice on button click.
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(pygame.mouse.get_pos()):
                rolled_number = self.roll_dice()
                self.card_picker.num_cards = rolled_number  # Set the number of cards to draw
                self.card_picker.cards_drawn = []  # Reset drawn cards when new roll happens
                
                return True  # Continue the game
        return False

class CoinFlipper:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.coin_folder = "assets/coin_faces"
        
        # Set colors
        self.WHITE = (255, 255, 255)
        self.BEIGE = (166, 147, 126)
        self.BLACK = (0, 0, 0)

        # Load the coin images (heads and tails)
        self.coin_images = {
            "heads": pygame.transform.scale(pygame.image.load(os.path.join(self.coin_folder, "heads.png")), (75, 75)),
            "tails": pygame.transform.scale(pygame.image.load(os.path.join(self.coin_folder, "tails.png")), (75, 75))
        }
        
        self.current_side = None  # No coin flip result initially
        #width - self.button_width - 40
        # Button settings for flipping the coin
        self.button_color = self.BEIGE
        self.button_hover_color = self.BLACK
        self.button_width = 150
        self.button_height = 50
        self.button_x = 70
        self.button_y = 225
        self.button_rect = pygame.Rect(self.button_x, self.button_y, self.button_width, self.button_height)
        
        # Font settings
        self.font = pygame.font.SysFont(None, 24)
        self.result_font = pygame.font.SysFont(None, 24)

    def draw_text(self, text, x, y, font):
        """Helper function to draw text on the screen."""
        text_obj = font.render(text, True, self.WHITE)
        text_rect = text_obj.get_rect(center=(x, y))
        self.screen.blit(text_obj, text_rect)

    def draw_button(self):
        """Draw the button on the screen."""
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, self.button_hover_color, self.button_rect)
        else:
            pygame.draw.rect(self.screen, self.button_color, self.button_rect)
        self.draw_text("Flip Coin", self.button_x + self.button_width // 2, self.button_y + self.button_height // 2, self.font)

    def flip_coin(self):
        """Flip the coin and randomly show heads or tails."""
        self.current_side = random.choice(["heads", "tails"])

    def draw_coin(self):
    #Draw the coin's current side on the screen if it's been flipped.""
        if self.current_side:
            self.screen.blit(self.coin_images[self.current_side], (110, 279))
            # Draw the text result under the coin
            self.draw_text(self.current_side.capitalize(), 145, 365, self.result_font)

    def handle_event(self, event):
        """Handle the coin flip event on button click."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.flip_coin()
                return True
        return True

class JengaTower:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
      
        self.WHITE = (255, 255, 255)
        self.BEIGE = (166, 147, 126)
        self.BLACK = (0, 0, 0)
        self.TRANSPARENT_BEIGE = (166, 147, 126, 150)

        self.button_color = self.BEIGE
        self.button_hover_color = self.BLACK
        self.button_width = 200
        self.button_height = 50
        self.button_x = 50
        self.button_y = 50
        self.button_rect = pygame.Rect(self.button_x, self.button_y, self.button_width, self.button_height)
        self.results = ""

        self.area_color = self.TRANSPARENT_BEIGE
        self.area_rect_width = 250
        self.area_rect_height = 175
        self.area_rect_x = 25
        self.area_rect_y = 25
        self.area_rect =pygame.Rect(self.area_rect_x, self.area_rect_y, self.area_rect_width, self.area_rect_height)

        self.font = pygame.font.SysFont(None, 24)
        self.button_font = pygame.font.SysFont(None, 24)

        self.total_jenga_dice = 100
        self.rounds = 0

    def draw_text(self, text, x, y, font):
        text_obj = self.font.render(text, True, self.WHITE)
        text_rect = text_obj.get_rect(center=(x, y))
        self.screen.blit(text_obj, text_rect)

    def draw_button(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, self.BLACK, self.button_rect)
        else:
            pygame.draw.rect(self.screen, self.BEIGE, self.button_rect)
        self.draw_text("Pull From the Tower", self.button_x + self.button_width // 2, self.button_y + self.button_height // 2, self.font)

    def draw_area(self):
        pygame.draw.rect(self.screen, self.BEIGE, self.area_rect, pygame.SRCALPHA)
    
    def draw(self):
        self.draw_area()
        self.draw_button()
        lines = self.results.split('\n')
        y_offset = self.area_rect_y + self.button_height + 30
        for line in lines:
            text = self.font.render(line, True, self.WHITE)
            self.screen.blit(text, (self.area_rect_x + 30, y_offset))
            y_offset += 20


    def roll_jenga_dice(self):
        if self.total_jenga_dice > 0:
            self.rounds += 1
            self.results = f"Roll {self.rounds}: Rolling {self.total_jenga_dice} Dice\n"

            rolled_results = [random.randint(1,6) for _ in range(self.total_jenga_dice)]
            ones_count = rolled_results.count(1)

            self.results += f"Removing {ones_count} chances\n"
            
            self.total_jenga_dice -= ones_count
            self.results += f"Chances left: {self.total_jenga_dice}\n\n"

            if self.total_jenga_dice <= 0:
                self.results += f"\nGame Over in {self.rounds} pulls!"
            else:
                self.results += ""
        
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(pygame.mouse.get_pos()):
                self.roll_jenga_dice()

def roll_extra_die():
    return random.randint(1, 6)

def draw_extra_die(screen, dice_images, dice_index, x, y):
    screen.blit(dice_images[dice_index], (x,y))

def draw_extra_die_button(screen, button_rect, font):
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (0, 0, 0), button_rect)
    else:
        pygame.draw.rect(screen, (166, 147, 126), button_rect)
    text_obj = font.render("Roll Extra Die", True, (255, 255, 255))
    text_rect = text_obj.get_rect(center=button_rect.center)
    screen.blit(text_obj, text_rect)


def handle_extra_die_click (event, button_rect):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            return True   
    return False

# Main game loop
def main():
    # Initialize Pygame
    pygame.init()
    pygame.font.init()

    # Set up display
    width, height = 1000, 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Solo RPG Helper")

    icon = pygame.image.load(os.path.join("Lighthouse.png"))
    pygame.display.set_icon(icon)

    #set bg image
    bg = pygame.image.load(os.path.join("map_bg.jpg"))
    #scale bg
    bg = pygame.transform.scale(bg, (width, height))

    # Initialize the dice roller and card picker and coin flipper
    card_picker = CardPicker(screen, width, height)
    dice_roller = DiceRoller(screen, width, height, card_picker)
    coin_flipper = CoinFlipper(screen, width, height)
    jenga_tower = JengaTower(screen, width, height)

    round_counter = 0
    round_font = pygame.font.SysFont(None, 36)
    extra_die_font =pygame.font.SysFont(None, 24)
    

    def draw_round_counter():
        round_text = round_font.render(f"Week: {round_counter}", True, (255, 255, 255))
        screen.blit(round_text, (width - 150, 30))

    #extra die setup
    extra_dice_images = [
        pygame.transform.scale(pygame.image.load(os.path.join("assets/dice_assets", f"white{i}.png")), (50, 50))
        for i in range(1, 6 + 1)
    ]
    extra_die_index = 0
    extra_die_x = 750
    extra_die_y = 150
    extra_die_button_rect = pygame.Rect(extra_die_x - 50, extra_die_y - 50, 150, 40)

    # Main game loop
    running = True
    while running:
        screen.blit(bg, (0,0))

        # Draw the dice and button
        dice_roller.draw_dice()
        dice_roller.draw_button()

        #Draw the card button
        card_picker.draw_button()
        card_picker.draw_message()

        #Draw coin
        coin_flipper.draw_button()
        coin_flipper.draw_coin()

        #draw jenga setup
        jenga_tower.draw()

        #draw extra die
        draw_extra_die(screen, extra_dice_images, extra_die_index, extra_die_x, extra_die_y)
        draw_extra_die_button(screen, extra_die_button_rect, extra_die_font)

        # Handle events for dice and card picking
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if dice_roller.handle_event(event):
                round_counter += 1
            if card_picker.handle_event(event):
                pass
            coin_flipper.handle_event(event)
            jenga_tower.handle_event(event)
            if handle_extra_die_click(event, extra_die_button_rect):
                extra_die_index = roll_extra_die() -1
            
        card_picker.draw_message()

        # Draw the cards with delay
        if card_picker.cards_drawn:
            card_picker.draw_cards()

        draw_round_counter()
        card_picker.draw_storage_area()

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()