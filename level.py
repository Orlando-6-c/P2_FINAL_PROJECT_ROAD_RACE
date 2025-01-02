import pygame
import random

class Level:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.obstacles = []  # List to hold obstacle objects

        # Load obstacle sprite
        self.obstacle_image = pygame.image.load("obstacle.png")  # Adjust path if necessary
        self.obstacle_image = pygame.transform.scale(self.obstacle_image, (50, 50))  # Resize obstacle

    def generate_obstacles(self):
        """Generate obstacles based on the level's difficulty."""
        self.obstacles = []
        for i in range(self.difficulty * 5):  # Difficulty affects the number of obstacles
            x = random.randint(0, 450)  # Random x position (avoid edges)
            y = random.randint(-600, -50)  # Random y position off-screen (obstacles start above)
            self.obstacles.append(Obstacle(x, y, self.obstacle_image))

    def update_obstacles(self):
        """Update obstacles' positions and reset if they go off-screen."""
        for obstacle in self.obstacles:
            obstacle.y += 5  # Move down
            if obstacle.y > 600:  # Reset if off the screen
                obstacle.y = random.randint(-200, -50)
                obstacle.x = random.randint(0, 450)

    def check_collisions(self, player):
        """Check for collisions between player and obstacles."""
        for obstacle in self.obstacles:
            if pygame.Rect(player.x, player.y, player.width, player.height).colliderect(obstacle.rect):
                # Handle collision (e.g., end game or reduce score)
                print("Collision Detected!")

    @staticmethod
    def get_levels():
        """Return a list of available levels."""
        return [
            Level("Easy", 1),
            Level("Medium", 2),
            Level("Hard", 3)
        ]


class Obstacle:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        """Draw the obstacle to the screen."""
        screen.blit(self.image, (self.x, self.y))
