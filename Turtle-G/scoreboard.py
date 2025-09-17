import pygame

class Scoreboard:
    def __init__(self):
        self.level = 1
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        text_surface = self.font.render(f"Level: {self.level}", True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))

    def increase_level(self):
        self.level += 1

    def game_over(self, screen):
        game_over_text = self.font.render("GAME OVER", True, (255, 255, 255))
        text_rect = game_over_text.get_rect(center=(300, 300))
        screen.blit(game_over_text, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)