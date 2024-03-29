from OpenGL.GL import *

from config.configurator import Configurator
from draw.shapes.shape import Shape


class LShape(Shape):
    """
        Classe que representa uma forma em L
    """

    def __init__(self,
                 configurator: Configurator,
                 speed_movimentation_y: float,
                 shape_width: float,
                 shape_height: float,
                 shape_width_2: float,
                 shape_height_2: float):
        """
            Construtor da forma em L

            :param configurator: Classe de configuração do jogo
            :param speed_movimentation_y: Velocidade que o objeto deverá se movimentar no eixo Y
            :param shape_width: Largura da forma que fica na horizontal do L
            :param shape_height: Altura da forma que fica na horizontal do L
            :param shape_width_2: Largura da forma que fica na vertical do L
            :param shape_height_2: Altura da forma que fica na vertical do L
        """

        super().__init__(configurator, speed_movimentation_y, shape_width, shape_height)

        self.shape_width_2 = shape_width_2
        self.shape_height_2 = shape_height_2

    def draw(self):
        glColor3f(1, 1, 1)
        glBegin(GL_QUADS)

        # Quadrado maior da peça L
        glVertex2f(self.position_x, self.position_y)
        glVertex2f(self.position_x + self.shape_width, self.position_y)
        glVertex2f(self.position_x + self.shape_width, self.position_y + self.shape_height)
        glVertex2f(self.position_x, self.position_y + self.shape_height)

        # Quadrado menor da peça L
        glVertex2f(self.position_x, self.position_y + self.shape_height)
        glVertex2f(self.position_x + self.shape_width_2, self.position_y + self.shape_height)
        glVertex2f(self.position_x + self.shape_width_2, self.position_y + self.shape_height + self.shape_height_2)
        glVertex2f(self.position_x, self.position_y + self.shape_height + self.shape_height_2)

        glEnd()

    def rotate(self, clockwise=True):
        pass
