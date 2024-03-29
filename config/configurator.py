import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


class Configurator:

    def __init__(self, screen_width: float, screen_height: float):
        """
            Construtor da classe de configuração

            :param screen_width: Largura da janela
            :param screen_height: Altura da janela
        """
        self.screen_width = screen_width
        self.screen_height = screen_height

    def configure_display_mode(self):
        """
            Função para configurar a janela que o jogo será desenhado
        """
        pygame.init()
        pygame.display.set_mode((self.screen_width, self.screen_height), DOUBLEBUF | OPENGL)

        glClearColor(0.0, 0.0, 0.0, 1.0)
        gluOrtho2D(0, self.screen_width, 0, self.screen_height)
