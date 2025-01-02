import pygame
import pickle
import os

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.x, self.y = 250, 500  # Starting position of the car
        self.width, self.height = 50, 100  # Size of the car
        self.speed = 5  # Movement speed of the car

        # Load the car sprite image
        self.image = pygame.image.load("car.png")  # Adjust path if necessary
        self.image = pygame.transform.scale(self.image, (self.width, self.height))  # Resize the image to match the car size

        # Load saved progress if available
        self.load_progress()

    def update(self):
        keys = pygame.key.get_pressed()

        # Move the car based on keyboard input
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        # Ensure the car doesn't go out of bounds
        self.x = max(0, min(self.x, 500 - self.width))  # Keep the car within screen width
        self.y = max(0, min(self.y, 600 - self.height))  # Keep the car within screen height

    def draw(self, screen):
        # Draw the player (car) sprite
        screen.blit(self.image, (self.x, self.y))  # Draw the car at the specified position

    def increase_score(self):
        """Increase the player's score."""
        self.score += 1

    def save_progress(self):
        """Save the player's progress (score) using pickle."""
        with open(f"{self.name}_progress.pkl", "wb") as file:
            pickle.dump(self.score, file)

    def load_progress(self):
        """Load the player's progress (score) if available using pickle."""
        filename = f"{self.name}_progress.pkl"
        if os.path.exists(filename):
            with open(filename, "rb") as file:
                self.score = pickle.load(file)
        else:
            self.score = 0  # Default score if no saved progress

    def get_score(self):
        """Return the player's score."""
        return self.score

    def reset_position(self):
        """Reset the player's position to the starting point."""
        self.rect.x, self.rect.y = 250, 500  # Reset to starting position
