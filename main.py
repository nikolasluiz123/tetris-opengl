from settings import *
from tetris import Tetris, Text
import sys
import pathlib


class App:
    """
        Classe que representa o jogo, contem as funcionalidades principais para desenhar as peças e realizar as ações
        de acordo com as teclas pressionadas.

        :var user_event Identificador do evento padrão do pygame, é usado na movimentação das peças no eixo Y na
        velocidade normal.

        :var fast_user_event Identificador de um evento customizado, é usado na movimentação rápida das peças no eixo Y
        em alta velocidade. Esse evento só será chamado quando o jogador apertar a seta para baixo.

        :var anim_trigger Indica se a animação de movimento automático da peça no eixo Y deve ocorrer.

        :var fast_anim_trigger Indica se a animação de movimento rápido da peça no eixo Y deve ocorrer.

        :var screen: Representação da tela criada pelo pygame de acordo com as dimensões definidas.

        :var clock: Timer utilizado para controlar a taxa de quadros do jogo.

        :var images Lista com as imagens que representam os cubos que formarão as peças do jogo.

        :var tetris Objeto usado em operações do jogo.

        :var text Objeto usado para escrever as informações textuais.
    """

    def __init__(self):
        self.user_event = 0
        self.fast_user_event = 0
        self.anim_trigger = False
        self.fast_anim_trigger = False

        pg.init()
        pg.display.set_caption('Tetris')

        self.screen = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.set_timer()
        self.images = self.load_images()
        self.tetris = Tetris(self)
        self.text = Text(self)

    def load_images(self):
        """
            Função para carregar as imagens usadas para montar as peças do jogo. Todas as imagens são ajustadas para que
            fiquem no mesmo tamanho que os pequenos quadrados definidos na área jogável.
        """

        files = [item for item in pathlib.Path(SPRITE_DIR_PATH).rglob('*.png') if item.is_file()]
        images = [pg.image.load(file).convert_alpha() for file in files]
        images = [pg.transform.scale(image, (TILE_SIZE, TILE_SIZE)) for image in images]

        return images

    def set_timer(self):
        """
            Função que define temporizadores do pygame para que sejam enviados eventos a cada X tempo, conforme definido
            nas settings.
        """

        self.user_event = pg.USEREVENT
        self.fast_user_event = pg.USEREVENT + 1
        self.anim_trigger = False
        self.fast_anim_trigger = False
        pg.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)
        pg.time.set_timer(self.fast_user_event, FAST_ANIM_TIME_INTERVAL)

    def update(self):
        """
            Função utilizada para atualizar o jogo, executa todas as validações necesárias enquanto o jogo estiver
            rodando.
        """

        self.tetris.update()
        self.clock.tick(FPS)

    def draw(self):
        """
            Função para realizar o desenho de toda a interface do jogo.
        """

        self.screen.fill(color=BG_COLOR)
        self.screen.fill(color=FIELD_COLOR, rect=(0, 0, *FIELD_RES))
        self.tetris.draw()
        self.text.draw()
        pg.display.flip()

    def check_events(self):
        """
            Função que realiza o tratamento dos eventos realizados pelo usuário.
        """

        self.anim_trigger = False
        self.fast_anim_trigger = False

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.tetris.control(pressed_key=event.key)
            elif event.type == self.user_event:
                self.anim_trigger = True
            elif event.type == self.fast_user_event:
                self.fast_anim_trigger = True

    def run(self):
        """
            Função usada para execução do jogo em loop.
        """

        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    app = App()
    app.run()
