import pygame
from OpenGL.GL import *

from draw.shapes.shape import Shape


class Drawer:
    """
        Classe responsável por realizar o desenho das formas
        para causar a impressão de movimento.
    """

    def __init__(self, shape: Shape):
        self.shape = shape

    def start_draw_to_bottom(self):
        """
            Função que realiza chamadas para desenhar a forma
            a cada 10 milisegundos
        """

        clock = pygame.time.Clock()

        while self.shape.initial_position_y > self.shape.MIN_Y_POSITION:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.shape.update_position_y()

            pygame.display.flip()
            clock.tick(60)
