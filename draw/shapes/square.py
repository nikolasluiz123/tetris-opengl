import numpy as np
from OpenGL.GL import *

from draw.shapes.shape import Shape


class Square(Shape):
    """
        Classe que representa um quadrado.
    """

    def __init__(self, configurator, speed_movimentation_y: float):
        super().__init__(configurator,
                         speed_movimentation_y,
                         int(configurator.screen_width * 0.1),
                         int(configurator.screen_height * 0.05))

    def draw(self):
        glPushMatrix()
        glTranslatef(self.position_x + self.shape_width / 2, self.position_y + self.shape_height / 2, 0)
        glRotatef(self.angle, 0, 0, 1)
        glTranslatef(-self.shape_width / 2, -self.shape_height / 2, 0)

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
            Essa função cria uma matriz com 1 para representar o quadrado,
            sendo a ordem dessa matriz baseado nas proporções do shape.
        """
        return np.ones((self.shape_height, self.shape_width), dtype=int)
