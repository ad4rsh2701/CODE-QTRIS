import numpy as np
import pygame

# Define Tetromino shapes
SHAPES = [
    np.array([[1, 1, 1, 1]]),  # I
    np.array([[1, 1, 1], [0, 1, 0]]),  # T
    np.array([[1, 1], [1, 1]]),  # O
    np.array([[0, 1, 1], [1, 1, 0]]),  # S
    np.array([[1, 1, 0], [0, 1, 1]]),  # Z
    np.array([[1, 1, 1], [1, 0, 0]]),  # L
    np.array([[1, 1, 1], [0, 0, 1]])   # J
]

class Tetromino:
    def __init__(self, shape, x, y):
        self.shape = shape
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        self.shape = np.rot90(self.shape)

    def draw(self, surface, color=(255, 255, 255)):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(surface, color, (self.x + x * 15, self.y + y * 15, 15, 15))
