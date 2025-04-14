import pygame
import sys
import os
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
        if game.state == "MAIN_MENU":
            action = menu.run_menu("Project Kessler - Asteroid Miner", MAIN_MENU_OPTIONS)
            if action == "START_GAME":
                if os.path.exists("savegame.dat"):
                    # game.load_game()
                    game.reset()
                    game.state = "START_GAME"
                else:
                    game.reset()
                    game.state = "START_GAME"
            elif action == "INSTRUCTIONS":
                game.state = "INSTRUCTIONS"
            elif action == "OPTIONS":
                game.state = "OPTIONS"
            elif action == "EXIT":
                pygame.quit()
                sys.exit()
        
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
                pygame.quit()
                sys.exit()
        else:
            game.state = "MAIN_MENU"
        


if __name__ == "__main__":
    main()


def emergency_exit():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LCTRL] and keys[pygame.K_q]:
        pygame.quit()
        sys.exit()