from config.configurator import Configurator
from draw.drawer import Drawer
from draw.shapes.square import Square


def main():
    configurator = Configurator(screen_width=400, screen_height=800)
    configurator.configure_display_mode()
    configurator.configure_perspective()

    drawer = Drawer(Square())
    drawer.start_draw()


if __name__ == "__main__":
    main()
