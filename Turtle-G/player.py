import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load the image of a turtle
        self.image = pygame.image.load("turtle.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect(center=(300, 570))

    def move_up(self):
        self.rect.y -= 30

    def go_to_start(self):
        self.rect.center = (300, 570)

    def is_at_finish_line(self):
        return self.rect.y < 30