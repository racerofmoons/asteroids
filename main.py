import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()
    dt = 0
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Bullet.containers = (bullets, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    game = Game()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        if player.shoot_timer > 0:
            player.shoot_timer -= dt

        for object in drawable:
            object.draw(screen)

        for asteroid in asteroids:
            for bullet in bullets:
                if bullet.collision(asteroid):
                    bullet.kill()
                    result = asteroid.split("bullet")
                    if isinstance(result, int):
                        game.score_keeper(result)

        asteroid_list = asteroids.sprites()
        for i, asteroid1 in enumerate(asteroid_list):
            for asteroid2 in asteroid_list[i+1:]:
                if asteroid1.collision(asteroid2):
                    asteroid1.split("asteroid")
                    asteroid2.split("asteroid")

        for object in asteroids:
            if object.collision(player):
                print("Game Over!")
                return

        pygame.display.flip()
        dt = (pygame.time.Clock().tick(60) / 1000)
        


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()