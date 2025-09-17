import pygame
import random
from car import Car
from player import Player
from scoreboard import Scoreboard

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Turtle Crossing Game")

# Game clock to control frame rate
clock = pygame.time.Clock()

# Create game objects
player = Player()
cars = pygame.sprite.Group()  # Pygame group to manage all car sprites
scoreboard = Scoreboard()

# Game loop
game_is_on = True
while game_is_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()

    # Add new cars at random intervals
    if random.randint(1, 20) == 1:
        new_car = Car()
        cars.add(new_car)

    # Update game objects
    cars.update()

    # Clear screen and draw objects
    screen.fill((52, 73, 94))  # Dark blue background
    cars.draw(screen)
    screen.blit(player.image, player.rect)
    scoreboard.draw(screen)

    # Collision detection
    if pygame.sprite.spritecollideany(player, cars):
        game_is_on = False
        scoreboard.game_over(screen)

    # Check for successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        for car in cars:
            car.increase_speed()
        scoreboard.increase_level()

    pygame.display.flip()
    clock.tick(60)  # 60 frames per second

pygame.quit()