import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.bounce_timer = 10.0

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

    # check if hit screen edge    
    def out_of_area(self):
        border_x1 = 0
        border_x2 = SCREEN_WIDTH
        border_y1 = 0
        border_y2 = SCREEN_HEIGHT
        if (self.position.x <= border_x1 or self.position.x >= border_x2) or (
            self.position.y <= border_y1 or self.position.y >= border_y2):
            return True
        else:
            return False
    
    # bounce off the screen
    def bounce(self):
        if self.out_of_area() == True and self.bounce_timer <= 0:
            self.velocity *= -1
            self.bounce_timer = 10.0