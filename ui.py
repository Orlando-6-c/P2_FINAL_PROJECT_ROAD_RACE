import pygame
from level import Level

class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)  # Default font

    def show_start_menu(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))  # Black background

            # Dynamically adjust font size for title text
            title_font = pygame.font.Font(None, 48)  # Larger font for title
            start_font = pygame.font.Font(None, 24)  # Smaller font for start instructions

            title_text = title_font.render("Car Race Game", True, (255, 255, 255))
            start_text = start_font.render("Press Enter to Start or Esc to Exit", True, (255, 255, 255))

            # Centering title and start instructions
            title_text_rect = title_text.get_rect(center=(250, 200))  # Title centered at (250, 200)
            start_text_rect = start_text.get_rect(center=(250, 300))  # Start instructions centered at (250, 300)

            # Blit the text onto the screen
            self.screen.blit(title_text, title_text_rect)
            self.screen.blit(start_text, start_text_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None  # Exit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Enter key
                        return "Player1"  # Replace with actual player name input logic
                    if event.key == pygame.K_ESCAPE:  # Escape key
                        return None  # Exit
    
    def show_level_selection(self, levels):
        running = True
        while running:
            self.screen.fill((0, 0, 0))  # Black background
            title_text = self.font.render("Select Level", True, (255, 255, 255))
            self.screen.blit(title_text, (300, 100))

            for idx, level in enumerate(levels):
                # Access the level's attributes directly
                level_text = self.font.render(f"Level {idx + 1}: {level.name}", True, (255, 255, 255))  # Level name
                self.screen.blit(level_text, (200, 200 + idx * 50))  # Adjust y position for each level

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None  # Exit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:  # Select Level 1
                        return levels[0]
                    if event.key == pygame.K_2:  # Select Level 2
                        return levels[1]
                    if event.key == pygame.K_3:  # Select Level 3
                        return levels[2]

                    
    def draw_score(self, score):
        """Display the player's score on the screen."""
        score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))  # White score text
        score_text_rect = score_text.get_rect(topright=(500, 10))  # Position at top-right corner
        self.screen.blit(score_text, score_text_rect)


