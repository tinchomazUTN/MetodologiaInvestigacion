import os
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, MOUSEBUTTONUP, QUIT, K_p


Blanco = (255, 255, 255)
ColorTablero = (209, 148, 95)
Negro = (0, 0, 0)
mostrar_hitboxes = False

class Main:
    def init(self, komi=2.5):
        pygame.init()
        anchoDePantalla = 1000
        altoDePantalla = 700

        self.screen = pygame.display.set_mode((anchoDePantalla, altoDePantalla))

        if os.path.exists('./iconFile.png'):
            pygame.display.set_icon(pygame.image.load('./iconFile.png'))

        self.move = 0
        self.white_move = False
        self.passed_in_a_row = 0
        self.gameover = False
        self.komi = komi

#Pantalla de Inicio del juego
    def pantallaInicio(self):
        pygame.init()
        screen = pygame.display.set_mode((1000, 700))
        #Imagen de Fondo
        background_image = pygame.image.load("lib/dragones.jpg").convert()
        background_image = pygame.transform.scale(background_image, (1000, 700))

        # Boton
        button_image = pygame.image.load("lib/boton.png").convert_alpha()
        button_image = pygame.transform.scale(button_image, (250, 100))
        button_rect = button_image.get_rect()
        button_rect.x = (screen.get_width() - button_rect.width) // 2
        button_rect.y = 550

        screen.blit(background_image, (0, 0))
        screen.blit(button_image, button_rect)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        if __name__ == '__main__':
                            app = Main()
                            app.init()
                            app.Iniciar()


    #Iniciar Juego
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


    #Metodo para Dibujar el tablero
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
    app = Main()
    app.pantallaInicio()
