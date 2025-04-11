from circleshape import *
from constants import *
from bullet import Bullet

class Player(CircleShape):
    def __init__(self, x, y, radius=PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.color = (0,128,0)
        self.rotation = 0
        self.shoot_timer = 0.0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.triangle(), width=2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVE_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT] or keys[pygame.K_KP4]:
            self.rotate(dt * -1)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] or keys[pygame.K_KP6]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_KP8]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN] or keys[pygame.K_KP2]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE] or keys[pygame.K_KP0]:
            if self.shoot_timer <= 0:
                self.shoot_timer = 0.3
                self.shoot()

    def shoot(self):
        bullet = Bullet(self.position, radius=SHOT_RADIUS)
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED