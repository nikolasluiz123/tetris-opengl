import pygame
from OpenGL.GL import *
from pygame.locals import *

from config.configurator import Configurator
from draw.shapes.shape import Shape


class Drawer:
    """
        Classe responsável por tratar tudo relacionado a movimentação
        dos objetos.
    """

    def __init__(self, configurator: Configurator, shape: Shape):
        """
            Construtor para passagem dos parâmetros

            :param configurator: Objeto de configuração do jogo.
            :param shape: Objeto que será movido
        """

        self.configurator = configurator
        self.shape = shape
        self.clock = pygame.time.Clock()
        self.rotate_clockwise = False
        self.rotate_counter_clockwise = False

    def start_object_movimentation(self):
        """
            Função principal que realiza a movimentação do objeto
            no eixo Y e permite que o usuário movimente-se no eixo
            X usando as setas.
        """

        while True:
            glClear(GL_COLOR_BUFFER_BIT)

            self.execute_actions_on_events()

            if self.shape.position_y > 0:
                self.update_object_positions()
            else:
                self.shape.position_y = 0
                self.shape.speed_movimentation_y = 0

            self.shape.draw()

            pygame.display.flip()
            self.clock.tick(60)

    def execute_actions_on_events(self):
        """
        Função responsável por tratar os eventos do jogo.

        Eventos:
            **QUIT** Quando o usuário fecha o jogo. Isso é necessário para que o processo do jogo não trave e que
            os recursos sejam liberados ao final do processo.

            **KEYDOWN** Quando o usuário aperta uma tecla. Pode ser usado para tratar a movimentação no eixo X do
            objeto.

            **KEYUP** Quando o usuário solta uma tecla. Pode ser usado para parar a movimentação no eixo X do
            objeto.
        """

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                self.move_object_on_x_axis(event)
                self.start_rotation(event)
            elif event.type == KEYUP:
                self.stop_object_movimentation_on_x_axis(event)
                self.stop_rotation(event)

    def start_rotation(self, event):
        """
        Função responsável por iniciar a rotação do objeto.

        :param event: Evento realizado pelo usuário
        """

        if event.key == K_w:
            self.rotate_clockwise = True
        elif event.key == K_s:
            self.rotate_counter_clockwise = True

    def stop_rotation(self, event):
        """
        Função responsável por parar a rotação do objeto.

        :param event: Evento realizado pelo usuário
        """

        if event.key == K_w:
            self.rotate_clockwise = False
        elif event.key == K_s:
            self.rotate_counter_clockwise = False
            
    def move_object_on_x_axis(self, event):
        """
            Função responsável por mover o objeto no eixo X,
            tanto para esquerda como para a direita dependendo da tecla
            precionada.

            Se a tecla precisonada for a seta esquerda, a velocidade de movimentação
            do objeto precisa negativa.

            Se a tecla precionada for a seta direita, a velocidade de movimentação
            do objeto precisa ser positiva.

            :param event: Evento realizado pelo usuário
        """

        if event.key == K_LEFT:
            self.shape.speed_movimentation_x = -1
        elif event.key == K_RIGHT:
            self.shape.speed_movimentation_x = 1

    def stop_object_movimentation_on_x_axis(self, event):
        """
            Função responsável por zerar a velocidade do objeto no eixo X
            caso seja necessário.

            :param event: Evento realizado pelo usuário
        """

        if event.key == K_LEFT or event.key == K_RIGHT:
            self.shape.speed_movimentation_x = 0

    def update_object_positions(self):
        """
            Função responsável por atualizar a posição X e Y baseado na velocidade definida
            no Objeto. É usado um multiplicador para aumentar um pouco a velocidade, isso pode
            ser definido dinamicamente no futuro.
        """

        self.shape.position_x += self.shape.speed_movimentation_x * 5
        self.shape.position_y += self.shape.speed_movimentation_y * 5

        if self.rotate_clockwise:
            self.shape.rotate(clockwise=True)
        elif self.rotate_counter_clockwise:
            self.shape.rotate(clockwise=False)

        self.define_screen_limits_on_x_axis()

    def define_screen_limits_on_x_axis(self):
        """
            Função que define até onde o objeto pode se movimentar no eixo X,
            isso garante que o objeto não saia da tela.
        """

        if self.shape.position_x < 0:
            self.shape.position_x = 0
        elif self.shape.position_x + self.shape.shape_width > self.configurator.screen_width:
            self.shape.position_x = self.configurator.screen_width - self.shape.shape_width
