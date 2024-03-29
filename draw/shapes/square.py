from draw.shapes.shape import Shape
from OpenGL.GL import *


class Square(Shape):
    """
        Classe para representar a forma de um quadrado.
    """

    def _draw_to_right(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glBegin(GL_QUADS)
        glVertex3f(self.initial_position_x - 0.1, self.initial_position_y + 0.1, 0)
        glVertex3f(self.initial_position_x - 0.1, self.initial_position_y - 0.1, 0)
        glVertex3f(self.initial_position_x + 0.1, self.initial_position_y - 0.1, 0)
        glVertex3f(self.initial_position_x + 0.1, self.initial_position_y + 0.1, 0)
        glEnd()

        self.initial_position_x += 0.1

    def _draw_to_left(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glBegin(GL_QUADS)
        glVertex3f(self.initial_position_x - 0.1, self.initial_position_y + 0.1, 0)
        glVertex3f(self.initial_position_x - 0.1, self.initial_position_y - 0.1, 0)
        glVertex3f(self.initial_position_x + 0.1, self.initial_position_y - 0.1, 0)
        glVertex3f(self.initial_position_x + 0.1, self.initial_position_y + 0.1, 0)
        glEnd()

        self.initial_position_x -= 0.1

    def _draw_to_bottom(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glBegin(GL_QUADS)
        glVertex3f(-0.1, self.initial_position_y + 0.1, 0)
        glVertex3f(0.1, self.initial_position_y + 0.1, 0)
        glVertex3f(0.1, self.initial_position_y - 0.1, 0)
        glVertex3f(-0.1, self.initial_position_y - 0.1, 0)
        glEnd()
