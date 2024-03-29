import pygame
from OpenGL.GL import *
from pygame.locals import *

from config.configurator import Configurator
from draw.shapes.shape import Shape


class Drawer:
    """
        Classe responsável por realizar o desenho das formas
        para causar a impressão de movimento.
    """

    def __init__(self, configurator: Configurator, shape: Shape):
        self.configurator = configurator
        self.shape = shape
        self.clock = pygame.time.Clock()

    def start_object_movimentation(self):
        while True:
            glClear(GL_COLOR_BUFFER_BIT)

            # Eventos
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.shape.speed_movimentation_x = -1
                    elif event.key == K_RIGHT:
                        self.shape.speed_movimentation_x = 1
                elif event.type == KEYUP:
                    if event.key == K_LEFT or event.key == K_RIGHT:
                        self.shape.speed_movimentation_x = 0

            # Atualização da posição
            self.shape.position_x += self.shape.speed_movimentation_x * 5
            self.shape.position_y += self.shape.speed_movimentation_y * 5

            # Limites da tela
            if self.shape.position_x < 0:
                self.shape.position_x = 0
            elif self.shape.position_x + self.shape.size > self.configurator.screen_width:
                self.shape.position_x = self.configurator.screen_width - self.shape.size

            # Verificação se atingiu o chão
            if self.shape.position_y < 0:
                self.shape.position_y = 0
                self.shape.speed_movimentation_y = 0

            # Desenho do quadrado
            self.shape.draw()

            pygame.display.flip()
            self.clock.tick(60)
