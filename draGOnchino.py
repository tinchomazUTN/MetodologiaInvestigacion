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
from pygame.locals import  MOUSEBUTTONUP, QUIT
"""
MOUSEBUTTONUP: Esta constante representa el evento de soltar un botón del mouse.
QUIT: Esta constante representa el evento de salir de la aplicación.
"""

#colores
Negro = (0, 0, 0)
Blanco = (255,255,255)
#color del tablero
ColorTablero = (209, 148, 95)
#posiciones
PosicionesSprites = False

class Spot(pygame.sprite.Sprite):
    def __init__(self, array_indexes, location, size, color):
        super(Spot, self).__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill(color)

        self.location = location
        self.array_indexes = array_indexes
        self.occupied = False
        self.color = None



#Clase Main
class Main:
    def init(self, komi=2.5):
        #inicializar la biblioteca pygame y prepararla para su uso
        pygame.init()
        #Dimensiones de la pantalla
        anchoDePantalla = 1000
        altoDePantalla = 700

        #Asignamos un objeto de Sprites
        self.sprites = pygame.sprite.Group()
        """
        Es una matriz 2D (lista de listas) 
        que se inicializa con 19 filas y 19 columnas. 
        Cada elemento de la matriz se inicializa con el valor 0.
        """
        self.sprite_array = [[0 for _ in range(19)] for _ in range(19)]


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

        #contador de turnos
        self.turno = 0
        # Ventaja del jugador que comienza segundo
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
                            app.iniciar()


    #Iniciar Juego
    def iniciar(self):

        #Generamos las ubicaciones de los Sprites
        self.ubicacionSprites()

        self.addSprites()

        ejecutando = True

        while ejecutando:
            for event in pygame.event.get():
                #Creamos el fondo de la pantalla
                self.screen.fill(ColorTablero)
                #Dibujamos el tabler
                self.dibujarTablero()
                """
                Dibujamos las ubicaciones de los Sprites
                """
                self.dibujarSprites()

                if event.type == MOUSEBUTTONUP:
                    #posición actual del cursor del mouse en la ventana del juego (x,y)
                    pos = pygame.mouse.get_pos()
                    #contiene los sprites del grupo self.sprites con los que el cursor del mouse ha colisionado.
                    clicked_sprites = [sprite for sprite in self.sprites if self.spriteCollided(sprite.location, pos)]

                    #asegurarse de que se ha hecho clic en al menos un sprite
                    if clicked_sprites:
                        clicked_sprite = clicked_sprites[0]

                        #verificar si el sprite clikeado no está ocupado.
                        if not clicked_sprite.occupied:
                            self.turno += 1
                            #colorcirculo es negro si el numero es impar y blanco si es par
                            colorCirculo = Negro if self.turno % 2 else Blanco

                            #obtener las coordenadas x , y de la ubicación del sprite clikeado.
                            x, y = clicked_sprite.location
                            posicion = (x + 1, y)

                            #dibuja un círculo en la pantalla en la posición loc, con un radio de 10 píxeles y utilizando el colo
                            pygame.draw.circle(self.screen, colorCirculo, posicion, 10, 0)

                            clicked_sprite.occupied = True
                            clicked_sprite.color = colorCirculo
                    print()

                elif event.type == QUIT:
                    ejecutando = False

            pygame.display.update()

        pygame.quit()

    def ubicacionSprites(self):
        #lista para las ubicaciones de los sprites
        locations = []

        for y_index, y_pos in enumerate(range(10, 551, 30)):
            for x_index, x_pos in enumerate(range(10, 551, 30)):
                locations.append([[y_index, x_index], [y_pos, x_pos]])

        #se guarda la lista en la variable de clase
        self.locations = locations

    def addSprites(self):
        #rastrear la fila y el índice del elemento en la matriz
        fila = 0
        item = 0

        #iterar a través de las ubicaciones generadas
        for location in self.locations:
            if item >= 19:
                fila += 1
                item = 0
            if fila > 18:
                break

            sprite = Spot(*location, (10, 10), (255, 32, 1))
            #el sprite recién creado se agrega al grupo de sprites
            self.sprites.add(sprite)
            #también se agrega a la matriz
            self.sprite_array[item][fila] = sprite
            #siguiente elemento
            item += 1

    #Metodo para Dibujar el tablero
    def dibujarTablero(self):

        for y_pos in range(10, 551, 30):
            pygame.draw.line(self.screen, Negro, (10, y_pos), (551, y_pos), width=2)

        for x_pos in range(10, 551, 30):
            pygame.draw.line(self.screen, Negro, (x_pos, 10), (x_pos, 551), width=2)

    def dibujarSprites(self):
        for entity in self.sprites:
            if PosicionesSprites:
                self.screen.blit(entity.surf, entity.location)
            if entity.occupied:
                x, y = entity.location
                loc = (x+1, y)
                pygame.draw.circle(self.screen, entity.color, loc, 10, 0)

    def spriteCollided(self, sprite_location, clicked_location):
        sprite_y, sprite_x = sprite_location
        clicked_y, clicked_x = clicked_location

        if sprite_y - 10 < clicked_y < sprite_y + 10:
            if sprite_x - 10 < clicked_x < sprite_x + 10:
                return True

        return False



if __name__ == '__main__':
    app = Main()
    app.pantallaInicio()
    