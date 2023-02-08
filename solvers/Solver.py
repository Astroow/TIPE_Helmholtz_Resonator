import numpy as np

from objects.Experiment import Experiment
from objects.Source import Source
from tools.maths import distance, closest_value


class Solver:

    def __init__(self, exp: Experiment, source: Source):
        self.exp = exp
        self.source = source

        self.p0 = 0
        self.p1 = 0

        self.r_max = self.compute_max_range()

        self.results = {}
        self.R = None
        self.P = None
        self.X = None
        self.Y = None
    def solve(self, p0: float, p1: float, r_step: float, t_step: float):
        self.X = np.linspace(0, self.exp.room_x, self.exp.x_res+1)
        self.Y = np.linspace(0, self.exp.room_y, self.exp.y_res+1)
        self.R = np.linspace(0, self.r_max, round(self.r_max/r_step))
        self.P = np.zeros((self.exp.x_res+1, self.exp.y_res+1))

        alpha = self.exp.sound_celerity*t_step/r_step
        beta = 2*(1 - (1 / alpha ** 2))
        gamma = 2*(1 - alpha ** 2)

        self.results[0] = p0
        self.results[self.R[1]] = p1

        for i in range(1, len(self.R)-1):
            self.results[self.R[i+1]] = (((beta+gamma) / (1 - alpha ** 2)) * (self.R[i] / (self.R[i+1])) * self.results[self.R[i]]) - (self.R[i-1])/(self.R[i+1])*self.results[self.R[i-1]]

        for i in range(len(self.X)):
            for j in range(len(self.Y)):
                x = self.X[i]
                y = self.Y[j]
                distance_to_source = distance(x, y, self.source.x_coord, self.source.y_coord)
                closest_r = closest_value(self.R, distance_to_source)
                self.P[j, i] = self.results[closest_r]
    def compute_max_range(self):
        return max(distance(self.source.x_coord, self.source.y_coord, 0, 0),
                   distance(self.source.x_coord, self.source.y_coord, 0, self.exp.room_y),
                   distance(self.source.x_coord, self.source.y_coord, self.exp.room_x, 0),
        distance(self.source.x_coord, self.source.y_coord, self.exp.room_x, self.exp.room_y))
