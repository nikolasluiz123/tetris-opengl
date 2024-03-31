import random

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

from draw.shapes.l_shape import LShape
from draw.shapes.rectangle import Rectangle
from draw.shapes.square import Square


class Configurator:
    """
        Classe de configuração do jogo
    """

    def __init__(self, screen_width: float, screen_height: float):
        """
            Construtor da classe de configuração

            :param screen_width: Largura da janela
            :param screen_height: Altura da janela
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.shapes = []

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
        speed_movimentation_y = -0.3

        self.__generate_shapes_rectangle(speed_movimentation_y)
        self.__generate_shapes_square(speed_movimentation_y)
        self.__generate_shapes_l_shape(speed_movimentation_y)

        random.shuffle(self.shapes)

    def __generate_shapes_rectangle(self, speed_movimentation_y):
        """
            Função parar gerar peças de retângulo

            :param speed_movimentation_y: Velocidade de queda
        """
        for i in range(20):
            random_rectangle_width = random.randint(50, 100)
            random_rectangle_height = random.randint(5, 15)

            shape = Rectangle(configurator=self,
                              speed_movimentation_y=speed_movimentation_y,
                              shape_width=random_rectangle_width,
                              shape_height=random_rectangle_height)

            self.shapes.append(shape)

    def __generate_shapes_square(self, speed_movimentation_y):
        """
            Função parar gerar peças de quadrado

            :param speed_movimentation_y: Velocidade de queda
        """

        for i in range(20):
            random_square_size = random.randint(20, 45)

            shape = Square(configurator=self,
                           speed_movimentation_y=speed_movimentation_y,
                           shape_width=random_square_size,
                           shape_height=random_square_size)

            self.shapes.append(shape)

    def __generate_shapes_l_shape(self, speed_movimentation_y):
        """
            Função parar gerar peças de L

            :param speed_movimentation_y: Velocidade de queda
        """

        for i in range(20):
            random_l_shape_width = random.randint(25, 50)
            random_l_shape_height = random.randint(15, 30)

            shape = LShape(configurator=self,
                           speed_movimentation_y=speed_movimentation_y,
                           shape_width=random_l_shape_width,
                           shape_height=random_l_shape_height)

            self.shapes.append(shape)
