# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    # Initialize pygame
    pygame.init()

    # Create the game screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Set game clock variable
    clock = pygame.time.Clock()

    
    # Creates groups for all objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Creates containers and assigns groups to the containers
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    # Creates player ship
    player = Player(x = (SCREEN_WIDTH / 2), y = (SCREEN_HEIGHT / 2) )
    
    # Creates asteroid field
    asteroid_field = AsteroidField()

    # Delta time 
    dt = 0


    # Main game loop
    while True:        
        # Closes game if the close buttom (X) is clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # calls the update methods for every object assigned the update group
        # This behavior is dependant on the overwritten update() method in each class
        updatable.update(dt)
        
        # Loop through the asteroids
        for asteroid in asteroids:
            # Check for collision with the ship to end the game
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()       
            
            # Check for collision with bullet and call the split() method for asteroid behavior
            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()
                
        # Paint it black
        screen.fill("black")

        # Draws sprites on top of black screen
        for sprite in drawable:
            sprite.draw(screen)
        
        # Flip causes the updates to be displayed
        pygame.display.flip()

        # Sets the delta time to be independant of CPU clock speeds and changes tick to seconds
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
