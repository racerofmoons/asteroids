from constants import *
from circleshape import *

class Bullet(CircleShape):
    def __init__(self, position, radius):
        super().__init__(position.x, position.y, radius)
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt