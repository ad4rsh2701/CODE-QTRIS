import pygame
import sys
from qtromino import Tetromino, SHAPES
from qr_code import generate_qr_code

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 800
BG_COLOR = (0, 0, 0)
FPS = 60

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CODE QTRIS')

# Generate and load QR code
generate_qr_code('https://example.com')
qr_code_img = pygame.image.load("assets/qr_code.png")

# Resize QR code to fit within the screen dimensions
qr_code_width, qr_code_height = qr_code_img.get_size()
scale_factor = min(WIDTH / qr_code_width, HEIGHT / qr_code_height)
new_size = (int(qr_code_width * scale_factor), int(qr_code_height * scale_factor))
qr_code_img = pygame.transform.scale(qr_code_img, new_size)

# Position the QR code in the middle, slightly lower
qr_code_x = (WIDTH - new_size[0]) // 2
qr_code_y = (HEIGHT - new_size[1]) // 2 + 50  # Adjust the +50 value as needed to position it lower

# Create Tetromino
current_tetromino = Tetromino(SHAPES[4], WIDTH // 2, 0)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_tetromino.move(-15, 0)
            elif event.key == pygame.K_RIGHT:
                current_tetromino.move(15, 0)
            elif event.key == pygame.K_DOWN:
                current_tetromino.move(0, 15)
            elif event.key == pygame.K_UP:
                current_tetromino.rotate()

    # Clear screen
    screen.fill(BG_COLOR)
    
    # Draw QR code background
    screen.blit(qr_code_img, (qr_code_x, qr_code_y))

    # Draw current Tetromino
    current_tetromino.draw(screen)

    # Refresh screen
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
