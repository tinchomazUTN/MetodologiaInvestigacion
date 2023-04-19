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
    def get_cell(pos):
    x, y = pos
    cell_x, cell_y = x // CELL_SIZE, y // CELL_SIZE
    if cell_x >= BOARD_SIZE or cell_y >= BOARD_SIZE:
        return None
    return (cell_x, cell_y)

# Tablero
board = [[None for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

# Bucle principal
while True:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            cell = get_cell(pos)
            if cell is not None:
                x, y = cell
                board[x][y] = BLACK
                

 # Dibujar el tablero y las piezas
    draw_board()
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if board[x][y] == BLACK:
                draw_piece(x, y, BLACK)
            elif board[x][y] == WHITE:
                draw_piece(x, y, WHITE)

    # Actualizar pantalla
    pygame.display.flip()

    # Esperar un tiempo para mantener una tasa de FPS constante
    clock.tick(FPS)               