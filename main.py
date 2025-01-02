import pygame
from player import Player
from level import Level
from ui import UI

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption("Car Race Game")

    clock = pygame.time.Clock()
    ui = UI(screen)  # Initialize the UI
    player_name = ui.show_start_menu()  # Show start menu

    if not player_name:
        pygame.quit()
        return

    player = Player(player_name)
    selected_level = ui.show_level_selection(Level.get_levels())  # Show levels

    if not selected_level:
        pygame.quit()
        return

    # Directly use selected_level (which is already a Level object)
    level = selected_level  # No need to index or unpack, it's already the Level object

    level.generate_obstacles()  # Generate obstacles for the level

    running = True
    paused = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused

        if paused:
            ui.draw_pause_menu()
            pygame.display.flip()
            continue

        # Game logic and rendering
        screen.fill((0, 0, 0))  # Clear screen
        player.update()  # Update player position
        level.update_obstacles()  # Update obstacles' position
        level.check_collisions(player)  # Check for collisions
        ui.draw_score(player.score)  # Draw score

        # Draw obstacles on the screen
        for obstacle in level.obstacles:
            obstacle.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
