from abc import abstractmethod, ABC

from OpenGL.GL import *

from config.configurator import Configurator


class Shape(ABC):

    def __init__(self, configurator: Configurator, speed_movimentation_y: float, size: float):
        self.position_x = configurator.screen_width // 2
        self.position_y = configurator.screen_height + 50
        self.speed_movimentation_y = speed_movimentation_y
        self.speed_movimentation_x = 0
        self.size = size

    @abstractmethod
    def draw(self):
        pass
