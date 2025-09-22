import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from player import Player, Shot
from asteroids import Asteroid
from asteroidfield import AsteroidField
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shooting = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers =(shooting, updatable, drawable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        dt = clock.tick(60) / 1000 
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                exit()
            for bullet in shooting:
                if asteroid.collision(bullet):
                    asteroid.split()
                    bullet.kill()
            


        
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
        
 
    


if __name__ == "__main__":
    main()
