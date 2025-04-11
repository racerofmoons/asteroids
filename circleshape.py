import pygame
import random

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collision(self, other):
        if self.position.distance_to(other.position) < self.radius + other.radius:
            return True
        return False

   
#    def asteroid_collision(self, other):
        collision_normal = (self.position - other.position).normalize()
        relative_velocity = self.velocity - other.velocity
        velocity_along_normal = relative_velocity.dot(collision_normal)
        if velocity_along_normal > 0:
            return
        restitution = 1.0
        j = -(1 + restitution * velocity_along_normal) / (1/self.radius + 1/other.radius)
        impulse = collision_normal * j
        self.velocity += impulse / self.radius
        other.velocity -= impulse / other.radius
        jitter = pygame.math.Vector2(random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)).normalize() * 0.1
        self.velocity += jitter
        other.velocity -= jitter  

#    def overlap(self, other):
        overlap = (self.radius + other.radius) - self.position.distance_to(other.position)
        if overlap > 0:
            seperation_vector = (self.position - other.position)
            if seperation_vector.length() != 0:
                seperation_vector = seperation_vector.normalize() * overlap
                correction_factor = min(0.8, max(0.5, overlap * 0.5))
                self.position -= seperation_vector * correction_factor
                other.position += seperation_vector * correction_factor
                
