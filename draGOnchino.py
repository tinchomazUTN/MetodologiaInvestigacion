import os
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, MOUSEBUTTONUP, QUIT, K_p


Blanco = (255, 255, 255)
ColorTablero = (209, 148, 95)
Negro = (0, 0, 0)
mostrar_hitboxes = False

class Main:
    def __init__(self, komi=2.5):
        pygame.init()
        anchoDePantalla = 563
        altoDePantalla = 563

        self.screen = pygame.display.set_mode((anchoDePantalla, altoDePantalla))

        if os.path.exists('./iconFile.png'):
            pygame.display.set_icon(pygame.image.load('./iconFile.png'))

        self.move = 0
        self.white_move = False
        self.passed_in_a_row = 0
        self.gameover = False
        self.komi = komi


    def Iniciar(self):
        Ejecutando = True

        while Ejecutando:
            for event in pygame.event.get():
                self.screen.fill(ColorTablero)
                self.DibujarTablero()

                if event.type == QUIT:
                    Ejecutando = False

            pygame.display.update()

        pygame.quit()

    def DibujarTablero(self):
        for y_pos in range(10, 551, 30):
            pygame.draw.line(self.screen, Negro, (10, y_pos), (551, y_pos), width=2)

        for x_pos in range(10, 551, 30):
            pygame.draw.line(self.screen, Negro, (x_pos, 10), (x_pos, 551), width=2)

        star_spots = \
            [
                (100, 100),
                (100, 280),
                (100, 460),

                (280, 100),
                (280, 280),
                (280, 460),

                (460, 100),
                (460, 280),
                (460, 460)
            ]


if __name__ == '__main__':
    app = Main(komi=2.5)
    app.Iniciar()
