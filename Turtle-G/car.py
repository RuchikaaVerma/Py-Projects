import pygame
import random

CAR_IMAGES = [
    "red_car.png",
    "blue_car.png",
    "yellow_car.png"
]
MOVE_SPEED = 5

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load a random car image
        image_path = random.choice(CAR_IMAGES)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 30))
        self.rect = self.image.get_rect(x=600, y=random.randint(150, 450))
        self.speed = MOVE_SPEED

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()  # Remove car when it's off-screen

    def increase_speed(self):
        self.speed += 1