"""
Interesting pattern generators
"""
import random
import matplotlib.pyplot as plt


class NumberPattern:
    """
    Class for creating intreresting ptterns using rules represented as 8-bit number
    """
    def __init__(self, N: int, rule: int, is_random: bool = False) -> None:
        """
        Initializing parameters of ``NumberPattern``
        :param:``N`` - width of the pattern
        :param:``rule`` - number [0-255] defining rule
        :param:``is_random`` - creating first iteration randomly (True) or middle one is 1 (False)
        """
        if(is_random):
            self.cells = [random.randint(0, 1) for _ in range(N)]
        else:
            self.cells = [1 if i == N//2 else 0 for i in range(N)]
        self.rule = {(3*'0'+bin(7-i)[2:])[-3:]: v for i, v in enumerate((8*'0'+bin(rule)[2:])[-8:])}
        self.__N = N

    def evolve(self) -> None:
        """
        Using rule to make 1 step
        """
        new_cells = []
        for i, cell in enumerate(self.cells):
            left = self.cells[i-1]
            right = self.cells[(i+1)%self.__N]
            thing = str(left) + str(cell) + str(right)
            new_cells.append(self.rule[thing])
        self.cells = [int(i) for i in new_cells]

    def evolution(self, n_iter: int = 1, _print: bool = False) -> None:
        """
        Using rule to make many evolutons with optional printing
        :param:``n_iter`` - number of evolutions to make
        :param:``_print`` - print results (True) or not (Flase)
        """
        if _print:
                print(self)
        for _ in range(n_iter):
            self.evolve()
            if _print:
                print(self)  

    def __str__(self) -> str:
        return ''.join(['*' if i==1 else ' ' for i in self.cells])


class FunctionPattern:
    """
    Class for creating patterns using patrameters of functions
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

leaf_params_and_probs = (
        ((0,0,0,0,0.16,0), 
         (0.2,-0.26,0,0.23,0.22,1.6), 
         (-0.15,0.28,0,0.26,0.24,0.44), 
         (0.85,0.04,0,-0.04,0.85,1.6)), 
        (0.01, 0.07, 0.07, 0.85))