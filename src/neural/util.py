from typing import List
from math import exp


def dot_product(xs: List[float], ys: List[float]) -> float:
    return sum(x * y for x, y in zip(xs, ys))


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + exp(-x))

# 参考：http://nonbiri-tereka.hatenablog.com/entry/2014/06/30/134023
def derivative_sigmoid(x: float) -> float:
    sig: float = sigmoid(x)
    return sig * (1 - sig)
