import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player (CircleShape):
    def __init__(self, x, y, radius, shots_group):
        super().__init__(x, y, radius)  
        self.rotation = 0
        self.shots = shots_group
        self.cooldown = 0

    def rotate (self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def move (self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot (self):
        shot = Shot(self.position.x, self.position.y)
        direction = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot.velocity = direction
        self.shots.add(shot)
    
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        dt_neg = dt * -1
        self.cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(dt_neg)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_s]:
            self.move(dt_neg)

        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_SPACE]:
            if self.cooldown > 0:
                pass
            else:
                self.shoot()
                self.cooldown = PLAYER_SHOOT_COOLDOWN