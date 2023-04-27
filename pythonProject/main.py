import pygame
import numpy as np
import sys

SCREEN_SIZE = (800, 800)
CELL_SIZE = 40
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BROWN = (205, 133, 63)

def draw_stone(x, y, player):
    if player == 1:
        color = WHITE
    else:
        color = BLACK
    pygame.draw.circle(screen, color, (x*CELL_SIZE, y*CELL_SIZE), CELL_SIZE // 2 - 2)

def draw_board():
    screen.fill(LIGHT_BROWN)
    for i in range(board_size):
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, SCREEN_SIZE[1]))
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (SCREEN_SIZE[0], i * CELL_SIZE))

def get_clicked_cell(pos):
    x, y = pos
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    return row, col

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Go Game")

board_size = SCREEN_SIZE[0] // CELL_SIZE
board = np.zeros((board_size, board_size), dtype=np.int8)
player = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row, col = get_clicked_cell(pos)
            if board[row, col] == 0:
                board[row, col] = player
                draw_stone(col+1,row+1 , player)
                player = 3 - player

    draw_board()

    for row in range(board_size):
        for col in range(board_size):
            if board[row, col] != 0:
                draw_stone(col+1,row+1 , board[row,col])

    pygame.display.update()