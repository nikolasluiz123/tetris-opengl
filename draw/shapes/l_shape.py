from OpenGL.GL import *

from draw.shapes.shape import Shape


class LShape(Shape):
    """
        Classe que representa uma forma em L
    """

    def draw(self):
        glPushMatrix()
        glTranslatef(self.position_x + self.shape_width / 2, self.position_y + self.shape_height / 2, 0.0)
        glRotatef(self.angle, 0.0, 0.0, 1.0)
        glTranslatef(-self.position_x - self.shape_width / 2, -self.position_y - self.shape_height / 2, 0.0)

        glColor3f(1, 1, 1)
        glBegin(GL_QUADS)

        # Quadrado maior da peça L
        glVertex2f(self.position_x, self.position_y)  # canto inferior esquerdo
        glVertex2f(self.position_x + self.shape_width, self.position_y)  # canto inferior direito
        glVertex2f(self.position_x + self.shape_width,
                   self.position_y + self.shape_height / 3)  # canto superior esquerdo
        glVertex2f(self.position_x, self.position_y + self.shape_height / 3)  # canto superior direito

        # Quadrado menor da peça L
        glVertex2f(self.position_x, self.position_y)  # canto inferior esquerdo
        glVertex2f(self.position_x + self.shape_width / 5, self.position_y)  # canto inferior direito
        glVertex2f(self.position_x + self.shape_width / 5,
                   self.position_y + self.shape_height * 2)  # canto superior esquerdo
        glVertex2f(self.position_x, self.position_y + self.shape_height * 2)  # canto superior direito

        glEnd()

        glPopMatrix()
