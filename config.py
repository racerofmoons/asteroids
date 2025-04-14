import pygame
from constants import *

class Config:
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
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
