from settings import *
import random


class Block(pg.sprite.Sprite):
    """
        Classe que representa um bloco da peça do tétris.

        :param tetromino Objeto contendo as informações da peça usadas para montar o bloco.

        :param pos Lista de tuplas contendo as posições X e Y de cada quadrado que formará a peça.

        :var next_pos Posição que a próxima peça fica na interface.

        :var alive Indica se o bloco ainda está presente no jogo.

        :var image Imagem png carregada de cor aleatória.

        :var rect Retângulo do contorno da imagem.

        :var sfx_image Cópia da imagem da peça que será usada para o efeito de explosão quando uma linha for completada.

        :var sfx_speed Velocidade do efeito de explosão ao completar uma linha.

        :var sfx_cycles Quantidade de ciclos da animação de explosão ao completar uma linha.

        :var cycle_counter Contador dos ciclos usado para verificar quando deve parar de fazer a animação.
    """

    def __init__(self, tetromino, pos):
        self.tetromino = tetromino
        self.pos = vec(pos) + INIT_POS_OFFSET
        self.next_pos = vec(pos) + NEXT_POS_OFFSET
        self.alive = True

        super().__init__(tetromino.tetris.sprite_group)
        self.image = tetromino.image
        self.rect = self.image.get_rect()

        self.sfx_image = self.image.copy()
        self.sfx_image.set_alpha(110)
        self.sfx_speed = random.uniform(0.2, 0.6)
        self.sfx_cycles = random.randrange(6, 8)
        self.cycle_counter = 0

    def sfx_end_time(self):
        """
            Função para verificar se é o fim da aniação de explosão.
        """

        if self.tetromino.tetris.app.anim_trigger:
            self.cycle_counter += 1
            if self.cycle_counter > self.sfx_cycles:
                self.cycle_counter = 0
                return True

    def sfx_run(self):
        """
            Função usada para rodar a animação de explosão
        """

        self.image = self.sfx_image
        self.pos.y -= self.sfx_speed
        self.image = pg.transform.rotate(self.image, pg.time.get_ticks() * self.sfx_speed)

    def is_alive(self):
        """
            Função que roda a animação e quando ela terminar elimina o bloco do container
        """

        if not self.alive:
            if not self.sfx_end_time():
                self.sfx_run()
            else:
                self.kill()

    def rotate(self, pivot_pos):
        """
            Função utilizada para rotacionar o bloco em 90 graus

            :param pivot_pos: Posição que vai indicar qual dos blocos será o eixo da rotação.
        """

        translated = self.pos - pivot_pos
        rotated = translated.rotate(90)
        return rotated + pivot_pos

    def set_rect_pos(self):
        """
            Função que define a posição do bloco
        """
        pos = [self.next_pos, self.pos][self.tetromino.current]
        self.rect.topleft = pos * TILE_SIZE

    def update(self):
        """
            Função usada para atualizar as informações do bloco
        """
        self.is_alive()
        self.set_rect_pos()

    def is_collide(self, pos):
        """
            Função que verifica se o bloco enostou em algo

            :param pos: Posição atual
        """

        x, y = int(pos.x), int(pos.y)
        if 0 <= x < FIELD_W and y < FIELD_H and (
                y < 0 or not self.tetromino.tetris.field_array[y][x]):
            return False
        return True


class Tetromino:
    """
        Classe que representa uma peça, composta por 4 blocos

        :param tetris Objeto usado em operações do jogo.

        :param current Indica se a peça é a atual, ou seja, se está em jogo.

        :var shape Lista de tupla contendo as posições X e Y para montar a peça.

        :var image Imagem usada para montar a peça

        :var blocks Blocos que vão ser usados para montar a peça.

        :var landing Indica se a peça foi encaixada
    """

    def __init__(self, tetris, current=True):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOES.keys()))
        self.image = random.choice(tetris.app.images)
        self.blocks = [Block(self, pos) for pos in TETROMINOES[self.shape]]
        self.landing = False
        self.current = current

    def rotate(self):
        """
            Função para rotacionar a peça.
        """

        pivot_pos = self.blocks[0].pos
        new_block_positions = [block.rotate(pivot_pos) for block in self.blocks]

        if not self.is_collide(new_block_positions):
            for i, block in enumerate(self.blocks):
                block.pos = new_block_positions[i]

    def is_collide(self, block_positions):
        """
            Função que retorna se a peça bateu em algo
        """

        return any(map(Block.is_collide, self.blocks, block_positions))

    def move(self, direction):
        """
            Função que movimenta a peça dependendo da direção

            :param direction: Direção que a peça será movimentada
        """

        move_direction = MOVE_DIRECTIONS[direction]
        new_block_positions = [block.pos + move_direction for block in self.blocks]
        is_collide = self.is_collide(new_block_positions)

        if not is_collide:
            for block in self.blocks:
                block.pos += move_direction
        elif direction == 'down':
            self.landing = True

    def update(self):
        """
            Função que atualiza a peça
        """

        self.move(direction='down')











