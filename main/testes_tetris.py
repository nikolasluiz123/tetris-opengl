import pygame

from config.configurator import Configurator
from draw.drawer import Drawer
from draw.shapes.square import Square


def main():
    configurator = Configurator(screen_width=400, screen_height=800)
    configurator.configure_display_mode()

    square = Square(configurator, -0.3, 50)

    drawer = Drawer(configurator, square)
    drawer.start_object_movimentation()


if __name__ == "__main__":
    main()
