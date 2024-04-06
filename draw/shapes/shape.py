from abc import abstractmethod, ABC

import numpy as np


class Shape(ABC):
    """
        Classe que define uma forma do jogo que será gerada e deverá ser
        encaixada.
    """

    def __init__(self,
                 configurator,
                 speed_movimentation_y: float,
                 shape_width: int,
                 shape_height: int):
        """
            Construtor com os parâmetros da forma.

            :param configurator: Classe de configuração do jogo
            :param speed_movimentation_y: Velocidade que o objeto deverá se movimentar no eixo Y
            :param shape_width: Largura da forma
            :param shape_height: Altura da forma
        """

        self.position_x = configurator.screen_width // 2
        self.position_y = configurator.screen_height - shape_height
        self.speed_movimentation_y = speed_movimentation_y
        self.speed_movimentation_x = 0
        self.shape_width = shape_width
        self.shape_height = shape_height
        self.angle = 0
        self.locked = False

    @abstractmethod
    def draw(self):
        """
            Função responsável por desenhar a forma.
        """

        pass

    def rotate(self, clockwise=True):
        rotation_angle = 5 if clockwise else -5
        self.angle += rotation_angle

    def to_matrix(self):
        """
            Retorna uma matriz representando o shape.
        """
        return np.ones((self.shape_height, self.shape_width), dtype=int)
