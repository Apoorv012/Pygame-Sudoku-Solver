# Import Modules
import pygame

# Constants
DIMENSION = 9
CELL_SIZE = 80

# Colors
WHITE = [255, 255, 255]

# Main Game Class
class Game:
    def __init__(self, grid = None):
        self.grid = grid if grid else self.generateGame()
    
    def generateGame(self) -> list:
        pass

    def display(self):
        self.window.fill(WHITE)

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