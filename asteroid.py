import pygame
import random
from circleshape import CircleShape
from constants import *




class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # overwrites the default draw() from circlshape
    def draw(self, screen):
        # args are (surface, color, center, radius, width)
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        # Destroys current asteroid
        self.kill()
        # Checks if the radius is already the smallest and does nothing if True
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Set random angle for vector
        random_angle = random.uniform(20, 50)

        # Creates two opposite vectors for the new asteroids
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)

        # Set the new smaller size for the asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Creates new asteroid objects with the new radius
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)        
        new_asteroid2 =Asteroid(self.position.x, self.position.y, new_radius)

        # Sets the new velocity and direction of the asteroids
        new_asteroid1.velocity = vector1 * 1.2
        new_asteroid2.velocity = vector2 * 1.2
        
        

    
