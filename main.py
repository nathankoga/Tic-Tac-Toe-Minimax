import pygame
import tictactoe_legacy


#  Visual Controller for tictactoe game
def main():
    pygame.init()  # initialize pygame library
    board = tictactoe_legacy.Board()
    screen = pygame.display.set_mode([600, 600])  # Set drawing window (x, y)
    width = screen.get_width()
    height = screen.get_height()

    # Run until quit input
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Set up board visual
        screen.fill((255, 255, 255))  # Fill background with white
        pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 600), 5)  # vertical 1
        pygame.draw.line(screen, (0, 0, 0), (400, 0), (400, 600), 5)  # vertical 2
        pygame.draw.line(screen, (0, 0, 0), (0, 200), (600, 200), 5)  # horizontal 1
        pygame.draw.line(screen, (0, 0, 0), (0, 400), (600, 400), 5)  # horizontal 2

        for row in board.board:
            pass

        # Update Display
        pygame.display.flip()

    # Out of running loop
    pygame.quit()


if __name__ == "__main__":
    main()