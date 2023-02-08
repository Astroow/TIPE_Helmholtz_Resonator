import math

from numpy import ndarray


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


def closest_value(ilist: ndarray, ivalue: float):
    difference = lambda input_list: abs(input_list - ivalue)
    return min(ilist, key=difference)