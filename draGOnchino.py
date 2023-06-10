"""
Esto importa todo el módulo pygame,
lo que te permite acceder a todas las funciones,
clases y constantes proporcionadas por la biblioteca.
"""
import pygame
# constantes para eventos, teclas y botones del mouse.
from pygame.locals import MOUSEBUTTONDOWN,MOUSEBUTTONUP, QUIT,K_ESCAPE, KEYDOWN, K_p
import numpy as np
import time
import random
"""
MOUSEBUTTONUP: Esta constante representa el evento de soltar un botón del mouse.
QUIT: Esta constante representa el evento de salir de la aplicación.
"""

# colores
Negro = (0, 0, 0)
Blanco = (255,255,255)
#color del tablero
ColorTablero = (125,125,125)
sp= 33
alt=608

class nuevoSprite(pygame.sprite.Sprite):
    def __init__(self, array_indexes, location, size, color):
        super(nuevoSprite, self).__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
        self.location = location
        self.array_indexes = array_indexes
        self.occupied = False
        self.color = None

# Clase Main
def pantallaInicio():
    # inicializar la biblioteca pygame y prepararla para su uso
    pygame.init()
    pygame.mixer.get_init()
    # Dimension de la pantalla de inicio
    screen = pygame.display.set_mode((1100, 630))
    #Imagen inicial de fondo
    background_image = pygame.image.load("lib/portada.png").convert()
    background_image = pygame.transform.scale(background_image, (1100, 630))
# Boton jcj
    botonImagen = pygame.image.load("lib/boton.png").convert_alpha()
    botonImagen = pygame.transform.scale(botonImagen,(213,66))
    # objeto rectángulo que representa las dimensiones y la posición del botón en la interfaz gráfica.
    botonJ = botonImagen.get_rect()
    # establece la posición horizontal (x) del rectángulo
    botonJ.x = (screen.get_width() - botonJ.width) // 2
    # establece la posición vertical (y) del rectángulo
    botonJ.y = 400
# Boton BOT
    button_image = pygame.image.load("lib/boton.png").convert_alpha()
    button_image = pygame.transform.scale(button_image, (213,66))
    # objeto rectángulo que representa las dimensiones y la posición del botón en la interfaz gráfica.
    botonBot = button_image.get_rect()
    # establece la posición horizontal (x) del rectángulo
    botonBot.x = (screen.get_width() - botonBot.width) // 2
    # establece la posición vertical (y) del rectángulo
    botonBot.y = 500
    # renderizar la imagen de fondo
    screen.blit(background_image, (0, 0))
    # renderiza la imagen del botón Bot
    screen.blit(button_image, botonBot)
    # renderiza la imagen del botón Jugador
    screen.blit(botonImagen, botonJ)
    # actualizar la pantalla, mostrando los cambios realizados
    pygame.display.flip()
    #Musica menu principal
    musicaInicio = pygame.mixer.music
    musicaInicio.load('lib/Sonido/musica_inicio.mp3')
    musicaInicio.play(-1)
    musicaInicio.set_volume(0.05)

    #Bucle de pantalla de inicio para capturar los eventos del teclado o mouse
    Ejecutando = True
    while Ejecutando:
        for event in pygame.event.get():

            # Si se presiona el boton de salir(X) se cierra el juego
            if event.type == pygame.QUIT:
                Ejecutando = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Ejecutando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                """
                Se determina si el evento esta sobre la posicion del boton,
                para iniciar el juego
                """
                if botonJ.collidepoint(event.pos):
                    if __name__ == '__main__':
                        musicaInicio.stop()
                        aplicacion = Main()
                        aplicacion.init()
                        aplicacion.iniciar()
                if botonBot.collidepoint(event.pos):
                    if __name__ == '__main__':
                        musicaInicio.stop()
                        aplicacion = Main()
                        aplicacion.init()
                        aplicacion.iniciarVSbot()


#board shape es una tupla que tiene dos valores, que son filas[0] y columnas[1]
def getNeighbors(y, x, board_shape):
    neighbors = list()

    if y > 0:
        neighbors.append((y - 1, x))
    if y < board_shape[0] - 1:
        neighbors.append((y + 1, x))
    if x > 0:
        neighbors.append((y, x - 1))
    if x < board_shape[1] - 1:
        neighbors.append((y, x + 1))

    #retorna una list con los "vecinos" que son las libertades posibles que tiene la ficha
    return neighbors

def spriteClick(posicion_sprite, posicion_click):
    sprite_y, sprite_x = posicion_sprite
    click_y, click_x = posicion_click

    if sprite_y - 10 < click_y < sprite_y + 10:
        if sprite_x - 10 < click_x < sprite_x + 10:
            return True

    return False

class Main:
    def __init__(self):
        self.locations = None
        self.visited = None
        self.empty_colors = None
        self.empty_counts = None
        self.empty_groups = None
        self.gameover = None
        self.passed_in_a_row = None
        self.komi = None
        self.turno_blanco = None
        self.turno = None
        self.screen = None
        self.sprite_array = None
        self.sprites = None
    def init(self, komi=2.5):
        # inicializar la biblioteca pygame y prepararla para su uso
        pygame.init()
        #Dimensiones de la pantalla
        anchoDePantalla = 1100
        altoDePantalla = 630


        # Asignamos un objeto de Sprites
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
        # cargar como icono de la ventana
        pygame.display.set_icon(pygame.image.load('lib/icono.jpg'))

        # contador de turnos
        self.turno = 0
        # turno jugador blanco
        self.turno_blanco = False
        # Ventaja del jugador que comienza segundo
        self.komi = komi
        self.passed_in_a_row = 0
        self.gameover = False

    def iniciarVSbot(self):
        clock = pygame.time.Clock()
        fps = 5
        # Generamos las ubicaciones de los Sprites
        self.ubicacionSprites()
        # Ubicamos los Sprites
        self.ubicarSprites()
        ejecutando = True
        musicaPartida = pygame.mixer.music
        musicaPartida.load('lib/Sonido/partida.mp3')
        musicaPartida.play(-1)
        musicaPartida.set_volume(0.05)
        background_image = pygame.image.load('lib/montaña.jpg')
        background_image = pygame.transform.scale(background_image, (1100, 630))
        # IMAGEN QUE MUESTRA DE QUIEN ES EL TURNO
        turnoImagen = pygame.image.load('lib/turnoColor.png')
        turnoImagen = pygame.transform.scale(turnoImagen, (318, 111))
        ubicacionTurno = self.screen.get_width() - 400
        #Botones para pasar menu y rendirse
        botonPasarImagen = pygame.image.load("lib/pasar.png").convert_alpha()
        botonPasarImagen = pygame.transform.scale(botonPasarImagen, (178, 52))
        botonPasar = botonPasarImagen.get_rect()
        botonPasar.x = self.screen.get_width() - 330
        botonPasar.y = 200
        botonMenuImagen = pygame.image.load("lib/menu.png").convert_alpha()
        botonMenuImagen = pygame.transform.scale(botonMenuImagen, (178, 52))
        botonMenu = botonMenuImagen.get_rect()
        botonMenu.x = self.screen.get_width() - 330
        botonMenu.y = 260


        bot = 0
        cont = 0
        while ejecutando:
            clock.tick(fps)
            if self.gameover:
                ejecutando = False
                if self.calculateWhoWon() == 'White':
                    # llamar a pantalla de ganador con ganador blanco
                    self.ganador("blanco")
                else:
                    # llamar a pantalla de ganador con ganador negro
                    self.ganador("negro")

            if self.turno % 2 == 0:
                for event in pygame.event.get():
                    # Creamos el fondo de la pantalla
                    self.screen.blit(background_image, (0, 0))
                    #Dibujamos botones al costado del tablero
                    self.screen.blit(turnoImagen,(ubicacionTurno,0))
                    self.screen.blit(botonPasarImagen,botonPasar)
                    self.screen.blit(botonMenuImagen,botonMenu)
                    # Dibujamos el tablero
                    self.dibujarTablero()
                    """
                    Dibujamos las ubicaciones de los Sprites
                    """
                    self.dibujarSprites()

                    if event.type == MOUSEBUTTONDOWN:
                        # posición actual del cursor del mouse en la ventana del juego (x,y)
                        pos = pygame.mouse.get_pos()

                        # contiene los sprites del grupo self.sprites con los que el cursor del mouse ha colisionado.
                        clicked_sprites = [sprite for sprite in self.sprites if spriteClick(sprite.location, pos)]
                        if botonPasar.collidepoint(event.pos):
                            if __name__ == '__main__':
                                self.pasar()
                        if botonMenu.collidepoint(event.pos):
                            if __name__ == '__main__':
                                pantallaInicio()
                                pygame.quit()
                        #asegurarse de que se ha hecho clic en al menos un sprite
                        if clicked_sprites:
                            # Sonido al poner ficha
                            sonidoFicha = pygame.mixer.Sound('lib/Sonido/Mover.mp3')
                            sonidoFicha.play(0)
                            sonidoFicha.set_volume(0.05)
                            clicked_sprite = clicked_sprites[0]
                            #verificar si el sprite clikeado no está ocupado.
                            if not clicked_sprite.occupied:
                                self.turno += 1
                                # colorcirculo es negro si el numero es impar y blanco si es par
                                colorCirculo = Negro if self.turno % 2 else Blanco

                                #obtener las coordenadas x , y de la ubicación del sprite clikeado.
                                x, y = clicked_sprite.location
                                posicion = (x + 1, y)

                                """
                                # Redimensionar la imagen al tamaño deseado (10x10)
                                imagen = pygame.image.load("lib/FichaNegra.png") if self.turno % 2 else pygame.image.load("lib/FichaBlanca.png")

                                imagen = pygame.transform.scale(imagen, (10, 10))
                                # Dibujar la imagen en la superficie de pantalla
                                self.screen.blit(imagen, posicion)
                                """

                                clicked_sprite.occupied = True
                                clicked_sprite.color = colorCirculo

                                # Envia a la funcion el Sprite clickeado
                                self.capturePieces(*clicked_sprite.array_indexes)

                                if not clicked_sprite.occupied:
                                    self.turno -= 1
                                    self.turno_blanco = True if not self.turno_blanco else False

                                else:
                                    self.passed_in_a_row = 0

                                    person = 'Black' if not self.turno % 2 else 'White'
                                    pygame.display.set_caption(f'Go Chess | It\'s {person}\'s move!')
                    elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            ejecutando = False

                        elif event.key == K_p:
                            player = 'White' if not self.turno % 2 else 'Black'
                            self.pasar()
                    elif event.type == QUIT:
                        ejecutando = False

            else:
                if self.passed_in_a_row==1:
                    if self.calculateWhoWon()=="White":
                        self.pasar()
                listiña=[]
                print("Turno del bot")
                self.screen.blit(background_image, (0, 0))
                self.dibujarTablero()
                self.dibujarSprites()

                for sprite in self.sprites:
                    if sprite.occupied and sprite.color == Negro:
                        #vecinos = getNeighbors(sprite.location[1],(19,19))
                        for loc in self.locations:
                            if sprite.location==loc[1]:
                                vecinos = getNeighbors(loc[0][1],loc[0][0], (19, 19))
                                for vec in vecinos:
                                    spritiño = self.sprite_array[vec[0]][vec[1]]
                                    if not spritiño.occupied:
                                        listiña.append(spritiño.location)



                if 0 == 0:
                    pos= random.choice(listiña)
                    # contiene los sprites del grupo self.sprites con los que el cursor del mouse ha colisionado.
                    clicked_sprites = [sprite for sprite in self.sprites if spriteClick(sprite.location, pos)]
                    # Sonido al poner ficha
                    sonidoFicha = pygame.mixer.Sound('lib/Sonido/Mover.mp3')
                    sonidoFicha.play(0)
                    sonidoFicha.set_volume(0.05)
                    # asegurarse de que se ha hecho clic en al menos un sprite
                    if clicked_sprites:
                            clicked_sprite = clicked_sprites[0]
                            # verificar si el sprite clikeado no está ocupado.
                            if not clicked_sprite.occupied:
                                self.turno += 1
                                # colorcirculo es negro si el numero es impar y blanco si es par
                                colorCirculo = Negro if self.turno % 2 else Blanco

                                # obtener las coordenadas x , y de la ubicación del sprite clikeado.
                                x, y = clicked_sprite.location
                                posicion = (x + 1, y)

                                """
                                # Redimensionar la imagen al tamaño deseado (10x10)
                                imagen = pygame.image.load("lib/FichaNegra.png") if self.turno % 2 else pygame.image.load("lib/FichaBlanca.png")
    
                                imagen = pygame.transform.scale(imagen, (10, 10))
                                # Dibujar la imagen en la superficie de pantalla
                                self.screen.blit(imagen, posicion)
                                """

                                clicked_sprite.occupied = True
                                clicked_sprite.color = colorCirculo

                                # Envia a la funcion el Sprite clickeado
                                self.capturePieces(*clicked_sprite.array_indexes)

                                if not clicked_sprite.occupied:
                                    self.turno -= 1
                                    self.turno_blanco = True if not self.turno_blanco else False

                                else:
                                    self.passed_in_a_row = 0

                                    person = 'Black' if not self.turno % 2 else 'White'
                                    pygame.display.set_caption(f'Go Chess | It\'s {person}\'s move!')
                    cont += 1

            pygame.display.update()
        pygame.quit()

    # Iniciar Juego
    def iniciar(self):
        clock = pygame.time.Clock()
        fps = 20
        # Generamos las ubicaciones de los Sprites
        self.ubicacionSprites()
        # Ubicamos los Sprites
        self.ubicarSprites()
        ejecutando = True
        musicaPartida = pygame.mixer.music
        musicaPartida.load('lib/Sonido/partida.mp3')
        musicaPartida.play(-1)
        musicaPartida.set_volume(0.05)
        background_image = pygame.image.load('lib/montaña.jpg')
        background_image = pygame.transform.scale(background_image, (1100, 630))
        #IMAGEN QUE MUESTRA DE QUIEN ES EL TURNO
        turnoImagen = pygame.image.load('lib/turnoColor.png')
        turnoImagen = pygame.transform.scale(turnoImagen,(318,111))
        ubicacionTurno = self.screen.get_width() - 400
        # Botones para pasar menu y rendirse
        botonPasarImagen = pygame.image.load("lib/pasar.png").convert_alpha()
        botonPasarImagen = pygame.transform.scale(botonPasarImagen, (178, 52))
        botonPasar = botonPasarImagen.get_rect()
        botonPasar.x = self.screen.get_width() - 330
        botonPasar.y = 200
        botonMenuImagen = pygame.image.load("lib/menu.png").convert_alpha()
        botonMenuImagen = pygame.transform.scale(botonMenuImagen, (178, 52))
        botonMenu = botonMenuImagen.get_rect()
        botonMenu.x = self.screen.get_width() - 330
        botonMenu.y = 260
        while ejecutando:
            clock.tick(fps)
            if self.gameover:
                ejecutando = False
                if self.calculateWhoWon() == 'White':
                    # llamar a pantalla de ganador con ganador blanco
                    self.ganador("blanco")
                else:
                    # llamar a pantalla de ganador con ganador negro
                    self.ganador("negro")

            for event in pygame.event.get():
                # Creamos el fondo de la pantalla

                self.screen.blit(background_image, (0, 0))
                self.screen.blit(turnoImagen,(ubicacionTurno,0))
                # Dibujamos botones al costado del tablero
                self.screen.blit(turnoImagen, (ubicacionTurno, 0))
                self.screen.blit(botonPasarImagen, botonPasar)
                self.screen.blit(botonMenuImagen,botonMenu)
                # Dibujamos el tablero
                self.dibujarTablero()
                """
                Dibujamos las ubicaciones de los Sprites
                """
                self.dibujarSprites()

                if event.type == MOUSEBUTTONDOWN:
                    # posición actual del cursor del mouse en la ventana del juego (x,y)
                    pos = pygame.mouse.get_pos()
                    # contiene los sprites del grupo self.sprites con los que el cursor del mouse ha colisionado.
                    clicked_sprites = [sprite for sprite in self.sprites if spriteClick(sprite.location, pos)]
                    # Sonido al poner ficha
                    sonidoFicha = pygame.mixer.Sound('lib/Sonido/Mover.mp3')
                    sonidoFicha.play(0)
                    sonidoFicha.set_volume(0.05)
                    #logica botones costado
                    if botonPasar.collidepoint(event.pos):
                        if __name__ == '__main__':
                            self.pasar()
                    if botonMenu.collidepoint(event.pos):
                        if __name__ == '__main__':
                            pantallaInicio()
                            pygame.quit()
                    #asegurarse de que se ha hecho clic en al menos un sprite
                    if clicked_sprites:
                        clicked_sprite = clicked_sprites[0]
                        #verificar si el sprite clikeado no está ocupado.
                        if not clicked_sprite.occupied:
                            self.turno += 1
                            # colorcirculo es negro si el numero es impar y blanco si es par
                            colorCirculo = Negro if self.turno % 2 else Blanco

                            #obtener las coordenadas x , y de la ubicación del sprite clikeado.
                            x, y = clicked_sprite.location
                            posicion = (x + 1, y)

                            # Redimensionar la imagen al tamaño deseado (10x10)
                            imagen = pygame.image.load("lib/FichaNegra.png") if self.turno % 2 else pygame.image.load("lib/FichaBlanca.png")

                            imagen = pygame.transform.scale(imagen, (10, 10))
                            # Dibujar la imagen en la superficie de pantalla
                            self.screen.blit(imagen, posicion)

                            clicked_sprite.occupied = True
                            clicked_sprite.color = colorCirculo

                            # Envia a la funcion el Sprite clickeado
                            self.capturePieces(*clicked_sprite.array_indexes)

                            if not clicked_sprite.occupied:
                                self.turno -= 1
                                self.turno_blanco = True if not self.turno_blanco else False

                            else:
                                self.passed_in_a_row = 0

                                person = 'Black' if not self.turno % 2 else 'White'
                                pygame.display.set_caption(f'Go Chess | It\'s {person}\'s move!')

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        ejecutando = False

                    elif event.key == K_p:
                        player = 'White' if not self.turno % 2 else 'Black'
                        self.pasar()

                elif event.type == QUIT:
                    ejecutando = False
            pygame.display.update()
        pygame.quit()

    def pasar(self):
        self.passed_in_a_row += 1
        if self.passed_in_a_row == 2:
            self.terminar()
            return

        self.turno += 1
        self.turno_blanco = True if not self.turno_blanco else False

        jugador = 'Black' if not self.turno % 2 else 'White'
        pygame.display.set_caption(f'Batalla! | Es turno del jugador {jugador}')

    #llama a la pantalla de final del juego
    def terminar(self):
        jugadorGanador = self.calculateWhoWon()
        self.gameover = True

    #retortna blanco o negro
    def calculateWhoWon(self):
        white_score = self.komi
        black_score = 0

        white_on_board, black_on_board = self.findPiecesOnBoard()
        white_surrounded, black_surrounded = self.calculateSurroundedSpots()

        white_score += white_on_board
        black_score += black_on_board

        white_score += white_surrounded
        black_score += black_surrounded

        if white_score > black_score:
            return 'White'
        else:
            return 'Black'

    def ganador(self, color):
        pygame.init()
        screen = pygame.display.set_mode((1100, 630))
        # Boton para volver al menu
        botonMenuImagen = pygame.image.load("lib/menu.png").convert_alpha()
        botonMenuImagen = pygame.transform.scale(botonMenuImagen, (178, 52))
        botonMenu = botonMenuImagen.get_rect()
        # establece la posición horizontal (x) del rectángulo
        botonMenu.x = (self.screen.get_width() / 2) - 85
        # establece la posición vertical (y) del rectángulo
        botonMenu.y = 550
        # Cargar imagen de fondo según el color
        if color == "blanco":
            background_image = pygame.image.load("lib/dragonBlanco.jpeg").convert()
        elif color == "negro":
            background_image = pygame.image.load("lib/dragonNegro.jpeg").convert()
        else:
            # Color no válido, salir sin mostrar imagen
            return

        background_image = pygame.transform.scale(background_image, (1100, 630))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == MOUSEBUTTONDOWN:
                    # posición actual del cursor del mouse en la ventana del juego (x,y)
                    pos = pygame.mouse.get_pos()

                    if botonMenu.collidepoint(event.pos):
                        if __name__ == '__main__':
                            pantallaInicio()
                            pygame.quit()
            screen.blit(background_image, (0, 0))
            screen.blit(botonMenuImagen,botonMenu)
            pygame.display.flip()

        pygame.quit()
    #devuelve cuantas fichas tiene cada uno
    def findPiecesOnBoard(self):
        white_count = 0
        black_count = 0

        for row in self.sprite_array:
            for item in row:
                if not item.occupied:
                    continue

                color = item.color

                if color == Blanco:
                    white_count += 1
                else:
                    black_count += 1

        return white_count, black_count

    #retorna espacio "cercado"
    def calculateSurroundedSpots(self):
        white_count = 0
        black_count = 0

        self.empty_groups = []
        self.empty_counts = []
        self.empty_colors = []
        self.visited = []

        for y, row in enumerate(self.sprite_array):
            for x, sprite in enumerate(row):
                if sprite.occupied:
                    continue

                self.findEmptyLocations(y, x)

        for index in range(len(self.empty_colors)):
            empty_count = self.empty_counts[index]
            empty_colors = self.empty_colors[index]

            if Negro not in empty_colors and Blanco in empty_colors:
                white_count += empty_count
            if Blanco not in empty_colors and Negro in empty_colors:
                black_count += empty_count

        return white_count, black_count

    #mp que devuelve las ubicaciones libres que tiene esa ficha, revisando sus libertades, y devolviendo cuales no estan
    #ocupadas por el rival
    def findEmptyLocations(self, y, x, adding=False):
        if not adding:
            self.empty_groups.append([])
            self.empty_counts.append(0)
            self.empty_colors.append([])

        neighbors = getNeighbors(y, x, (19, 19))
        neighbors.append((y, x))

        for location in neighbors:
            sprite = self.sprite_array[location[0]][location[1]]
            if sprite.occupied or sprite in self.visited:
                continue

            self.visited.append(sprite)
            self.empty_groups[-1].append(location)
            self.empty_counts[-1] += 1
            self.empty_colors[-1] += self.getNonEmptyColorsOfNeighbors(y, x)
            self.findEmptyLocations(location[0], location[1], adding=True)

    #devuelve el color de la ubicacion ocupada
    def getNonEmptyColorsOfNeighbors(self, y, x):
        colors = []

        neighbors = getNeighbors(y, x, (19, 19))
        for location in neighbors:
            sprite = self.sprite_array[location[0]][location[1]]
            if not sprite.occupied:
                continue
            colors.append(sprite.color)

        return colors

    #current group es una matriz de 19x19 con todos 0 o falso
    #nt pero basicamente te devuelve si tiene o no libertades
    def testGroup(self, board, opponent_board, y, x, current_group):

        pos = (y, x)

        if current_group[pos]:
            # las fichas ya testeads no son liberates
            return False

        #verifica si hay una ficha del rival en pos
        if opponent_board[pos]:
            current_group[pos] = True

            neighbors = getNeighbors(y, x, board.shape)


            for yn, xn in neighbors:
                has_liberties = self.testGroup(board, opponent_board, yn, xn, current_group)
                if has_liberties:
                    return True
            return False

        return not board[pos]

    #En resumen, la función se encarga de capturar las piezas del oponente en el juego, actualiza el estado del
    #tablero y cambia el turno de juego.
    def capturePieces(self, y, x):
        """
            Estos tableros son matrices NumPy que representan la distribución de las piezas en el juego.
            Cada celda de la matriz contiene un valor de 1.0 si hay una pieza blanca o negra
            en esa posición, respectivamente,y 0.0 si está vacía.
        """
        # Tablero auxiliar blanco
        tablero_blanco = np.array(
            [[1.0 if item.color == Blanco and item.occupied else 0.0 for item in row] for row in self.sprite_array],
            dtype=int)
        # Tablero auxiliar negro
        tablero_negro = np.array(
            [[1.0 if item.color == Negro and item.occupied else 0.0 for item in row] for row in self.sprite_array],
            dtype=int)

        # cambiamos el turno
        turno_blanco = self.turno_blanco
        self.turno_blanco = True if not self.turno_blanco else False

        # Llamamos a la funcion enviandole los dos tableros
        tablero_resultante = self.fastCapturePieces(tablero_negro, tablero_blanco, turno_blanco, y, x)

        for index1, row in enumerate(tablero_resultante):
            for index2, item in enumerate(row):
                # color de la ficha
                # Si el valor es 1, el color se establece en "Blanco"; de lo contrario, se establece en "Negro".
                color = Blanco if item == 1 else Negro
                # posicion ocupada o no
                # Si el valor de la celda es diferente de 0, se considera ocupada; de lo contrario, se considera vacía.
                occupied = True if item != 0 else False

                # Actualiza el estado de la celda correspondiente en la matriz
                # sprite_array con los valores de color y ocupado
                self.sprite_array[index1][index2].occupied = occupied
                self.sprite_array[index1][index2].color = color

    def fastCapturePieces(self, black_board_, white_board_, turn_white, y, x):

        black_board, white_board = black_board_.copy(), white_board_.copy()

        # solo testea los vecinos del jugador actual, ya que los del otro no han cambiado
        neighbors = getNeighbors(y, x, black_board.shape)

        #asigna a tablero el tablero del jugador actual, y a la otra el otro
        board = white_board if turn_white else black_board
        opponent_board = black_board if turn_white else white_board

        #crea otra copia del tablero del rival
        original_opponent_board = opponent_board.copy()

        # testear movimientos suicida
        original_pos = (y, x)

        original_pos = original_pos[::-1]

        # testear suicidio
        #array 19x19 tipo booleano
        current_group = np.zeros((19, 19), dtype=bool)
        original_pos_has_liberties = self.testGroup(opponent_board, board, *original_pos, current_group)


        # only test adjacent stones in opponent's color
        for pos in neighbors:
            #La línea de código pos = pos[::-1] invierte el orden de los elementos en la variable pos.
            pos = pos[::-1]

            if not opponent_board[pos]:
                continue
            #el código crea una matriz booleana de tamaño 19x19 llena de False
            current_group = np.zeros((19, 19), dtype=bool)
            has_liberties = self.testGroup(board, opponent_board, *pos, current_group)

            if not has_liberties:
                opponent_board[current_group] = False

        same = True
        break_out = False

        for row_index, row in enumerate(original_opponent_board):
            for item_index, item in enumerate(row):
                if opponent_board[row_index, item_index] != item:
                    same = False
                    break_out = True
                    break
            if break_out:
                break

        out_board = [[i for i in range(19)] for v in range(19)]
        for i in range(19):
            for v in range(19):
                if white_board[i][v]:
                    out_board[i][v] = 1
                elif black_board[i][v]:
                    out_board[i][v] = -1
                else:
                    out_board[i][v] = 0

        if same and not original_pos_has_liberties:
            out_board[original_pos[0]][original_pos[1]] = 0

            return out_board
        else:
            return out_board

    #esto genera un array llamado ubicaciones con las posiciones x y donde se posicionaran luego las fichas
    #esto es usado por ubicar sprites
    def ubicacionSprites(self):
        ubicaciones = []


        for y_index, y_pos in enumerate(range(10, alt, sp)):
            for x_index, x_pos in enumerate(range(10, alt, sp)):
                ubicaciones.append([[y_index, x_index], [y_pos, x_pos]])

        # se guarda la lista en la variable de clase
        self.locations = ubicaciones

    # esto es para crear el lugar clikeable donde iran las fichas, y las agrega a lalista de sprites,
    # la cual sera usada por la funcion dibujar sprites para obtener las ubicaciones
    def ubicarSprites(self):
        # rastrear la fila y el índice del elemento en la matriz
        fila = 0
        item = 0

        # iterar a través de las ubicaciones generadas
        for location in self.locations:

            if item >= 19:
                fila += 1
                item = 0
            if fila > 18:
                break

            sprite = nuevoSprite(*location, (10, 10), (255, 32, 1))

            # el sprite recién creado se agrega al grupo de sprites
            self.sprites.add(sprite)

            # también se agrega a la matriz
            self.sprite_array[item][fila] = sprite


            # siguiente elemento
            item += 1


    # Metodo para Dibujar lineas del tablero
    def dibujarTablero(self):

        for y_pos in range(10, alt,sp):
            pygame.draw.line(self.screen, Negro, (10, y_pos), (alt, y_pos), width=2)
        for x_pos in range(10, alt, sp):
            pygame.draw.line(self.screen, Negro, (x_pos, 10), (x_pos, alt), width=2)

    #dibuja la ficha en el lugar seleccionado
    def dibujarSprites(self):

        for entity in self.sprites:
            if entity.occupied:
                x, y = entity.location
                loc = (x-20,y-20)
                #pygame.draw.circle(self.screen, entity.color, loc, 15, 0)
                imagen = pygame.image.load("lib/FichaNegra.png") if entity.color==Negro else pygame.image.load(
                    "lib/FichaBlanca.png")
                imagen = pygame.transform.scale(imagen, (40, 40))

                self.screen.blit(imagen, loc)


if __name__ == '__main__':
    app = Main()
    pantallaInicio()
