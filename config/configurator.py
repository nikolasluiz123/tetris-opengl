import random
import sys

import numpy as np
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

from draw.shapes.l_shape import LShape
from draw.shapes.rectangle import Rectangle
from draw.shapes.shape import Shape
from draw.shapes.square import Square


class Configurator:
    """
        Classe de configuração do jogo
    """

    GAME_MATRIX_AXIS_LINE_DIMENSION = 0
    """
        Constante que representa a dimensão de linha
        de uma matriz.
    """

    def __init__(self, screen_width: int, screen_height: int):
        """
            Construtor da classe de configuração

            :param screen_width: Largura da janela
            :param screen_height: Altura da janela
        """
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.shapes = []
        self.game_matrix = np.zeros((screen_height, screen_width), dtype=int)

    def configure_display_mode(self):
        """
            Função para configurar a janela que o jogo será desenhado
        """
        pygame.init()
        pygame.display.set_mode((self.screen_width, self.screen_height), DOUBLEBUF | OPENGL)

        glClearColor(0.0, 0.0, 0.0, 1.0)
        gluOrtho2D(0, self.screen_width, 0, self.screen_height)

    def configure_shape_list(self):
        """
            Função para inicializar a lista de shapes com uma quantidade
            específica de cada um. A lista é embaralhada para tentar trazer
            uma aleatoriedade nas peças que cairão.
        """
        speed_movimentation_y = -1

        self.__generate_shapes_square(speed_movimentation_y)
        # self.__generate_shapes_rectangle(speed_movimentation_y)
        self.__generate_shapes_l_shape(speed_movimentation_y)

        # random.shuffle(self.shapes)

    def __generate_shapes_rectangle(self, speed_movimentation_y):
        """
            Função parar gerar peças de retângulo

            :param speed_movimentation_y: Velocidade de queda
        """
        for i in range(1):
            # random_rectangle_width = random.randint(50, 100)
            # random_rectangle_height = random.randint(5, 15)

            shape = Rectangle(configurator=self,
                              speed_movimentation_y=speed_movimentation_y,
                              shape_width=12,
                              shape_height=2)

            self.shapes.append(shape)

    def __generate_shapes_square(self, speed_movimentation_y):
        """
            Função parar gerar peças de quadrado

            :param speed_movimentation_y: Velocidade de queda
        """

        for i in range(1):
            shape = Square(configurator=self,
                           speed_movimentation_y=speed_movimentation_y,
                           shape_width=4,
                           shape_height=4)

            self.shapes.append(shape)

    def __generate_shapes_l_shape(self, speed_movimentation_y):
        """
            Função parar gerar peças de L

            :param speed_movimentation_y: Velocidade de queda
        """

        for i in range(1):
            shape = LShape(configurator=self,
                           speed_movimentation_y=speed_movimentation_y,
                           shape_width=5,
                           shape_height=3)

            self.shapes.append(shape)

    def delete_completed_matrix_lines(self):
        lines_to_delete = self.__check_game_matrix_lines()

        if len(lines_to_delete) > 0:
            for line_number in lines_to_delete:
                self.game_matrix = np.delete(self.game_matrix, line_number, axis=self.GAME_MATRIX_AXIS_LINE_DIMENSION)
                new_line = np.zeros((1, self.screen_width), dtype=int)
                self.game_matrix = np.concatenate((new_line, self.game_matrix),
                                                  axis=self.GAME_MATRIX_AXIS_LINE_DIMENSION)

    def __check_game_matrix_lines(self) -> list[int]:
        return [i for i, line in enumerate(self.game_matrix) if self.__is_line_complete(line)]

    def __is_line_complete(self, line):
        return all(line)

    def put_shape_in_game_matrix(self, shape):
        """
            Coloca o shape dentro da matriz do jogo.
        """
        shape_matrix = shape.to_matrix()

        int_shape_x = self.__get_shape_position_x_to_matrix(shape)
        int_shape_y = self.__get_shape_position_y_to_matrix(shape)

        for y in range(shape_matrix.shape[0]):
            for x in range(shape_matrix.shape[1]):
                if int_shape_x == (self.game_matrix.shape[1] - 1):
                    game_matrix_x = int_shape_x - x
                else:
                    game_matrix_x = int_shape_x + x

                game_matrix_y = int_shape_y + y

                if shape_matrix[y, x] == 1:
                    self.game_matrix[game_matrix_y][game_matrix_x] = shape_matrix[y, x]

        with np.printoptions(threshold=sys.maxsize):
            print(shape_matrix)
            print(self.game_matrix)

    def shape_fits_game_matrix(self, shape):
        shape_matrix = shape.to_matrix()
        int_shape_x = self.__get_shape_position_x_to_matrix(shape)
        int_shape_y = self.__get_shape_position_y_to_matrix(shape)

        for y in range(shape_matrix.shape[0]):
            for x in range(shape_matrix.shape[1]):
                if int_shape_x == (self.game_matrix.shape[1] - 1):
                    game_matrix_x = int_shape_x - x
                else:
                    game_matrix_x = int_shape_x + x

                game_matrix_y = int_shape_y + y + 1

                if int_shape_y == (self.game_matrix.shape[0] - 1):
                    return False

                position_value = self.game_matrix[game_matrix_y][game_matrix_x] + shape_matrix[y, x]

                if position_value == 2 or shape.position_y <= 0:
                    return False

        return True

    def __get_shape_position_y_to_matrix(self, shape: Shape) -> int:
        max_game_matrix_position_y = self.game_matrix.shape[0] - 1
        shape_position_y = shape.position_y - 1

        result = max_game_matrix_position_y - (shape_position_y + shape.to_matrix().shape[0])

        if result < 0:
            result = result * -1

        return result

    def __get_shape_position_x_to_matrix(self, shape) -> int:
        int_shape_x = int(shape.position_x)

        if (int_shape_x + shape.shape_width) == self.game_matrix.shape[1]:
            int_shape_x = self.game_matrix.shape[1] - 1

        if int_shape_x > 0:
            int_shape_x = int_shape_x - (shape.to_matrix().shape[1] - 1)

        return int_shape_x
