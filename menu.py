import pygame
import sys
from constants import *
from config import *
from ui import *

user_menu_inputs = [
    ((pygame.K_UP, pygame.K_w, pygame.K_KP_8), "UP"),
    ((pygame.K_DOWN, pygame.K_s, pygame.K_KP_2), "DOWN"),
    ((pygame.K_RETURN, pygame.K_KP_ENTER), "SELECT"),
    ((pygame.K_LEFT, pygame.K_KP_4), "LEFT"),
    ((pygame.K_RIGHT, pygame.K_KP_6), "RIGHT")
]

class Menu:
    def __init__(self, config):
        self.config = config
        self.title_font = pygame.font.Font(None, 74)
        self.option_font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()
        self.keyboard_navigation = True
        self.menu = "MAIN_MENU"
        self.submenu = None
    
    def flip_helper(self):
        pygame.display.flip()
        self.clock.tick(FPS)
    
    def title_printer(self, text, text_color=WHITE_COLOR, background=BLACK_COLOR):
        self.config.screen.fill(background)
        title_text = self.title_font.render(text, True, text_color)
        if self.menu == "LOAD_MENU":
            title_height = 12
        else: 
            title_height = 8
        title_rect = title_text.get_rect(center=(self.config.screen.get_width() // 2, self.config.screen.get_height() // title_height))
        self.config.screen.blit(title_text, title_rect)

    def menu_escape_keypress(self, selected_option):
        if self.menu == "MAIN_MENU":
            quitter()
        else:
            self.menu = "MAIN_MENU"
            self.submenu = None


        return selected_option, None
    
    def user_input_handler(self, event, menu_options, selected_option):
        user_menu_inputs = [
            ((pygame.K_UP, pygame.K_w, pygame.K_KP_8), "UP"),
            ((pygame.K_DOWN, pygame.K_s, pygame.K_KP_2), "DOWN"),
            ((pygame.K_RETURN, pygame.K_KP_ENTER), "SELECT"),
            ((pygame.K_LEFT, pygame.K_KP_4), "LEFT"),
            ((pygame.K_RIGHT, pygame.K_KP_6), "RIGHT")
            ]
        for inputs, action, in user_menu_inputs:
            if event.key in inputs:
                if action in ("UP", "LEFT") and selected_option > 0:
                    selected_option = (selected_option - 1) % len(menu_options)
                if action in ("DOWN", "RIGHT") and selected_option < len(menu_options) - 1:
                    selected_option = (selected_option + 1) % len(menu_options)
                if action == "SELECT":
                    return selected_option, menu_options[selected_option].upper().replace(" ", "_")
        return selected_option, None

    def menu_event_handler(self, event, menu_options, selected_option, user_inputs=user_menu_inputs):
        if event.type == pygame.QUIT:
            quitter()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return self.menu_escape_keypress(selected_option)
        if event.type == pygame.KEYDOWN:
            return self.user_input_handler(event, menu_options, selected_option)
        elif event.type == pygame.MOUSEMOTION:
            self.keyboard_navigation = False
        return selected_option, None
    
    def create_menu_buttons(self, menu_options, orientation="VERTICAL", selected_option=0):
        buttons = []
        max_width = max([self.option_font.render(option, True, BUTTON_COLOR).get_width() for option in menu_options])
        max_height = max([self.option_font.render(option, True, BUTTON_COLOR).get_height() for option in menu_options])
        for i, option in enumerate(menu_options):
            if orientation == "VERTICAL":
                position = (self.config.screen_width // 5 - 100, self.config.screen_height // 3 + i * 50)
            elif orientation == "HORIZONTAL":
                menu_width = len(menu_options) * (max_width + 10)
                position = ((self.config.screen_width - menu_width) // 2 + i * (max_width + 20), self.config.screen_height // 8)
            btn = Button(
                position = position,
                text = option,
                font = self.option_font,
                color = GRAY_COLOR,
                hover_color = WHITE_COLOR,
                action = lambda opt=option: opt,
                width = max_width,
                height = max_height
                )
            buttons.append(btn)
        return buttons

    def draw_menu_buttons(self, buttons, selected_option=0):
        for i, button in enumerate(buttons):
            is_selected = (selected_option is not None and i == selected_option)
            button.draw(self.config.screen, is_selected)

    def create_table_buttons(self, game, table_x, table_y, row_height=40):
        buy_buttons, sell_buttons, display_indicies = [], [], range(1, 8)
        button_font = pygame.font.Font(None, 24)
        button_height = 16
        button_width = 60
        for row_id, resource_id in enumerate(display_indicies):
            buy_position = (table_x + 160, table_y + 30 + (row_id * row_height))
            sell_position = (table_x + 240, table_y + 30 + (row_id * row_height))
            buy_btn = Button(
                position=buy_position,
                text="Buy 10",
                font=button_font,
                color=BUTTON_COLOR,
                hover_color=BUTTON_HOVER_COLOR,
                action=lambda rid=resource_id: self.buy_resource(rid),
                width=button_width,
                height=button_height
            )
            buy_buttons.append(buy_btn)
            sell_btn = Button(
                position=sell_position,
                text="Sell 10",
                font=button_font,
                color=BUTTON_COLOR,
                hover_color=BUTTON_HOVER_COLOR,
                action=lambda rid=resource_id: self.sell_resource(rid),
                width=button_width,
                height=button_height
            )
            sell_buttons.append(sell_btn)
        return buy_buttons, sell_buttons


    def menu_render_selector(self, title, menu_buttons, selected_option, game):
        default = None
        if self.menu == "MAIN_MENU":
            return default
        if self.menu == "LOAD_MENU":
            self.load_menu_render(title, menu_buttons, selected_option)
            self.load_menu_submenu_loader(game)
            self.status_printer(game)
        if self.menu == "OPTIONS":
            return default
        if self.menu == "CONTROLS":
            return default
        if self.menu == "CREDITS":
            return default
        if self.menu == "PAUSE":
            return default
        
    def load_menu_render(self, title, menu_buttons, selected_option):
        pass

    def status_printer(self, game):
        font = pygame.font.Font(None, 30)
        level_text = font.render(f"Level: {game.resources[8]}", True, WHITE_COLOR)
        level_rect = level_text.get_rect(midleft=(self.config.screen.get_width() // 12 - 15, self.config.screen.get_height() // 10 - 30))
        xp_text = font.render(f"Current XP: {game.resources[9]}", True, WHITE_COLOR)
        xp_rect = xp_text.get_rect(midleft=(self.config.screen.get_width() // 12 - 15, self.config.screen.get_height() // 10 - 0))
        next_level_text = font.render(f"XP to level {game.resources[8] + 1}: {game.resources[10]}", True, WHITE_COLOR)
        next_level_rect = next_level_text.get_rect(midleft=(self.config.screen.get_width() // 12 - 15, self.config.screen.get_height() // 10 + 30))
        self.config.screen.blit(level_text, level_rect)
        self.config.screen.blit(xp_text, xp_rect)
        self.config.screen.blit(next_level_text, next_level_rect)
        

    def load_menu_submenu_loader(self, game):
        if self.submenu in (None, "VISIT_TRADER"):
            self.render_scorecard(game)
        if self.submenu == "RESEARCH_LAB":
            self.render_lab()
        if self.submenu == "UPGRADE_SHIP":
            self.render_upgrades()
    
    def render_scorecard(self, game, table_width=600, row_height=40):
        header_font = pygame.font.Font(None, 40)
        font = pygame.font.Font(None, 30)
        display_indicies  =range(1, 8)
        table_height = len(display_indicies) * row_height + 80
        table_x = (self.config.screen_width - table_width) // 10
        table_y = (self.config.screen_height - table_height) // 3
        table_bg = pygame.Surface((table_width, table_height))
        table_bg.fill((0, 0, 0, 128))
        self.config.screen.blit(table_bg, (table_x, table_y))

        title = font.render("Minerals Gathered", True, WHITE_COLOR)
        title_rect = title.get_rect(midtop=(table_x + table_width//2, table_y + 10))
        self.config.screen.blit(title, title_rect)

        buy_buttons, sell_buttons = self.create_table_buttons(game, table_x, table_y)
        for row_id, resource_id in enumerate(display_indicies):
            if resource_id < len(game.resources):
                resource_name = list(RESOURCES.values())[resource_id]
                name_text = font.render(resource_name, True, LIGHT_GREY_COLOR)
                name_rect = name_text.get_rect(midleft=(table_x + 20, table_y + 50 + row_id * row_height))
                self.config.screen.blit(name_text, name_rect)

                value_text = font.render(str(game.resources[resource_id]), True, LIGHT_GREY_COLOR)
                value_rect = value_text.get_rect(midright=(table_x - 20, table_y + 50 + row_id * row_height))
                self.config.screen.blit(value_text, value_rect)
        for button in buy_buttons:
            button.draw(self.config.screen)
        for button in sell_buttons:
            button.draw(self.config.screen)

        top_left = (table_x, table_y)
        top_right = (table_x + table_width, table_y)
        bottom_right = (table_x + table_width, table_y + table_height)
        bottom_left = (table_x, table_y + table_height)
        return top_left, top_right, bottom_right, bottom_left

    def render_trader(self):
        pass

    def render_lab(self):
        pass

    def render_upgrades(self):
        pass

    def run_menu(
            self,
            title, 
            menu_options,
            game=None,
            submenu_options=None,
            orientation="VERTICAL",
            background_color=BLACK_COLOR,
            pre_render_callback=None,
            post_render_callback=None
            ):
        menu_running = True
        selected_option = 0
        menu_buttons = self.create_menu_buttons(menu_options, orientation)
        while menu_running:
            emergency_exit()
            self.config.screen.fill(background_color)
            if pre_render_callback:
                pre_render_callback(self)
            for i, button in enumerate(menu_buttons):
                if not self.keyboard_navigation:
                    if button.is_hovered():
                        selected_option = i
                        break
            self.title_printer(title, WHITE_COLOR, BLACK_COLOR)
            self.draw_menu_buttons(menu_buttons, selected_option)
            self.menu_render_selector(title, menu_buttons, selected_option, game)
            if post_render_callback:
                post_render_callback(self)
            for event in pygame.event.get():
                result = self.menu_event_handler(event, menu_options, selected_option)
                selected_option = result[0]
                if result[1]:
                    return result[1]
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    print(f"Mouse clicked at position: {event.pos}")
                    for button in menu_buttons:
                        print(f"Checking button: {button}, rect: {button.rect}, contains click: {button.rect.collidepoint(event.pos)}")
                        action_result = button.click()
                        print(f"Button click result: {action_result}")
                        if action_result:
                            return action_result
            self.flip_helper()







    def draw_score_table(self, game, table_width=600, row_height=30):
        header_font = pygame.font.Font(None, 40)
        font = pygame.font.Font(None, 30)
        table_height = len(RESOURCES) * row_height + 50
        table_x = 50
        table_y = (self.config.screen_height - table_height) // 2

        max_name_width = 0
        max_value_width = 0
        for key,value in RESOURCES.items():
            name_text = font.render(value, True, LIGHT_GREY_COLOR)
            value_text = font.render(str(game.resources[key]), True, LIGHT_GREY_COLOR)
            max_name_width = max(max_name_width, name_text.get_width())
            max_value_width = max(max_value_width, value_text.get_width())
        dynamic_width = max_name_width + max_value_width + max_name_width + max_value_width + 100
        table_width = max(table_width, dynamic_width)

        table_bg = pygame.Surface((table_width, table_height))
        table_bg.fill((0, 0, 0, 128))
        self.config.screen.blit(table_bg, (table_x, table_y))

        header_text = header_font.render("Gathered Resources", True, LIGHT_GREY_COLOR)
        header_rect = header_text.get_rect(midtop=(table_x + (max_name_width + max_value_width + 40) // 2, table_y + 10))
        self.config.screen.blit(header_text, header_rect)
        for i, (key, value) in enumerate(RESOURCES.items()):
            name_text = font.render(value, True, LIGHT_GREY_COLOR)
            name_rect = name_text.get_rect(midleft=(table_x + 20, table_y + 50 + i * row_height))
            self.config.screen.blit(name_text, name_rect)

            value_text = font.render(str(game.resources[key]), True, LIGHT_GREY_COLOR)
            value_rect = value_text.get_rect(midright=(table_x + table_width - 20, table_y + 50 + i * row_height))
            self.config.screen.blit(value_text, value_rect)

            buy_text = font.render(value + " Buy-Button", True, LIGHT_GREY_COLOR)
            buy_rect = buy_text.get_rect(midleft=(table_x + max_name_width + 100, table_y + 50 + i * row_height))
            self.config.screen.blit(buy_text, buy_rect)

            sell_text = font.render(value + " Sell-Button", True, LIGHT_GREY_COLOR)
            sell_rect = sell_text.get_rect(midright=(table_x + table_width - 20, table_y + 50 + i * row_height))
            self.config.screen.blit(sell_text, sell_rect)

            
        
        
    def pause_menu(self, resources):
        pause_menu_running = True
        selected_option = 0
        while pause_menu_running:
            overlay = pygame.Surface((self.config.screen_width, self.config.screen_height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 128))
            font = pygame.font.Font(None, 74)
            text = font.render("PAUSED", True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.config.screen_width/2, self.config.screen_height/2))
            self.config.screen.blit(text, text_rect)
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

        
    def options_menu(self):
        options_running = True
        selected_option = 0
        menu_options = ["Placeholder", "Placeholder", "Placeholder"]

        while options_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitter()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return "MAIN_MENU"
                    
            self.title_printer("Options Placeholder", WHITE_COLOR, BLACK_COLOR)

            for i, option in enumerate(menu_options):
                color = WHITE_COLOR if i == selected_option else GRAY_COLOR
                option_text = self.option_font.render(option, True, color)
                option_rect = option_text.get_rect(center=(self.config.screen_width // 2, self.config.screen_height // 2 + i * 50))
                self.config.screen.blit(option_text, option_rect)
            
            self.flip_helper()


    def instructions(self):
        instructions_running = True

        while instructions_running:
            for event in pygame.event.get():
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
                text_rect = text.get_rect(center=(self.config.screen_width/2, self.config.screen_height // 3 + i * 40))
                self.config.screen.blit(text, text_rect)
            
            self.flip_helper()

