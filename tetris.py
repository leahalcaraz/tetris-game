import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the shapes of the Tetris blocks
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
]

# Initialize the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Function to draw a block on the screen
def draw_block(x, y):
    pygame.draw.rect(screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Function to draw the current piece
def draw_piece(piece, x, y):
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] == 1:
                draw_block(x + j, y + i)

# Function to check if a piece can be placed at a given position
def is_valid_move(piece, x, y, grid):
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if piece[i][j] == 1:
                if x + j < 0 or x + j >= SCREEN_WIDTH // BLOCK_SIZE or y + i >= SCREEN_HEIGHT // BLOCK_SIZE or grid[y + i][x + j] == 1:
                    return False
    return True

# Main game loop
def main():
    clock = pygame.time.Clock()
    grid = [[0] * (SCREEN_WIDTH // BLOCK_SIZE) for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
    piece = random.choice(SHAPES)
    x, y = SCREEN_WIDTH // BLOCK_SIZE // 2 - len(piece[0]) // 2, 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and is_valid_move(piece, x - 1, y, grid):
                    x -= 1
                elif event.key == pygame.K_RIGHT and is_valid_move(piece, x + 1, y, grid):
                    x += 1
                elif event.key == pygame.K_DOWN and is_valid_move(piece, x, y + 1, grid):
                    y += 1

        # Move the piece down automatically
        if is_valid_move(piece, x, y + 1, grid):
            y += 1
        else:
            # Place the piece on the grid and check for completed lines
            for i in range(len(piece)):
                for j in range(len(piece[i])):
                    if piece[i][j] == 1:
                        grid[y + i][x + j] = 1

            # Check for completed lines and clear them
            for i in range(len(grid) - 1, -1, -1):
                if all(grid[i]):
                    del grid[i]
                    grid.insert(0, [0] * (SCREEN_WIDTH // BLOCK_SIZE))

            # Spawn a new piece
            piece = random.choice(SHAPES)
            x, y = SCREEN_WIDTH // BLOCK_SIZE // 2 - len(piece[0]) // 2, 0

        # Draw the background
        screen.fill(BLACK)

        # Draw the grid
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    draw_block(j, i)

        # Draw the current piece
        draw_piece(piece, x, y)

        pygame.display.update()
        clock.tick(5)

if __name__ == "__main__":
    main()
