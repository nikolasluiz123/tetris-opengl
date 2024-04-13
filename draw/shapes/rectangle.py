import numpy as np
from OpenGL.GL import *

from draw.shapes.shape import Shape


class Rectangle(Shape):
    """
        Classe que representa um retângulo.
    """

    def __init__(self, configurator, speed_movimentation_y: float):
        super().__init__(configurator,
                         speed_movimentation_y,
                         int(configurator.screen_width * 0.05),
                         int(configurator.screen_height * 0.05))

    def draw(self):
        glPushMatrix()
        glTranslatef(self.position_x + self.shape_width // 2, self.position_y + self.shape_height // 2, 0)
        glRotatef(self.angle, 0, 0, 1)
        glTranslatef(-self.shape_width // 2, -self.shape_height // 2, 0)

        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_QUADS)
        glVertex2f(0, 0)
        glVertex2f(self.shape_width, 0)
        glVertex2f(self.shape_width, self.shape_height)
        glVertex2f(0, self.shape_height)
        glEnd()

        glPopMatrix()

    def to_matrix(self):
        """
            Essa função cria uma matriz com 1 para representar o retângulo,
            sendo a ordem dessa matriz baseado nas proporções do shape.

            Se por acaso houve alguma rotação que fez o retângulo ficar em um ângulo
            que a divisão por 180 graus não é zero quer dizer que precisamos mudar a matriz.

            O shape começa com os graus zerados, se o usuário rotacionar uma vez
            vamos ter 90 graus (positivos ou negativos) isso quer dizer que se o shape
            estava na vertical, agora está na horizontal e devemos representar isso na matriz.
        """
        matrix = np.ones((self.shape_height, self.shape_width), dtype=int)

        if self.angle % 180 != 0:
            matrix = matrix.T

        return matrix

    def get_dimensions_diff(self) -> int:
        return abs(self.shape_width - self.shape_height + (abs(self.shape_width - self.shape_height) // 2))
