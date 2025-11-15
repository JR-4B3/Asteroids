import pygame
import random
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            vel1 = self.velocity.rotate(angle)
            vel2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            v1 = Asteroid(self.position.x, self.position.y, new_radius)
            v2 = Asteroid(self.position.x, self.position.y, new_radius)
            v1.velocity = vel1 * 1.2
            v2.velocity = vel2 * 1.2
            
            
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )
    
    def update(self, dt):
        self.position += self.velocity * dt
        