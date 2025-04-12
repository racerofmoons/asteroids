import pygame
import sys
from constants import *

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.Font(None, 74)
        self.option_font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()
    
    def flip_helper(self):
        pygame.display.flip()
        self.clock.tick(FPS)
    
    def title_printer(self, text, text_color=WHITE_COLOR, background=BLACK_COLOR):
        self.screen.fill(background)
        title_text = self.title_font.render(text, True, text_color)
        title_rect = title_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 6))
        self.screen.blit(title_text, title_rect)

    def main_menu(self):
        menu_running = True
        selected_option = 0
        menu_options = ["Start Game", "Instructions", "Options", "Exit"]

        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                keys = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_KP_8:
                        selected_option = (selected_option - 1) % len(menu_options)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_KP_2:
                        selected_option = (selected_option + 1) % len(menu_options)
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        return menu_options[selected_option].upper().replace(" ", "_")
                    
            self.title_printer("Project Kessler - Asteroid Miner", WHITE_COLOR, BLACK_COLOR)

            for i, option in enumerate(menu_options):
                color = WHITE_COLOR if i == selected_option else GRAY_COLOR
                option_text = self.option_font.render(option, True, color)
                option_rect = option_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + i * 50))
                self.screen.blit(option_text, option_rect)
            
            self.flip_helper()

    def instructions(self):
        instructions_running = True

        while instructions_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return "MAIN_MENU"
                    
            self.title_printer("Instructions", WHITE_COLOR, BLACK_COLOR)

            instructions_text = [
                "Use W/A/S/D, Arrow Keys, or numpad to navigate",
                "Space or Numpad 0 to shoot",
                "Beware of asteroid collisions - mine asteroids to salvage resources",
                "You have to destroy the fragments to collect salvaged resources",
                "Avoid collisions! You only start with one chance",
                "Press ESC to pause"
            ]

            for i, line in enumerate(instructions_text):
                text = self.option_font.render(line, True, WHITE_COLOR)
                text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT // 3 + i * 40))
                self.screen.blit(text, text_rect)
            
            self.flip_helper()
        
    def options(self):
        options_running = True
        selected_option = 0
        menu_options = ["Placeholder", "Placeholder", "Placeholder"]

        while options_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return "MAIN_MENU"
                    
            self.title_printer("Options Placeholder", WHITE_COLOR, BLACK_COLOR)

            for i, option in enumerate(menu_options):
                color = WHITE_COLOR if i == selected_option else GRAY_COLOR
                option_text = self.option_font.render(option, True, color)
                option_rect = option_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + i * 50))
                self.screen.blit(option_text, option_rect)
            
            self.flip_helper()


