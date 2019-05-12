# -*- coding: utf-8 -*-

import functools
from platypus import NSGAII, Problem, Real, ProcessPoolEvaluator

from Source.Optimization.optimization_objectives import optimization_objectives

def aircraft_optimization(design_input, geometry_input, engine_input, mission_input, point_performance_input, numcore = 4, iterations = 1000):
    problem = Problem(4,2,3)
    problem.types[:] = [
                Real(9.0, 11.5),
                Real(5.0, 8.0),
                Real(0.1, 0.25),
                Real(35.0, 50.0)
                ]
    problem.constraints[:] = [
                ">=1.0",
                "<=-14.0",
                ">=0.0"
                ]
    problem.directions[:] = Problem.MAXIMIZE
    problem.function = functools.partial(
            optimization_objectives, 
            design_input = design_input, 
            geometry_input = geometry_input, 
            engine_input = engine_input, 
            mission_input = mission_input, 
            point_performance_input = point_performance_input)
    with ProcessPoolEvaluator(numcore) as evaluator:
        algorithm = NSGAII(problem, evaluator=evaluator)
        algorithm.run(iterations)
    return algorithm