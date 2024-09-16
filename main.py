import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    player_shots = pygame.sprite.Group()

    Shot.containers = (player_shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    dt = 0
    score = 0
    lives = 3

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # updates all objects
        for obj in updatable:
            obj.update(dt)

        # check for collision
        for asteroid in asteroids:
            if asteroid.collision_with(player):
                if lives == 1:
                    print(f"Game over! With a Score of {score}")
                    sys.exit()
                lives -= 1
                player.kill()
                player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                for asteroid in asteroids:
                    asteroid.kill()

            for shot in player_shots:
                if asteroid.collision_with(shot):
                    score = asteroid.add_score(score)
                    asteroid.split()
                    shot.kill()
                if shot.out_of_area == True:
                    shot.kill()

        screen.fill("black")

        # spawns objects
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()