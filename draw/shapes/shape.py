from abc import abstractmethod, ABC


class Shape(ABC):
    """
        Classe que representa as formas do nosso jogo, ou seja,
        toda forma que criarmos deve ser filha dessa classe abstrata.
    """

    SPEED_MOVIMENTATION_Y = 0.007
    """
        Esse valor define o quanto será decrementado da posição Y
        do objeto. Basicamente, alterar esse valor muda a velocidade com
        que o objeto cai.
    """

    SPEED_MOVIMENTATION_X = 0.003

    MIN_Y_POSITION = -1.95
    """
        Esse valor define a posição Y que o objeto deve parar de cair
        e retornar para a posição inicial.
    """

    MAX_Y_POSITION = 2
    """
        Esse valor define qual a posição Y que o objeto deve iniciar sua
        queda.
    """

    def __init__(self):
        self.initial_position_y = self.MAX_Y_POSITION
        self.initial_position_x = 0
        self.MIN_X_POSITION = -1
        self.MAX_X_POSITION = 1

    @abstractmethod
    def _draw_to_bottom(self):
        """
            Função responsável por desenhar a forma decrementando
            o eixo y para mover o objeto para baixo.

            Essa função só é visível para os filhos de Shape pois
            ela apenas será usada dentro da classe Drawer para mover
            o objeto para baixo.
        """
        pass

    @abstractmethod
    def _draw_to_right(self):
        """
            Função responsável por mover o objeto para a direita.
        """
        pass

    @abstractmethod
    def _draw_to_left(self):
        """
            Função responsável por mover o objeto para a esquerda.
        """
        pass

    def update_position_y(self):
        """
            Função responsável por redesenhar a forma na nova posição Y,
            isso vai fazer com que tenhamos a percepção de movimento.
        """

        self.initial_position_y -= self.SPEED_MOVIMENTATION_Y
        self._draw_to_bottom()

    def update_position_x_left(self):
        if self.initial_position_x >= self.MIN_X_POSITION:
            self.initial_position_x -= self.SPEED_MOVIMENTATION_X
            self._draw_to_left()

    def update_position_x_right(self):
        if self.initial_position_x <= self.MAX_X_POSITION:
            self.initial_position_x -= self.SPEED_MOVIMENTATION_X
            self._draw_to_right()
