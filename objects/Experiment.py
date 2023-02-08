import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray

from objects.Resonator import Resonator
from objects.Source import Source


class Experiment:

    def __init__(self, name: str, room_x: int, room_y: int, sound_celerity: float, p_int: float, x_res: int, y_res: int):
        self.name = name
        self.room_x = room_x
        self.room_y = room_y
        self.x_res = x_res
        self.y_res = y_res

        self.sound_celerity = sound_celerity
        self.p_int = p_int

        self.sources = []
        self.resonators = []

        self.fig = plt.figure()
        self.plot = self.fig.add_subplot()

    def render_room(self, sP: ndarray, sX: np.linspace, sY: np.linspace):
        plt.cla()

        self.plot.set_title(f"Experiment {self.name} for c = {self.sound_celerity} m.s / p_int = {self.p_int} Pa")
        self.plot.set_xlim([0, self.room_x])
        self.plot.set_ylim([0, self.room_y])

        x_source = [source.x_coord for source in self.sources]
        y_source = [source.y_coord for source in self.sources]
        plt.plot(x_source, y_source, 'x', label='sources')

        x_resonator = [resonator.x_coord for resonator in self.resonators]
        y_resonator = [resonator.y_coord for resonator in self.resonators]
        plt.plot(x_resonator, y_resonator, 'h', label='resonators')

        X, Y = np.meshgrid(sX, sY)
        cm = plt.cm.get_cmap('plasma')
        plt.scatter(X, Y, c=sP, cmap=cm)
        plt.colorbar(label='Pressure (Pa)')

        plt.legend(loc='upper right')
        plt.show()

    def add_source(self, source: Source):
        self.sources.append(source)

    def add_resonator(self, resonator: Resonator):
        self.resonators.append(resonator)