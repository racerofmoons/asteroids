import random
import math
from constants import *
from circleshape import *


class Asteroid(CircleShape):
    colors = {
        1: (194,178,128), # Sand -- Silica
        2: (185,78,72), # Deep Chestnut -- Iron
        3: (145,163,176), # Cadet Grey -- Aluminum
        4: (176,196,222), # Light Steel Blue -- Cobalt
        5: (218,165,32), # Goldenrod -- Gold
        6: (173,255,47), # Green Yellow -- Uranium
        7: (135,206,235), # Sky Blue -- Thorium
        }
    weights = [
        (1, 50),
        (2, 25),
        (3, 10),
        (4, 5),
        (5, 2),
        (6, 1),
        (7, 0.5),
    ]

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.verticies = self.lumpy_shape()
        self.tier = self.select_tier()
        self.color = self.colors[self.tier]
        self.value = 2 * self.tier # also updated in the .split() method

    def select_tier(self):
        tiers, weights = zip(*self.weights)
        total = sum(weights)
        normalized_weights = [w/total for w in weights]
        return random.choices(tiers, normalized_weights, k=1)[0]

    def draw(self, screen):
        screen_vertecies = []
        for vx, vy in self.verticies:
            screen_vertecies.append((self.position.x + vx, self.position.y + vy))
        pygame.draw.polygon(screen, self.color, screen_vertecies, width=2)
        pygame.draw.circle(screen, (0, 255, 0), (int(self.position.x), int(self.position.y)), 5)
        
    def update(self, dt):
        self.position += self.velocity * dt
        if self.collision_timer > 0:
            self.collision_timer -= dt

    def split(self, collider_type):
        if collider_type == "asteroid" and self.collision_timer > 0:
            return
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return self.tier
        angle = random.uniform(22, 66)
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)
        new_radius = self.radius / 2
        asteroid1 = self.fragment(self.position, new_radius, vector1)
        asteroid2 = self.fragment(self.position, new_radius, vector2)
        return asteroid1, asteroid2

    def fragment(self, position, radius, vector):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = vector * 1.2
        asteroid.collision_timer = 0.7
        asteroid.tier = self.tier
        asteroid.color = self.color
        asteroid.value = 2 * self.tier
        return asteroid


    def lumpy_shape(self, radius=None, num_verticies=None):
        if radius is None:
            radius = self.radius
        if num_verticies is None:
            num_verticies = random.randint(8, 20)
        vertecies = []
        for i in range(num_verticies):
            angle = (i / num_verticies) * (2 * math.pi)
            random_radius = radius * random.uniform(0.4, 1)
            vertecies.append((
                random_radius * math.cos(angle), 
                random_radius * math.sin(angle)
            ))
        return vertecies
    
