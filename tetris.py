from settings import *
import math
from tetromino import Tetromino
import pygame.freetype as ft


class Text:
    """
        Classe responsável por escrever todas as informações do jogo.

        :param app Classe principal do jogo utilizada para obter informações que devem ser escritas ou algum outro dado
        do jogo para realização de cálculos.

        :var font Fonte usada para escrever os textos carregada do diretório.
    """

    def __init__(self, app):
        self.app = app
        self.font = ft.Font(FONT_PATH)

    def get_color(self):
        """
            Função usada para obter a cor usada no texto Tetris de forma que mude a cada chamada, criando a impressão
            de algo gradual.
        """

        time = pg.time.get_ticks() * 0.001
        n_sin = lambda t: (math.sin(t) * 0.5 + 0.5) * 255

        return n_sin(time * 0.5), n_sin(time * 0.2), n_sin(time * 0.9)

    def draw(self):
        """
            Função que desenha todos os textos na interface.
        """

        self.font.render_to(self.app.screen, (WIN_W * 0.595, WIN_H * 0.02),
                            text='TETRIS', fgcolor=self.get_color(),
                            size=TILE_SIZE * 1.65, bgcolor='black')
        self.font.render_to(self.app.screen, (WIN_W * 0.65, WIN_H * 0.22),
                            text='next', fgcolor='orange',
                            size=TILE_SIZE * 1.4, bgcolor='black')
        self.font.render_to(self.app.screen, (WIN_W * 0.64, WIN_H * 0.67),
                            text='score', fgcolor='orange',
                            size=TILE_SIZE * 1.4, bgcolor='black')
        self.font.render_to(self.app.screen, (WIN_W * 0.64, WIN_H * 0.8),
                            text=f'{self.app.tetris.score}', fgcolor='white',
                            size=TILE_SIZE * 1.8)


class Tetris:
    """
        Classe que contém as principais funções necessárias para o jogo funcionar.

        :param app Objeto com informações do jogo utilizada para recuperar algumas informações.

        :var sprite_group Agrupador de sprides que são as peças do tétris

        :var field_array Array que representa a área jogável, onde as peças serão colocadas quando encaixadas.

        :var tetromino Objeto que representa a peça do jogo, formado por 4 blocos em diferentes posições.

        :var next_tetromino Objeto que representa a próxima peça que será colocada no jogo.

        :var speed_up Indicativo de que o usuário abertou a seta para baixo, é usado para realizar a movimentação rápida
        da peça.

        :var score Pontuação atual do jogador.

        :var full_lines Contador da quantidade e linhas que foram preenchidas, é usado para realizar o cálculo do score

        :var points_per_lines Dicionário que contém a quantidade de score obtida ao destruir quantidade específicas de
        linhas.
    """

    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.field_array = self.get_field_array()
        self.tetromino = Tetromino(self)
        self.next_tetromino = Tetromino(self, current=False)
        self.speed_up = False

        self.score = 0
        self.full_lines = 0
        self.points_per_lines = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

    def get_score(self):
        """
            Função utilizada para obter o score do jogador após destruir as linhas preenchidas.
        """

        self.score += self.points_per_lines[self.full_lines]
        self.full_lines = 0

    def check_full_lines(self):
        """
            Função utilizada para checar a quantidade de linhas preenchidas
        """

        row = FIELD_H - 1
        for y in range(FIELD_H - 1, -1, -1):
            for x in range(FIELD_W):
                self.field_array[row][x] = self.field_array[y][x]

                if self.field_array[y][x]:
                    self.field_array[row][x].pos = vec(x, y)

            if sum(map(bool, self.field_array[y])) < FIELD_W:
                row -= 1
            else:
                for x in range(FIELD_W):
                    self.field_array[row][x].alive = False
                    self.field_array[row][x] = 0

                self.full_lines += 1

    def put_tetromino_blocks_in_array(self):
        """
            Função utilizada para colocar a peça do jogo dentro da posição no array.
        """

        for block in self.tetromino.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block

    def get_field_array(self):
        """
            Função utilizada para obter o array do jogo.
        """

        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]

    def is_game_over(self):
        """
            Função que verifica se o jogador perdeu.
        """

        if self.tetromino.blocks[0].pos.y == INIT_POS_OFFSET[1]:
            pg.time.wait(300)
            return True

    def check_tetromino_landing(self):
        """
            Função que trata o encaixe da peça de forma visual, caso a peça tenha sido encaixada fora da área o jogador
            terá perdido e o jogo é recomeçado.
        """

        if self.tetromino.landing:
            if self.is_game_over():
                self.__init__(self.app)
            else:
                self.speed_up = False
                self.put_tetromino_blocks_in_array()
                self.next_tetromino.current = True
                self.tetromino = self.next_tetromino
                self.next_tetromino = Tetromino(self, current=False)

    def control(self, pressed_key):
        """
            Função para tratar os eventos do usuário.

            :param pressed_key: Chave do evento obtida pelo pygame
        """

        if pressed_key == pg.K_LEFT:
            self.tetromino.move(direction='left')
        elif pressed_key == pg.K_RIGHT:
            self.tetromino.move(direction='right')
        elif pressed_key == pg.K_UP:
            self.tetromino.rotate()
        elif pressed_key == pg.K_DOWN:
            self.speed_up = True

    def draw_grid(self):
        """
            Função para desenhar o quadriculado na área jogável.
        """

        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.screen, 'black',
                             (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def update(self):
        """
            Função que realiza as verificações necessárias enquanto o jogo estiver rodando.
        """

        trigger = [self.app.anim_trigger, self.app.fast_anim_trigger][self.speed_up]
        if trigger:
            self.check_full_lines()
            self.tetromino.update()
            self.check_tetromino_landing()
            self.get_score()
        self.sprite_group.update()

    def draw(self):
        """
            Função que realiza o desenho de tudo que for necessário.
        """

        self.draw_grid()
        self.sprite_group.draw(self.app.screen)













