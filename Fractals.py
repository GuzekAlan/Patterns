"""
TODO
"""
import matplotlib.pyplot as plt
import random

class Fractal:
    """
    Class for creating fractals
    """

    def __init__(self, set_of_params: list[tuple], probabilities: list[int]):
        """
        Creating starting values and assignings data
        :param:``set_of_params`` - list of tuple of parameters to generating funciton
        :param:``probabilietis`` - probabilities of choosing given tuple
        """
        if len(set_of_params) != len(probabilities):
            raise ValueError("Number of probabilities and sets of params must be equal!")
        if sum(probabilities) != 1:
            raise ValueError("Probabilities must sum up to 1")
        for params in set_of_params:
            if len(params)  != 6:
                raise ValueError("One of sets is different size than 6")
        self.x_values: list[int] = [0]
        self.y_values: list[int] = [0]
        self.sets: list[tuple] = set_of_params
        self.probs: list[int] = probabilities

    def create_points(self, N: int = 1000, copy: bool = True) -> tuple[list]:
        """
        Creates points using parameters and probabilieties
        :param:``N`` - size of created points
        :param:``copy`` - working on object lists (False) or creating from 0 (True)
        """
        x: list[int] = [0] if copy else self.x_values
        y: list[int] = [0] if copy else self.y_values
        for _ in range(N):
            a, b, c, d, e, f = random.choices(self.sets, weights=self.probs)[0]
            x.append(a*x[-1] + b*y[-1] + c)
            y.append(d*x[-2] + e*y[-1] + f)
        return x, y

    def plot_points(self, filepath: str, color: str = 'balck', data: tuple[list] = None):
        """
        Saving created fractal
        :param:``filepath`` - relative path with name to save results
        :param:``color`` - color of ploted results
        :param:``data`` - points to plot ( if ``None`` it will use object values )
        """
        if not data:
            data = (self.x_values, self.y_values)
        plt.figure()
        plt.scatter(data[0], data[1], marker='.', c=color)
        plt.savefig(filepath)
