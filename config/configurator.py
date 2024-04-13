import random
import sys

import numpy as np
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

from draw.shapes.l_shape import LShape
from draw.shapes.rectangle import Rectangle
from draw.shapes.shape import Shape, CalculatedDimensionsShape
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
        self.__generate_shapes_rectangle(speed_movimentation_y)
        self.__generate_shapes_l_shape(speed_movimentation_y)

        random.shuffle(self.shapes)

    def __generate_shapes_rectangle(self, speed_movimentation_y):
        """
            Função parar gerar peças de retângulo

            :param speed_movimentation_y: Velocidade de queda
        """
        for i in range(10):
            shape = Rectangle(configurator=self, speed_movimentation_y=speed_movimentation_y)
            self.shapes.append(shape)

    def __generate_shapes_square(self, speed_movimentation_y):
        """
            Função parar gerar peças de quadrado

            :param speed_movimentation_y: Velocidade de queda
        """

        for i in range(10):
            shape = Square(configurator=self, speed_movimentation_y=speed_movimentation_y)
            self.shapes.append(shape)

    def __generate_shapes_l_shape(self, speed_movimentation_y):
        """
            Função parar gerar peças de L

            :param speed_movimentation_y: Velocidade de queda
        """

        for i in range(10):
            shape = LShape(configurator=self, speed_movimentation_y=speed_movimentation_y)

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
            Função para colocar o shape dentro da matriz do jogo.

            Essa função vai transformar a forma em uma matriz através
            da função draw() da classe Shape.

            Tendo essa matriz gerada percorre-se ela e os números 1 contidos
            serão adicionados na matriz do jogo para indicar a presença do shape
            na posição.

            :param shape Shape que vai ser posto dentro da matriz
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

    def shape_fits_game_matrix(self, shape) -> bool:
        """
            Essa função retorna se o shape passado por parâmetro cabe
            na matriz do jogo na posição X e Y em que o shape estiver
            no momento da chamada.

            Essa função pode ser usada para parar a movimentação automática
            do eixo Y (que faz o shape cair) e definir shape como locked.

            Os princípios dessa função são os mesmos da função `Configurator.put_shape_in_game_matrix`
            percorre-se a matriz do shape da mesma forma mas ocorre a soma do valor que há na matriz
            do jogo com o valor que há na matriz do shape. Essa soma é feita para verificar se já há
            um shape posicionado naquela posição específica da matriz do jogo.

            :param shape: A peça que deseja verificar.
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

                game_matrix_y = int_shape_y + y + 1

                if game_matrix_y == self.game_matrix.shape[0] - 1:
                    return False

                position_value = self.game_matrix[game_matrix_y][game_matrix_x] + shape_matrix[y, x]

                if position_value == 2:
                    return False

        return True

    def __get_shape_position_y_to_matrix(self, shape: Shape) -> int:
        """
            Função que pode ser usada para obter a posição Y do shape
            realizando os devidos tratamentos para garantir que o valor
            retornado é compatível com uma posição de matriz.

            :param shape: Shape que deseja recuperar a posição Y.
        """
        max_game_matrix_position_y = self.game_matrix.shape[0] - 1
        shape_position_y = shape.position_y - 1

        result = max_game_matrix_position_y - (shape_position_y + shape.to_matrix().shape[0])
        not_equals_dimensions = shape.shape_height != shape.shape_width

        if isinstance(shape, CalculatedDimensionsShape) and shape.is_rotated() and not_equals_dimensions:
            result += shape.get_calculated_width()
        elif shape.is_rotated() and not_equals_dimensions:
            result -= shape.shape_width // 2

        if result < 0:
            result = result * -1

        return result

    def __get_shape_position_x_to_matrix(self, shape: Shape) -> int:
        """
            Função que pode ser usada para recuperar a posição X
            comos devidos tratamentos para garantir que o valor
            retornado é compatível com uma posição de matriz.

            :param shape: Shape que deseja recuperar a posição X.
        """

        int_shape_x = int(shape.position_x)

        if (int_shape_x + shape.shape_width) == self.game_matrix.shape[1]:
            int_shape_x = self.game_matrix.shape[1] - 1

        if int_shape_x > 0:
            int_shape_x = int_shape_x - (shape.to_matrix().shape[1] - 1)

        return int_shape_x

    def define_screen_limits_on_x_axis(self, shape):
        """
            Função que define até onde o objeto pode se movimentar no eixo X,
            isso garante que o objeto não saia da tela.

            :param shape: Shape que terá seu movimento em X limitado
        """
        not_equals_dimensions = shape.shape_height != shape.shape_width

        if shape.is_rotated():
            if isinstance(shape, CalculatedDimensionsShape) and not_equals_dimensions:
                dimensions_diff = abs(shape.get_calculated_width() - shape.shape_height)
                shape_position_x = shape.position_x - dimensions_diff

                if shape_position_x < 0:
                    shape.position_x = dimensions_diff

            elif not_equals_dimensions:
                dimensions_diff = abs(shape.shape_width - shape.shape_height + (abs(shape.shape_width - shape.shape_height) // 2))
                shape_position_x = shape.position_x - dimensions_diff

                screen_width = (self.screen_width + (abs(shape.shape_width - shape.shape_height) // 2))

                if shape_position_x < 0:
                    shape.position_x = dimensions_diff
                elif (shape.position_x + shape.shape_height) > screen_width:
                    shape.position_x = screen_width - shape.shape_height
        else:
            if shape.position_x < 0:
                shape.position_x = 0
            elif shape.position_x + shape.shape_width > self.screen_width:
                shape.position_x = self.screen_width - shape.shape_width

