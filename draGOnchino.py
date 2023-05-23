"""
importación del módulo os,
es útil cuando necesitamos interactuar con el sistema operativo en el que se ejecuta el proyecto,
permitiéndote realizar operaciones relacionadas con
archivos, directorios, variables de entorno y ejecución de comandos del sistema.
"""
import os
"""
Esto importa todo el módulo pygame,
lo que te permite acceder a todas las funciones, 
clases y constantes proporcionadas por la biblioteca.
"""
import pygame
#constantes para eventos, teclas y botones del mouse.
from pygame.locals import K_ESCAPE, KEYDOWN, MOUSEBUTTONUP, QUIT, K_p
"""
K_ESCAPE: Esta constante representa la tecla "Escape" en el teclado.
KEYDOWN: Esta constante representa el evento de presionar una tecla en el teclado.
MOUSEBUTTONUP: Esta constante representa el evento de soltar un botón del mouse.
QUIT: Esta constante representa el evento de salir de la aplicación.
K_p: representa la tecla "P" en el teclado.
"""

#color de linea de tablero
Negro = (0, 0, 0)
#color de tablero
ColorTablero = (209, 148, 95)

#Clase Main
class Main:
    def init(self, komi=2.5):
        #inicializar la biblioteca pygame y prepararla para su uso
        pygame.init()
        #Dimensiones de la pantalla
        anchoDePantalla = 1000
        altoDePantalla = 700
        #creación de una ventana de visualización
        self.screen = pygame.display.set_mode((anchoDePantalla, altoDePantalla))
        #La siguiente linea indica el turno de cada jugador
        pygame.display.set_caption('PELEA! | Comienza Dragon Negro')
        """
        La funcion para indicar el turno aun no esta implementada en su totalidad,
        para turnar los dialogos usaremos una sintaxis como esta:
        JUGADOR = 'Dragon Negro' if not self.move % 2 else 'Dragon Blanco'
        pygame.display.set_caption('PELEA! | Es turno de {JUGADOR}'')
        """
        # Si el archivo existe, se carga como icono de la ventana de visualización
        if os.path.exists('./iconFile.png'):
            pygame.display.set_icon(pygame.image.load('./iconFile.png'))
        #Ventaja del jugador que comienza segundo
        self.komi = komi

    #Pantalla de Inicio del juego
    def pantallaInicio(self):
        # inicializar la biblioteca pygame y prepararla para su uso
        pygame.init()
        # Dimension de la pantalla de inicio
        screen = pygame.display.set_mode((1000, 700))
        #Imagen inicial de fondo
        background_image = pygame.image.load("lib/dragones.jpg").convert()
        background_image = pygame.transform.scale(background_image, (1000, 700))

        #Boton
        button_image = pygame.image.load("lib/boton.png").convert_alpha()
        button_image = pygame.transform.scale(button_image, (250, 100))

        #objeto rectángulo que representa las dimensiones y la posición del botón en la interfaz gráfica.
        button_rect = button_image.get_rect()
        #establece la posición horizontal (x) del rectángulo
        button_rect.x = (screen.get_width() - button_rect.width) // 2
        #establece la posición vertical (y) del rectángulo
        button_rect.y = 550

        #renderizar la imagen de fondo
        screen.blit(background_image, (0, 0))
        #renderiza la imagen del botón
        screen.blit(button_image, button_rect)
        #actualizar la pantalla, mostrando los cambios realizados
        pygame.display.flip()

        #Bucle de pantalla de inicion para capturar los eventos del teclado o mouse
        while True:
            for event in pygame.event.get():
                #Si se presiona el boton de salir(X) se cierra el juego
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    """
                    Se determina si el evento esta sobre la posicion del boton,
                    para iniciar el juego
                    """
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
                #Creamos el fondo de la pantalla
                self.screen.fill(ColorTablero)
                #Dibujamos el tabler
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




if __name__ == '__main__':
    app = Main()
    app.pantallaInicio()
    