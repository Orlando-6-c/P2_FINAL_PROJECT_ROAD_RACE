import pygame
import random

class Obstacle:
    def __init__(self, x, y, sprite_path="obstacle.png"):
        self.x = x
        self.y = y
        self.speed = random.randint(3, 7)
        self.sprite = pygame.image.load(sprite_path)
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

    def move(self):
        """Move the obstacle downwards."""
        self.y += self.speed

    def draw(self, screen):
        """Draw the obstacle on the screen."""
        screen.blit(self.sprite, (self.x, self.y))

    def is_off_screen(self, screen_height):
        """Check if the obstacle has moved off the screen."""
        return self.y > screen_height

    def get_rect(self):
        """Get the rectangle representing the obstacle's position and size."""
        return pygame.Rect(self.x, self.y, self.width, self.height)
