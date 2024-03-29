from config.configurator import Configurator
from draw.drawer import Drawer
from draw.shapes.l_shape import LShape


def main():
    configurator = Configurator(screen_width=400, screen_height=800)
    configurator.configure_display_mode()

    # shape = Square(configurator, -0.3, 40, 40)
    # shape = Rectangle(configurator, -0.3, 15, 50)
    shape = LShape(configurator, -0.3, 50, 25)

    drawer = Drawer(configurator, shape)
    drawer.start_object_movimentation()


if __name__ == "__main__":
    main()
