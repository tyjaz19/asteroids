import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # draw asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    # everytime update function called move asteroid
    def update(self, dt):
        self.position += self.velocity * dt

    