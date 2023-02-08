from objects.Experiment import Experiment
from objects.Source import Source
from solvers.ExpSolver import ExpSolver
from solvers.Solver import Solver

exp = Experiment('Test', 20, 20, 340, 100000, 200, 200)

source_1 = Source(3, 5)
exp.add_source(source_1)

source_2 = Source(18, 14)
exp.add_source(source_2)

solver_1 = Solver(exp, source_1)
solver_2 = Solver(exp, source_2)

exp_solver = ExpSolver(exp)
exp_solver.add_solver(solver_1)
exp_solver.add_solver(solver_2)

solver_1.solve(100, 100, 0.01, 0.01)
solver_2.solve(100, 100, 0.01, 0.01)
exp_solver.solve_global()

exp.render_room(exp_solver.P, exp_solver.X, exp_solver.Y)