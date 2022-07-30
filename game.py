# Import Modules
import pygame
from pygame import Vector2
import os

# Initialization
pygame.init()

# Constants
DIMENSION = 9
CELL_SIZE = 60
FONT_NAME = os.path.join("Assets", "Fonts", "PlatNomor.otf")

# Colors
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]


def draw_thick_line(pos1: Vector2, pos2: Vector2, window: pygame.surface.Surface, thickness: Vector2):
    points = [pos1 + thickness, pos2 + thickness, pos2 - thickness, pos1 - thickness]
    pygame.draw.polygon(window, BLACK, points)


# Main Game Class
class Game:
    def __init__(self, grid = None, difficulty = 80):
        self.grid = grid if grid else self.generateGame(difficulty)
    
    def generateGame(self, difficulty) -> list:
        pass

    def display(self):
        self.window.fill(WHITE)
        self.draw_grid()
        self.show_numbers()

        pygame.display.update()

    def draw_grid(self):
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

    def show_numbers(self):
        for y in range(DIMENSION):
            for x in range(DIMENSION):
                if self.grid[y][x] == 0:
                    continue
                num = self.font.render(str(self.grid[y][x]), True, BLACK)
                num_rect = num.get_rect()
                num_rect.center = (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2)
                self.window.blit(num, num_rect)


        num = "1"
        num_obj = self.font.render(num, True, BLACK)
        num_rect = num_obj.get_rect()
        num_rect.center = (CELL_SIZE // 2, CELL_SIZE // 2)
        self.window.blit(num_obj, num_rect)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

    def run(self):
        self.window = pygame.display.set_mode((DIMENSION * CELL_SIZE, DIMENSION * CELL_SIZE))
        pygame.display.set_caption("Sudoku Solver")

        self.font = pygame.font.Font(FONT_NAME, 32)

        self.running = True
        while self.running:
            self.update()
            self.display()