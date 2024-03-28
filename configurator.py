import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


class Configurator:
    """
        Classe de configuração de tudo que for necessário para iniciar
        os processos do jogo.
    """

    DEFAULT_VERTICAL_VIEW_ANGLE = 45
    """
        Esse valor é ângulo vertical da visualização, como se fosse
        o ângulo de posicionamento de uma câmera filmando o jogo.
    """

    DEFAULT_MAX_DISTANCE_Z = 50.0
    """
       Distância que define a profundidade máxima de visão,
       tudo que estiver mais longe que esse valor não será visualizável.
    """

    DEFAULT_MIN_DISTANCE_Z = 0.1
    """
       Distância que define o ponto inicial do campo de visão,
       tudo que estiver mais perto do que esse ponto não será visualizável. 
    """

    INITIAL_OBJECT_POSITION_X = 0.0
    """
        Posição do objeto no eixo X, é zero pois queremos ele no centro horizontalmente no
        início do jogo.
    """

    INITIAL_OBJECT_POSITION_Y = 0.0
    """
        Posição do objeto no eixo Y, é zero pois são realizados cálculos para mover
        o objeto nesse eixo, por isso, definir um valor nele não é muito interessante.
    """

    INITIAL_OBJECT_POSITION_Z = -5
    """
        Posição do objeto no eixo Z, esse valor pode ser usado para definir o tamanho
        do objeto que vai ser exibido pois ele distancia o objeto da câmera dando a impressão
        que é um objeto menor.
    """

    def __init__(self, screen_width, screen_height):
        """
            Construtor da classe de configuração

            :param screen_width: Largura da janela
            :param screen_height: Altura da janela
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.aspect_relation = (self.screen_width / self.screen_height)

    def configure_display_mode(self):
        """
            Função para configurar a janela que o jogo será desenhado
        """
        pygame.init()
        pygame.display.set_mode((self.screen_width, self.screen_height), DOUBLEBUF | OPENGL)

    def configure_perspective(self,
                              vertical_view_angle=DEFAULT_VERTICAL_VIEW_ANGLE,
                              min_distance_z=DEFAULT_MIN_DISTANCE_Z,
                              max_distance_z=DEFAULT_MAX_DISTANCE_Z):
        """
            Função que define as configurações da perspectiva, basicamente os ângulos de visão e
            o posicionamento inicial do objeto.

            :param vertical_view_angle: Ângulo vertical da visualização.
            :param min_distance_z: Distância que define a profundidade máxima de visão.
            :param max_distance_z: Distância que define o ponto inicial do campo de visão.
        """
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(vertical_view_angle, self.aspect_relation, min_distance_z, max_distance_z)
        glTranslatef(self.INITIAL_OBJECT_POSITION_X, self.INITIAL_OBJECT_POSITION_Y, self.INITIAL_OBJECT_POSITION_Z)
