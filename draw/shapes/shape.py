from abc import abstractmethod, ABC

from config.configurator import Configurator


class Shape(ABC):
    """
        Classe que define uma forma do jogo que será gerada e deverá ser
        encaixada.
    """

    def __init__(self,
                 configurator: Configurator,
                 speed_movimentation_y: float,
                 shape_width: float,
                 shape_height: float):
        """
            Construtor com os parâmetros da forma.

            :param configurator: Classe de configuração do jogo
            :param speed_movimentation_y: Velocidade que o objeto deverá se movimentar no eixo Y
            :param shape_width: Largura da forma
            :param shape_height: Altura da forma
        """

        self.position_x = configurator.screen_width // 2
        self.position_y = configurator.screen_height + 50
        self.speed_movimentation_y = speed_movimentation_y
        self.speed_movimentation_x = 0
        self.shape_width = shape_width
        self.shape_height = shape_height

    @abstractmethod
    def draw(self):
        """
            Função responsável por desenhar a forma.
        """

        pass
