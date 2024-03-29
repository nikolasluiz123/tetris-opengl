from OpenGL.GL import *

from draw.shapes.shape import Shape


class Rectangle(Shape):
    """
        Classe que representa um retângulo.
    """

    def draw(self):
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_QUADS)
        glVertex2f(self.position_x, self.position_y)
        glVertex2f(self.position_x + self.shape_width, self.position_y)
        glVertex2f(self.position_x + self.shape_width, self.position_y + self.shape_height)
        glVertex2f(self.position_x, self.position_y + self.shape_height)
        glEnd()