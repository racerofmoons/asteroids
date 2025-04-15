import pygame
import math
import pickle
import time
import os
from constants import *
from config import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet
from menu import Menu


class Game:
    def __init__(self, config, menu):
        self.config = config
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.menu = menu
        self.resources = [
            0, # 0 credits
            0, # 1 silica
            0, # 2 iron
            0, # 3 aluminum
            0, # 4 cobalt
            0, # 5 gold
            0, # 6 uranium
            0, # 7 thorium
            1, # 8 level
            0, # 9 xp
            10, # 10 xp to next_level
            ]


        self.level = 8
        self.xp = 9
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
        
        self.player = Player(self.config.screen_width / 2, self.config.screen_height / 2)
        self.asteroid_field = AsteroidField(self.config)
        
    def reset_resources(self):
        self.resources = [
            0, # 0 credits
            0, # 1 silica
            0, # 2 iron
            0, # 3 aluminum
            0, # 4 cobalt
            0, # 5 gold
            0, # 6 uranium
            0, # 7 thorium
            1, # 8 level
            0, # 9 xp
            10, # 10 xp to next_level
        ]

    def reset_all(self):
        self.reset_resources()
        self.player.reset_upgrades()



    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
        self.event_handler(keys=pygame.key.get_pressed())
        if self.is_paused:
            self.pause_overlay()
            return "PLAYING"
        
        self.is_running = True
        self.config.screen.fill(BLACK_COLOR)
        self.updatable.update(self.dt)
        if self.player.shoot_timer > 0:
            self.player.shoot_timer -= self.dt

        for object in self.drawable:
            object.draw(self.config.screen)

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
        return "PLAYING"

    def fps_helper(self):
        pygame.display.flip()
        self.dt = (self.clock.tick(FPS) / 1000)

    def draw_game_state(self):
        self.config.screen.fill(BLACK_COLOR)
        for object in self.drawable:
            object.draw(self.config.screen)

    def event_handler(self, keys):
        if keys[pygame.K_ESCAPE]:
            self.is_paused = not self.is_paused
            pygame.time.delay(200)

    def pause_overlay(self):
        self.draw_game_state()
        self.menu.pause_menu(self.resources)


    def pause_menu_starter(self):
        def pause_menu_pre_render():
            self.draw_game_state()
            self.event_handler(keys=pygame.key.get_pressed())
            self.menu.draw_score_table(self.resources)



    def reset_run(self, config):
        self.all_sprites.empty()
        self.drawable.empty()
        self.updatable.empty()
        self.asteroids.empty()
        self.bullets.empty()

        self.all_sprites = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.updatable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        Player.containers = (self.all_sprites, self.drawable, self.updatable)
        Asteroid.containers = (self.all_sprites, self.asteroids, self.updatable, self.drawable)
        AsteroidField.containers = (self.all_sprites, self.updatable)
        Bullet.containers = (self.all_sprites, self.bullets, self.updatable, self.drawable)

        self.player = Player(self.config.screen_width / 2, self.config.screen_height / 2)
        self.asteroid_field = AsteroidField(config)


    def score_keeper(self, target_tier):
        tier = max(0, min(target_tier, len(self.resources) - 1))
        self.resources[target_tier] += 1
        self.resources[self.xp] += target_tier
        self.resources[CREDITS] += target_tier * 2
        if self.resources[self.xp] >= self.resources[self.next_level]:
            self.resources[self.level] += 1
            self.resources[self.xp] = 0
            self.resources[self.next_level] += math.floor(self.resources[self.level] * 1.2)
        print(f"Level: {self.resources[self.level]}, XP: {self.resources[self.xp]}, Next Level: {self.resources[self.next_level]}")
        print(f"Resources: {self.resources}")
        print(f"Credits: {self.resources[CREDITS]}")

    def save_game(self):
        save_data = {
            'resources': self.resources,
            'save_data': time.time(),
        }
        try:
            with open(SAVE_FILE, "wb") as save_file:
                pickle.dump(save_data, save_file)
        except Exception as e:
            print(f"Error saving game: {e}")

    def load_game(self):
        try:
            with open(SAVE_FILE, "rb") as file:
                save_data = pickle.load(file)
                self.resources = save_data['resources']
            print("Game loaded successfully.")
            return True
        except Exception as e:
            print(f"Error loading game: {e}")
            return False
