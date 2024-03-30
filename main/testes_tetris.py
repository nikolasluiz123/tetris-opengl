from config.configurator import Configurator
from draw.drawer import Drawer


def main():
    configurator = Configurator(screen_width=400, screen_height=800)
    configurator.configure_display_mode()
    configurator.configure_shape_list()

    drawer = Drawer(configurator)
    drawer.start_objects_movimentation()


if __name__ == "__main__":
    main()
