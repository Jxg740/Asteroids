import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    # overwrites the default draw() from circlshape
    def draw(self, screen):
        # args are (surface, color, center, radius, width)
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)  
