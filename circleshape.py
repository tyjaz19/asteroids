import pygame
import random
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.bounce_timer = ASTEROID_BOUNCE_RATE

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    # check for collision
    def collision_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius
    
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
            self.velocity *= -random.uniform(0.5, 1.5)
            self.bounce_timer = ASTEROID_BOUNCE_RATE