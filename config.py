import pygame
from constants import *


class Config:
    def __init__(self):
        self.screen_width, self.screen_height = SCREEN_SIZES[2]
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.NOFRAME)
        self.bg_color = BLACK_COLOR

        self.player_radius = PLAYER_RADIUS
        self.player_turn_speed = PLAYER_TURN_SPEED
        self.player_move_speed = PLAYER_MOVE_SPEED
        self.player_shoot_speed = PLAYER_SHOOT_SPEED
        self.player_shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        self.player_color = (0, 128, 0)
        self.shot_radius = SHOT_RADIUS

        self.asteroid_min_radius = 20
        self.asteroid_kinds = 3
        self.asteroid_spawn_rate = 0.8  # seconds
        self.asteroid_max_radius = self.asteroid_min_radius * self.asteroid_kinds 
        self.asteroid_min_velocity = 20
        self.asteroid_max_velocity = 100

        self.weights = [
        (1, 50),
        (2, 25),
        (3, 10),
        (4, 8),
        (5, 4),
        (6, 2),
        (7, 1),
        ]

    def display_mode(self, display_option):
        if display_option == DISPLAY_MODE[0]:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
        if display_option == DISPLAY_MODE[1]:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.NOFRAME | pygame.FULLSCREEN)
        if display_option == DISPLAY_MODE[2]:
            self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.NOFRAME)
    #    if display_option == DISPLAY_MODE[3]:
    #        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))