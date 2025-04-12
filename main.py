import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet
from game import Game
from menu import Menu


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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

    game = Game(screen)
    menu = Menu(screen)


    while True:
        if game.state == "MAIN_MENU":
            action = menu.main_menu()
            if action == "START_GAME":
                if sum(game.resources) == 0:
                    game.state = "START_GAME"
                else:
                    game.state = "LOAD_GAME"
            elif action == "INSTRUCTIONS":
                game.state = "INSTRUCTIONS"
            elif action == "OPTIONS":
                game.state = "OPTIONS"
            elif action == "EXIT":
                pygame.quit()
                return
        
        elif game.state == "INSTRUCTIONS":
            action = menu.instructions()
            if action == "MAIN_MENU" or action == "QUIT":
                game.state = action
        
        elif game.state == "OPTIONS":
            action = menu.options()
            if action == "MAIN_MENU" or action == "QUIT":
                game.state = action
            
        if game.state == "START_GAME" or game.state == "CONTINUE":
            game_result = game.run()
            if game_result == "GAME_OVER":
                game.state = "MAIN_MENU"
            elif game_result == "QUIT":
                pygame.quit()
                return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game.state = "MAIN_MENU"


        pygame.display.flip()
        


if __name__ == "__main__":
    main()