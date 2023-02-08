import numpy as np

from objects.Experiment import Experiment
from solvers.Solver import Solver


class ExpSolver:

    def __init__(self, exp: Experiment):
        self.exp = exp
        self.P = np.full((self.exp.x_res+1, self.exp.y_res+1), exp.p_int, dtype='float64')
        self.solvers = []

        self.X = np.linspace(0, self.exp.room_x, self.exp.x_res+1)
        self.Y = np.linspace(0, self.exp.room_y, self.exp.y_res+1)

    def solve_global(self):
        for solver in self.solvers:
            if solver.P is not None:
                self.P += solver.P

    def add_solver(self, solver: Solver):
        self.solvers.append(solver)
