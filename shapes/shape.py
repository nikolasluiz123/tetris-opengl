from abc import abstractmethod, ABC

from OpenGL.GL import *


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

    MIN_Y_POSITION = -2
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

    @abstractmethod
    def _draw(self):
        """
            Função responsável por desenhar a forma, deve ser obrigatoriamente
            implementada por todos os filhos.
        """
        pass

    def update_position_y(self):
        """
            Função responsável por redesenhar a forma na nova posição Y,
            isso vai fazer com que tenhamos a percepção de movimento.
        """

        self.initial_position_y -= self.SPEED_MOVIMENTATION_Y

        if self.initial_position_y < self.MIN_Y_POSITION:
            self.initial_position_y = self.MAX_Y_POSITION

        self._draw()


class Square(Shape):
    """
        Classe para representar a forma de um quadrado.
    """

    def _draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glBegin(GL_QUADS)
        glVertex3f(-0.1, self.initial_position_y + 0.1, 0)
        glVertex3f(0.1, self.initial_position_y + 0.1, 0)
        glVertex3f(0.1, self.initial_position_y - 0.1, 0)
        glVertex3f(-0.1, self.initial_position_y - 0.1, 0)
        glEnd()
