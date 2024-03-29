from draw.shapes.shape import Shape
from OpenGL.GL import *


class Square(Shape):

    def draw(self):
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_QUADS)
        glVertex2f(self.position_x, self.position_y)
        glVertex2f(self.position_x + self.size, self.position_y)
        glVertex2f(self.position_x + self.size, self.position_y + self.size)
        glVertex2f(self.position_x, self.position_y + self.size)
        glEnd()
