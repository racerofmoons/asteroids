import pygame
import random
from asteroid import Asteroid
from constants import *
from config import *


class AsteroidField(pygame.sprite.Sprite):
    def left_edge(self):
        return lambda y: pygame.Vector2(self.config.screen_width + self.config.asteroid_max_radius, y * self.config.screen_height)
    def right_edge(self):
        return lambda y: pygame.Vector2(self.config.screen_width + self.config.asteroid_max_radius, y * self.config.screen_height)
    def top_edge(self):
        return lambda x: pygame.Vector2(x * self.config.screen_width, -self.config.asteroid_max_radius)
    def bottom_edge(self):
        return lambda x: pygame.Vector2(x * self.config.screen_width, self.config.screen_height + self.config.asteroid_max_radius)

    edges = [
        [pygame.Vector2(1, 0), left_edge],
        [pygame.Vector2(-1, 0), right_edge],
        [pygame.Vector2(0, 1), top_edge],
        [pygame.Vector2(0, -1), bottom_edge],
    ]

    def __init__(self, config):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.config = config
        self.spawn_timer = 0.0


    def spawn(self, radius, position, velocity):
        position = random.choice(self.edges)[1](self)(random.uniform(0, 1))
        asteroid = Asteroid(position.x, position.y, radius, self.config)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > self.config.asteroid_spawn_rate:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            velocity = (edge[0] * random.randint(self.config.asteroid_min_velocity, self.config.asteroid_max_velocity)).rotate(random.randint(-30, 30))
            position = edge[1](self)(random.uniform(0, 1))
            kind = random.randint(1, self.config.asteroid_kinds)
            self.spawn(self.config.asteroid_min_radius * kind, position, velocity)