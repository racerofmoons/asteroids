import pygame
import math
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.resources = [
            0, # credits
            0, # silica
            0, # iron
            0, # aluminum
            0, # cobalt
            0, # gold
            0, # uranium
            0 # thorium
        ]
        self.level = 1
        self.xp = 0
        self.next_level = 10
        self.is_running = False
        self.is_paused = False
        self.state = "MAIN_MENU"


        self.all_sprites = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.updatable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        Player.containers = (self.all_sprites, self.drawable, self.updatable)
        Asteroid.containers = (self.all_sprites, self.asteroids, self.updatable, self.drawable)
        AsteroidField.containers = (self.all_sprites, self.updatable)
        Bullet.containers = (self.all_sprites, self.bullets, self.updatable, self.drawable)
        
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.asteroid_field = AsteroidField()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_paused = not self.is_paused
                    if self.is_paused:
                        return "PAUSE"
        if self.is_paused:
            font = pygame.font.Font(None, 74)
            text = font.render("PAUSED", True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
            self.screen.blit(text, text_rect)
            self.fps_helper()
            return "CONTINUE"
        self.is_running = True
        self.is_paused = False
        self.screen.fill(BLACK_COLOR)
        self.updatable.update(self.dt)
        if self.player.shoot_timer > 0:
            self.player.shoot_timer -= self.dt

        for object in self.drawable:
            object.draw(self.screen)

        for asteroid in self.asteroids:
            for bullet in self.bullets:
                if bullet.collision(asteroid):
                    bullet.kill()
                    result = asteroid.split("bullet")
                    if isinstance(result, int):
                        self.score_keeper(result)
        
        asteroid_list = self.asteroids.sprites()
        for i, asteroid1 in enumerate(asteroid_list):
            for asteroid2 in asteroid_list[i+1:]:
                if asteroid1.collision(asteroid2):
                    asteroid1.split("asteroid")
                    asteroid2.split("asteroid")

        for object in self.asteroids:
            if object.collision(self.player):
                return "GAME_OVER"
        
        self.fps_helper()
        return "CONTINUE"

    def fps_helper(self):
        pygame.display.flip()
        self.dt = (self.clock.tick(FPS) / 1000)

    def reset(self):
        self.resources = [
            0, # credits
            0, # silica
            0, # iron
            0, # aluminum
            0, # cobalt
            0, # gold
            0, # uranium
            0 # thorium
        ]
        self.level = 1
        self.xp = 0
        self.next_level = 10

    def score_keeper(self, target_tier):
        self.resources[target_tier] += 1
        self.xp += target_tier
        self.resources[CREDITS] += target_tier * 2
        if self.xp >= self.next_level:
            self.level += 1
            self.xp = 0
            self.next_level += math.floor(self.level * 1.2)
        print(f"Level: {self.level}, XP: {self.xp}, Next Level: {self.next_level}")
        print(f"Resources: {self.resources}")
        print(f"Credits: {self.resources[CREDITS]}")