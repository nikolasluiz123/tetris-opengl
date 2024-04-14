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
        """
            Função responsável por realizar a rotação do shape.

            A rotação pode ser no sentido horário ou anti-horário, dependendo do valor do parâmetro clockwise.
            Se a rotação é no sentido horário é preciso incrementar o ângulo com valores positivos, caso a rotação
            for no sentido anti-horário deve ser incrementado valores negativos.

            Sempre incrementamos 90 graus (positivos ou negativos) para que a peça faça rotações de forma mais rápida
            e direta como ocorre no jogo mesmo.

            Quando o ângulo chegar em 360 (positivos ou negativos) zeramos a variável pois significa que a peça já
            voltou para a posição inicial.

            :param clockwise: Indica se a rotação é no sentido horário (true) ou anti-horário (false)
        """

        rotation_angle = 90 if clockwise else -90
        new_angle = self.angle + rotation_angle

        if new_angle >= 360.0 or new_angle <= -360.0:
            self.angle = 0
        else:
            self.angle += rotation_angle

    def is_rotated(self) -> bool:
        """
            Função reponsável por retornar se houve alguma rotação.
        """
        return self.angle != 0

    @abstractmethod
    def to_matrix(self):
        """
            Função que deve transformar o shape em uma matriz
        """
        pass

    @abstractmethod
    def get_dimensions_diff(self) -> int:
        pass


class CalculatedDimensionsShape(Shape, ABC):
    """
        Classe para representar shapes que sejam de formatos um pouco mais complexos.

        Algumas das peças do tétris são formadas por duas ou maisformas básicas, normalmente retângulos.
        Para manter o padrão de passarmos somente altura e largura como parâmetro quando temos esses shapes mais
        complexos são realizados cálculos para obter dimensões.
    """

    @abstractmethod
    def get_calculated_width(self):
        """
            Função responsável por retornar a largura calculada do shape.
        """
        pass

    @abstractmethod
    def get_calculated_height(self):
        """
            Função responsável por retornar a altura calculada do shape.
        """
        pass
