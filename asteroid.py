import random

import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_COLOR
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.position = pygame.Vector2(self.x, self.y)
        self.shape = self.generate_shape()
    
    def generate_shape(self):
        num_verts = random.randint(7, 11)
        points = []
        for i in range(num_verts):
            # spread vertices unevenly around the circle
            angle = (360 / num_verts) * i + random.uniform(-20, 20)
            # vary radius a lot for a chunky, blocky feel
            r = self.radius * random.uniform(0.65, 1.0)
            points.append((angle, r))
        return points

    def draw(self, screen):
        world_points = []
        for angle, r in self.shape:
            offset = pygame.Vector2(0, 1).rotate(angle) * r
            world_points.append(self.position + offset)
        pygame.draw.polygon(screen, (0, 200, 70), world_points, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
        return super().update(dt)
    
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_rotation = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = self.velocity.rotate(new_rotation) * 1.2
        a2.velocity = self.velocity.rotate(-new_rotation) * 1.2