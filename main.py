import pygame
import sys
import os
import pickle
from constants import *
from config import *
from menu import Menu
from game import Game
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet


def main():
    pygame.init()
    pygame.display.set_caption("Project Kessler")
    pygame.time.Clock()
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Bullet.containers = (bullets, updatable, drawable)
    config = Config()
    menu = Menu(config)
    game = Game(config, menu)

    while True:
        emergency_exit()
        save_exists = False
        if game.state == "MAIN_MENU":
            if os.path.exists("savegame.dat"):
                save_exists = True
            action = menu.run_menu(MAIN_MENU_TITLE, MAIN_MENU_OPTIONS, game, None, "VERTICAL", BLACK_COLOR, None, None)
            if action == "START_GAME":
                if not save_exists:
                    game.reset_resources()
                    game.reset_run(config)
                    game.state = "START_GAME"
                elif save_exists:
                    game.reset_resources()
                    game.reset_run(config)
                    game.state = "START_GAME"
            elif action == "LOAD_GAME":
                set_load_state(game, menu)
                game.reset_resources()
                action = menu.run_menu(LOAD_MENU_TITLE, LOAD_GAME_OPTIONS, game, None, "HORIZONTAL", BLACK_COLOR, None, None)
            elif action == "OPTIONS":
                game.state = "OPTIONS"
            elif action == "EXIT":
                quitter()
        elif game.state == "PAUSED":
            pass
        elif game.state == "INSTRUCTIONS":
            action = menu.instructions()
            if action == "MAIN_MENU" or action == "QUIT":
                game.state = action
        
        elif game.state == "OPTIONS":
            action = menu.options()
            if action == "MAIN_MENU" or action == "QUIT":
                game.state = action
            
        if game.state == "START_GAME" or game.state == "PLAYING":
            game_result = game.run()
            if game_result == "GAME_OVER":
                game.save_game()
                game.state = "MAIN_MENU"
            elif game_result == "QUIT":
                quitter()
        else:
            game.state = "MAIN_MENU"
        






def emergency_exit():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LCTRL] and keys[pygame.K_q]:
        quitter()

def quitter():
    pygame.quit()
    sys.exit()

# Getters

def get_game_state(game):
    return game

def get_resources(game):
    return game.resources

def get_upgrades(game):
    return game.player.upgrades

def get_gamestate(game):
    return game.state

def get_config(config):
    return config

def get_menu(menu):
    return menu

# Setters

def set_load_state(game, menu):
    # game.load_game(game)
    game.state = "LOAD_MENU"
    menu.menu = "LOAD_MENU"
    return game



def delete_save(game):
    try:
        os.remove(SAVE_FILE)
        game.reset_all()
        game.reset_run()
    except Exception as e:
        print(f"Error deleting save data: {e}")
        print(f"To manually delete:")
        print(f"1. Navigate to your game folder")
        print(f"2. Manually delete the file named {SAVE_FILE}")
        print(f"3. Restart Game, your save data should be cleared")







if __name__ == "__main__":
    main()


