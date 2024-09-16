import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # draw asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    # everytime update function called move asteroid
    def update(self, dt):
        self.position += self.velocity * dt
        self.bounce_timer -= dt
        self.bounce()

    # split the asteroid
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        Vector1 = pygame.math.Vector2.rotate(self.velocity, angle)
        Vector2 = pygame.math.Vector2.rotate(self.velocity, -angle)
        self.radius -= ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)
        asteroid1.velocity = Vector1 * 1.2
        asteroid2.velocity = Vector2

    def add_score(self, Score):
        if self.radius <= ASTEROID_MIN_RADIUS:
            Score += 1
            return Score
        elif self.radius == ASTEROID_MAX_RADIUS:
            Score += 3
            return Score
        else:
            Score += 2
            return Score
