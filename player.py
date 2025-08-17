import pygame
from circleshape import CircleShape
from constants import *
from shot import *

class Player(CircleShape) :
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # overwrites the default draw() from circlshape
    def draw(self, screen):
        # args are (surface, color, points, width) points calls the info from the triangle method
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        # Updates all player sprites based on input

        # Updates the shot cooldown
        self.shoot_timer -= dt

        # Set input variable
        keys = pygame.key.get_pressed()

        # Set all movement inputs
        if keys[pygame.K_a]:
            self.rotate((-dt))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        
        # Shoot weapon
        if keys[pygame.K_SPACE]:
            # calls shoot()
            self.shoot()
            
        

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # Checks if the shot cooldown has reset, then sets it to 0.3
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN        
        # set a variable that calls an instance of Shot and passes the x and Y (I forgot to include the coordinates the first time)
        shot = Shot(self.position.x, self.position.y)        
        # sets the velocity
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        

