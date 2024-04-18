import pygame as pg

vec = pg.math.Vector2

FPS = 60
"""
    Quantidade de frames por segundo que serão gerados. Esse valor é o máximo, não significa que sempre serão 60 frames 
    em um segundo.
"""

FIELD_COLOR = (48, 39, 32)
"""
    RGB usado no fundo na área do jogo onde o usuário movimenta e encaixa as peças.
"""

BG_COLOR = (24, 89, 117)
"""
    RGB usado no fundo da tela do jogo.
"""

SPRITE_DIR_PATH = 'assets/sprites'
"""
    Diretório onde estão as imagens dos quadrados que são utilizadas para formar as peças do jogo.
"""

FONT_PATH = 'assets/font/FREAKSOFNATUREMASSIVE.ttf'
"""
    Diretório onde está a fonte usada para escrever as informações.
"""

ANIM_TIME_INTERVAL = 150
"""
    Tempo em milisegundos da animação de decida automática da peça. Quanto maior o número mais lenta é a animação.
"""

FAST_ANIM_TIME_INTERVAL = 15
"""
    Tempo em milisegundos da animação de decida rápida da peça, quando o usuário aperta a seta para baixo. Quanto maior 
    o número mais lenta é a animação.
"""

TILE_SIZE = 40
"""
    A tela do jogo é divida em quadrados, o valor definido fará com que todos os  componentes visuais do jogo aumentem
    ou diminuam.
"""

FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
"""
    Uma tupla que representa o tamanho da tela do jogo. Ao alterar esses valores o tamanho da área usada na movimentação
    e encaixe das peças será alterada.
"""

FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE
"""
    Usando os valores FIELD_W e FIELD_H definidos na tupla FIELD_SIZE é realizado um cálculo para obter o tamanho
    da área que o usuário vai mover e encaixar as peças. Tanto a altura quando a largura são multipliciadas pelo 
    TILE_SIZE para termos proporção.
"""

FIELD_SCALE_W, FIELD_SCALE_H = 1.7, 1.0
"""
    Escala usada para calcular largura e altura da tela como um todo.
"""

WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H
"""
    Resolução da tela, calculada usando os valores definidos em FIELD_RES multiplicado pela escala.
"""

INIT_POS_OFFSET = vec(FIELD_W // 2 - 1, 0)
"""
    Posição inicial da peça. É um vetor de duas dimensões, o primeiro valor é metade da largura da área jogável e o 
    segundo é a posição Y, zero para começar do topo.
"""

NEXT_POS_OFFSET = vec(FIELD_W * 1.3, FIELD_H * 0.45)
"""
    Posição onde a próxima peça do jogo deve ficar.
"""

MOVE_DIRECTIONS = {'left': vec(-1, 0), 'right': vec(1, 0), 'down': vec(0, 1)}
"""
    Dicionário para armazenar as chaves que representam os movimentos que o usuário pode fazer usando as setas e para
    cada chave um vetor que define a direção que peça vai se mover. 
    
    Se for para esquerda precisa reduzir 1 do eixo X.
    
    Se for para direita precisa adicionar 1 ao eixo X.
    
    Se for para baixo precisa adicionar 1 ao eixo Y.
"""

TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}
"""
    Dicionário contendo as chaves que representam as peças do jogo.
    
    Cada chave aponta para uma lista de tuplas, onde cada tupla é uma coordenada X e Y. Cada uma das tuplas representa 
    a posição que haverá um quadrado, por exemplo o T:
    
    Quadrado 1 no centro da tela, por isso X = 0 e Y = 0.
    
    Quadrado 2 a esquerda do quadrado 1, por isso X = -1 e Y = 0.
    
    Quadrado 3 a direita do quadrado 1, por isso X = 1 e Y = 0.
    
    Quadrado 4 acima do quadrado 1, por isso X = 0 e Y = -1.
"""
