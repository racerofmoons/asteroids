import pygame
import sys
from constants import *

user_menu_inputs = [
    ((pygame.K_UP, pygame.K_w, pygame.K_KP_8), "UP"),
    ((pygame.K_DOWN, pygame.K_s, pygame.K_KP_2), "DOWN"),
    ((pygame.K_RETURN, pygame.K_KP_ENTER), "SELECT")
]

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

    def menu_event_handler(self, event, menu_options, selected_option, user_inputs=user_menu_inputs):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return selected_option, menu_options[selected_option].upper().replace(" ", "_")
        if event.type == pygame.KEYDOWN:
            for inputs, action, in user_inputs:
                if event.key in inputs:
                    if action == "UP" and selected_option > 0:
                        selected_option = (selected_option - 1) % len(menu_options)
                    if action == "DOWN" and selected_option < len(menu_options) - 1:
                        selected_option = (selected_option + 1) % len(menu_options)
                    if action == "SELECT":
                        return selected_option, menu_options[selected_option].upper().replace(" ", "_")
        return selected_option, None

    def main_menu(self):
        menu_running = True
        selected_option = 0
        while menu_running:
            for event in pygame.event.get():
                result = self.menu_event_handler(event, MAIN_MENU_OPTIONS, selected_option)
                selected_option = result[0]
                if result[1]:
                    return result[1]
                    
            self.title_printer("Project Kessler - Asteroid Miner", WHITE_COLOR, BLACK_COLOR)

            for i, option in enumerate(MAIN_MENU_OPTIONS):
                color = WHITE_COLOR if i == selected_option else GRAY_COLOR
                option_text = self.option_font.render(option, True, color)
                option_rect = option_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + i * 50))
                self.screen.blit(option_text, option_rect)
            
            self.flip_helper()

    def draw_score_table(self, resources, table_width=600, row_height=40):
        font = pygame.font.Font(None, 36)
        table_height = 8 * row_height + 50
        table_x = (SCREEN_WIDTH - table_width) // 2
        table_y = (SCREEN_HEIGHT - table_height) // 2
        table_bg = pygame.Surface((table_width, table_height))
        table_bg.fill((0, 0, 0, 128))
        self.screen.blit(table_bg, (table_x, table_y))
        col_width = table_width // 2
        for i, (key, value) in enumerate(RESOURCES.items()):
            name_text = font.render(value, True, (220, 220, 220))
            name_rect = name_text.get_rect(midleft=(table_x + 20, table_y + 50 + i * row_height))
            self.screen.blit(name_text, name_rect)

            value_text = font.render(str(resources[i]), True, (220, 220, 220))
            value_rect = value_text.get_rect(midright=(table_x + table_width - 20, table_y + 50 + i * row_height))
            self.screen.blit(value_text, value_rect)
        
        
    def pause_menu(self, resources):
        pause_menu_running = True
        selected_option = 0
        while pause_menu_running:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 128))
            font = pygame.font.Font(None, 74)
            text = font.render("PAUSED", True, (255, 255, 255))
            text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            self.screen.blit(text, text_rect)
            self.draw_score_table(resources)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pause_menu_running = False
                    return "QUIT"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pause_menu_running = False
                        return "PLAYING"
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
                "Game auto-saves progress at regular intervals",
                "You have to destroy the fragments to collect salvaged resources",
                "Avoid collisions! You only start with one chance",
                "Press ESC to pause"
            ]

            for i, line in enumerate(instructions_text):
                text = self.option_font.render(line, True, WHITE_COLOR)
                text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT // 3 + i * 40))
                self.screen.blit(text, text_rect)
            
            self.flip_helper()

