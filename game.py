# Import Modules
import pygame
from pygame import Vector2

# Constants
DIMENSION = 9
CELL_SIZE = 60

# Colors
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]


def draw_thick_line(pos1: Vector2, pos2: Vector2, window: pygame.surface.Surface, thickness: Vector2):
    points = [pos1 + thickness, pos2 + thickness, pos2 - thickness, pos1 - thickness]
    pygame.draw.polygon(window, BLACK, points)


# Main Game Class
class Game:
    def __init__(self, grid = None):
        self.grid = grid if grid else self.generateGame()
    
    def generateGame(self) -> list:
        pass

    def display(self):
        self.window.fill(WHITE)

        for row in range(1, DIMENSION):
            if row % 3:
                pygame.draw.line(self.window, BLACK, Vector2(0, row * CELL_SIZE), \
                    Vector2(DIMENSION * CELL_SIZE, row * CELL_SIZE))
            else:
                draw_thick_line(Vector2(0, row * CELL_SIZE), Vector2(DIMENSION * CELL_SIZE, row * CELL_SIZE), self.window, Vector2(0, 3))
        
        for col in range(1, DIMENSION):
            if col % 3:
                pygame.draw.line(self.window, BLACK, Vector2(col * CELL_SIZE, 0), \
                    Vector2(col * CELL_SIZE, DIMENSION * CELL_SIZE))
            else:
                draw_thick_line(Vector2(col * CELL_SIZE, 0), Vector2(col * CELL_SIZE, DIMENSION * CELL_SIZE), self.window, Vector2(3, 0))

        pygame.display.update()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

    def run(self):
        self.window = pygame.display.set_mode((DIMENSION * CELL_SIZE, DIMENSION * CELL_SIZE))
        pygame.display.set_caption("Sudoku Solver")

        self.running = True
        while self.running:
            self.update()
            self.display()