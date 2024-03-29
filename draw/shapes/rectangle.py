from OpenGL.GL import *

from draw.shapes.shape import Shape


class Rectangle(Shape):
    """
        Classe que representa um retângulo.
    """

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
