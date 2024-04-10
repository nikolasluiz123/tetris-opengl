import time
from abc import abstractmethod, ABC


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
        rotation_angle = 90 if clockwise else -90
        new_angle = self.angle + rotation_angle

        if new_angle >= 360.0 or new_angle <= -360.0:
            self.angle = 0
        else:
            self.angle += rotation_angle

    @abstractmethod
    def to_matrix(self):
        pass


class CalculatedDimensionsShape(Shape, ABC):

    @abstractmethod
    def get_calculated_width(self):
        pass
