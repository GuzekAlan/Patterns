"""
Interesting Patterns and generators
"""
import random


class Pattern:
    """
    Class for creating intreresting ptterns usign rules.
    """
    def __init__(self, N: int, rule: int, is_random: bool = False) -> None:
        """
        Initializing parameters of ``Patterns``
        :param:``N`` - width of the Pattern
        :param:``rule`` - number [0-255] defining rule of Pattern
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