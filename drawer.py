import pygame

from shapes.shape import Shape


class Drawer:
    """
        Classe responsável por realizar o desenho das formas
        para causar a impressão de movimento.
    """

    def __init__(self, shape: Shape):
        self.shape = shape

    def start_draw(self):
        """
            Função que realiza chamadas para desenhar a forma
            a cada 10 milisegundos
        """

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.shape.update_position_y()

            pygame.display.flip()
            pygame.time.wait(10)
