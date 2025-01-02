import pygame

class Car:
    def __init__(self, x, y, sprite_path="car.png"):
        self.x = x
        self.y = y
        self.speed = 5
        self.sprite = pygame.image.load(sprite_path)
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

    def move_left(self):
        """Move the car to the left."""
        self.x -= self.speed

    def move_right(self):
        """Move the car to the right."""
        self.x += self.speed

    def draw(self, screen):
        """Draw the car on the screen."""
        screen.blit(self.sprite, (self.x, self.y))

    def get_rect(self):
        """Get the rectangle representing the car's position and size."""
        return pygame.Rect(self.x, self.y, self.width, self.height)
