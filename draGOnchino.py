import pygame,sys
# Constantes
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
CELL_SIZE = 50
BOARD_SIZE = 9
SCREEN_SIZE = (CELL_SIZE * BOARD_SIZE, CELL_SIZE * BOARD_SIZE)
FPS = 30

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()


# Funciones
def draw_board():
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            color = WHITE
            if (x + y) % 2 == 0:
                color = GRAY
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_piece(x, y, color):
    pygame.draw.circle(screen, color, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 5)