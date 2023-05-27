"""
Esto importa todo el módulo pygame,
lo que te permite acceder a todas las funciones,
clases y constantes proporcionadas por la biblioteca.
"""
import pygame
# constantes para eventos, teclas y botones del mouse.
from pygame.locals import MOUSEBUTTONUP, QUIT
import numpy as np

"""
MOUSEBUTTONUP: Esta constante representa el evento de soltar un botón del mouse.
QUIT: Esta constante representa el evento de salir de la aplicación.
"""

# colores
Negro = (0, 0, 0)
<<<<<<< HEAD
Blanco = (255, 255, 255)
# color del tablero
ColorTablero = (125, 125, 125)


=======
Blanco = (255,255,255)
#color del tablero
ColorTablero = (125,125,125)
sp= 38
alt=703
>>>>>>> 13f8cbc363be88c6266fa04df3ac06420e8a1966
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
class Main:
    def init(self, komi=2.5):
        # inicializar la biblioteca pygame y prepararla para su uso
        pygame.init()
<<<<<<< HEAD
        # Dimensiones de la pantalla
        anchoDePantalla = 1000
        altoDePantalla = 700
=======
        #Dimensiones de la pantalla
        anchoDePantalla = 1280
        altoDePantalla = 720
>>>>>>> 13f8cbc363be88c6266fa04df3ac06420e8a1966

        # Asignamos un objeto de Sprites
        self.sprites = pygame.sprite.Group()
        """
        Es una matriz 2D (lista de listas) 
        que se inicializa con 19 filas y 19 columnas. 
        Cada elemento de la matriz se inicializa con el valor 0.
        """
        self.sprite_array = [[0 for _ in range(19)] for _ in range(19)]

<<<<<<< HEAD
        # creación de una ventana de visualización
        self.screen = pygame.display.set_mode((anchoDePantalla, altoDePantalla))
        # La siguiente linea indica el turno de cada jugador
=======

        #creación de una ventana de visualización
        self.screen = pygame.display.set_mode((anchoDePantalla, altoDePantalla),pygame.FULLSCREEN)
        #La siguiente linea indica el turno de cada jugador
>>>>>>> 13f8cbc363be88c6266fa04df3ac06420e8a1966
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

    # Pantalla de Inicio del juego
    def pantallaInicio(self):
        # inicializar la biblioteca pygame y prepararla para su uso
        pygame.init()
        # Dimension de la pantalla de inicio
<<<<<<< HEAD
        screen = pygame.display.set_mode((1000, 700))
        # Imagen inicial de fondo
=======
        screen = pygame.display.set_mode((1280, 720),pygame.FULLSCREEN)
        #Imagen inicial de fondo
>>>>>>> 13f8cbc363be88c6266fa04df3ac06420e8a1966
        background_image = pygame.image.load("lib/portada.png").convert()
        background_image = pygame.transform.scale(background_image, (1280, 720))

        # Boton
        button_image = pygame.image.load("lib/boton.png").convert_alpha()
        button_image = pygame.transform.scale(button_image, (250, 250))

        # objeto rectángulo que representa las dimensiones y la posición del botón en la interfaz gráfica.
        button_rect = button_image.get_rect()
        # establece la posición horizontal (x) del rectángulo
        button_rect.x = (screen.get_width() - button_rect.width) // 2
        # establece la posición vertical (y) del rectángulo
        button_rect.y = 464

        # renderizar la imagen de fondo
        screen.blit(background_image, (0, 0))
        # renderiza la imagen del botón
        screen.blit(button_image, button_rect)
        # actualizar la pantalla, mostrando los cambios realizados
        pygame.display.flip()

<<<<<<< HEAD
        # Bucle de pantalla de inicion para capturar los eventos del teclado o mouse
        while True:
=======
        #Bucle de pantalla de inicion para capturar los eventos del teclado o mouse
        Ejecutando = True
        while Ejecutando:
>>>>>>> 13f8cbc363be88c6266fa04df3ac06420e8a1966
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
                    if button_rect.collidepoint(event.pos):
                        if __name__ == '__main__':
                            app = Main()
                            app.init()
                            app.iniciar()

    # Iniciar Juego
    def iniciar(self):

        # Generamos las ubicaciones de los Sprites
        self.ubicacionSprites()
        # Ubicamos los Sprites
        self.ubicarSprites()

        ejecutando = True

        while ejecutando:
            for event in pygame.event.get():
                # Creamos el fondo de la pantalla
                self.screen.fill(ColorTablero)
                # Dibujamos el tabler
                self.dibujarTablero()
                """
                Dibujamos las ubicaciones de los Sprites
                """
                self.dibujarSprites()
                if event.type == MOUSEBUTTONUP:
                    # posición actual del cursor del mouse en la ventana del juego (x,y)
                    pos = pygame.mouse.get_pos()
                    # contiene los sprites del grupo self.sprites con los que el cursor del mouse ha colisionado.
                    clicked_sprites = [sprite for sprite in self.sprites if self.spriteClick(sprite.location, pos)]
<<<<<<< HEAD

                    # asegurarse de que se ha hecho clic en al menos un sprite
                    if clicked_sprites:
                        clicked_sprite = clicked_sprites[0]

                        # verificar si el sprite clikeado no está ocupado.
=======
                    #asegurarse de que se ha hecho clic en al menos un sprite
                    if clicked_sprites:
                        clicked_sprite = clicked_sprites[0]
                        #verificar si el sprite clikeado no está ocupado.
>>>>>>> 13f8cbc363be88c6266fa04df3ac06420e8a1966
                        if not clicked_sprite.occupied:
                            self.turno += 1
                            # colorcirculo es negro si el numero es impar y blanco si es par
                            colorCirculo = Negro if self.turno % 2 else Blanco
<<<<<<< HEAD

                            # obtener las coordenadas x , y de la ubicación del sprite clikeado.
                            x, y = clicked_sprite.location
                            posicion = (x + 1, y)

                            # dibuja un círculo en la pantalla en la posición loc, con un radio de 10 píxeles y utilizando el colo
=======
                            #obtener las coordenadas x , y de la ubicación del sprite clikeado.
                            x, y = clicked_sprite.location
                            posicion = (x + 1, y)
                            #dibuja un círculo en la pantalla en la posición loc, con un radio de 10 píxeles y utilizando el colo
>>>>>>> 13f8cbc363be88c6266fa04df3ac06420e8a1966
                            pygame.draw.circle(self.screen, colorCirculo, posicion, 10, 0)
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

                    print()
                elif event.type == QUIT:
                    ejecutando = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        ejecutando= False
            pygame.display.update()
        pygame.quit()

    def testGroup(self, board, opponent_board, y, x, current_group):
        """ Assume the current group is captured. Find it via flood fill
        and if an empty neighboor is encountered, break (group is alive).

        board - 19x19 array of player's stones
        opponent_board - 19x19 array of opponent's stones
        x,y - position to test
        current_group - tested stones in player's color

        """

        pos = (y, x)

        if current_group[pos]:
            # already tested stones are no liberties
            return False

        if opponent_board[pos]:
            current_group[pos] = True
            neighbors = self.getNeighbors(y, x, board.shape)

            for yn, xn in neighbors:
                has_liberties = self.testGroup(board, opponent_board, yn, xn, current_group)
                if has_liberties:
                    return True
            return False

        return not board[pos]

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

                # Actualiza el estado de la celda correspondiente en la matriz sprite_array con los valores de color y ocupado
                self.sprite_array[index1][index2].occupied = occupied
                self.sprite_array[index1][index2].color = color

    def fastCapturePieces(self, black_board_, white_board_, turn_white, y, x):

        black_board, white_board = black_board_.copy(), white_board_.copy()

        # only test neighbors of current move (other's will have unchanged
        # liberties)
        neighbors = self.getNeighbors(y, x, black_board.shape)

        board = white_board if turn_white else black_board
        opponent_board = black_board if turn_white else white_board

        original_opponent_board = opponent_board.copy()

        # to test suicidal moves
        original_pos = (y, x)
        original_pos = original_pos[::-1]

        # testing suicides

        current_group = np.zeros((19, 19), dtype=bool)
        original_pos_has_liberties = self.testGroup(opponent_board, board, *original_pos, current_group)

        # only test adjacent stones in opponent's color
        for pos in neighbors:
            pos = pos[::-1]

            if not opponent_board[pos]:
                continue

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

    def getNeighbors(self, y, x, board_shape):
        neighbors = list()

        if y > 0:
            neighbors.append((y - 1, x))
        if y < board_shape[0] - 1:
            neighbors.append((y + 1, x))
        if x > 0:
            neighbors.append((y, x - 1))
        if x < board_shape[1] - 1:
            neighbors.append((y, x + 1))

        return neighbors

    def ubicacionSprites(self):
<<<<<<< HEAD
        # lista para las ubicaciones de los sprites
        ubicaciones = []
=======
        #lista para las ubicaciones de los sprites
        locations = []
>>>>>>> 13f8cbc363be88c6266fa04df3ac06420e8a1966

        for y_index, y_pos in enumerate(range(10, alt, sp)):
            for x_index, x_pos in enumerate(range(10, alt, sp)):
                locations.append([[y_index, x_index], [y_pos, x_pos]])

<<<<<<< HEAD
        # se guarda la lista en la variable de clase
        self.locations = ubicaciones
=======
        #se guarda la lista en la variable de clase
        self.locations = locations
>>>>>>> 13f8cbc363be88c6266fa04df3ac06420e8a1966

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

    # Metodo para Dibujar el tablero
    def dibujarTablero(self):

        for y_pos in range(10, alt,sp):
            pygame.draw.line(self.screen, Negro, (10, y_pos), (alt, y_pos), width=2)
        for x_pos in range(10, alt, sp):
            pygame.draw.line(self.screen, Negro, (x_pos, 10), (x_pos, alt), width=2)

    def dibujarSprites(self):
        for entity in self.sprites:
            if entity.occupied:
                x, y = entity.location
<<<<<<< HEAD
                loc = (x + 1, y)
                pygame.draw.circle(self.screen, entity.color, loc, 10, 0)
=======
                loc = (x+1, y)
                pygame.draw.circle(self.screen, entity.color, loc, 15, 0)
>>>>>>> 13f8cbc363be88c6266fa04df3ac06420e8a1966

    def spriteClick(self, posicion_sprite, posicion_click):
        sprite_y, sprite_x = posicion_sprite
        click_y, click_x = posicion_click

        if sprite_y - 10 < click_y < sprite_y + 10:
            if sprite_x - 10 < click_x < sprite_x + 10:
                return True

        return False


if __name__ == '__main__':
    app = Main()
<<<<<<< HEAD
    app.pantallaInicio()
=======
    app.pantallaInicio()
>>>>>>> 13f8cbc363be88c6266fa04df3ac06420e8a1966
