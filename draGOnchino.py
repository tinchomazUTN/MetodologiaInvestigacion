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
