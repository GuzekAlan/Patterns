import fractions
import Patterns
import Fractals

def pattern_example():
    """Example of Pattern class using rule 94"""
    pattern = Patterns.Pattern(N=30, rule=94)
    pattern.evolution(10, True)

def leaf_example():
    leaf = Fractals.Fractal(
        ((0,0,0,0,0.16,0), 
        (0.2,-0.26,0,0.23,0.22,1.6), 
        (-0.15,0.28,0,0.26,0.24,0.44), 
        (0.85,0.04,0,-0.04,0.85,1.6)), 
        (0.01, 0.07, 0.07, 0.85))
    leaf.create_points(N=4000, copy=False)
    leaf.plot_points('./img/LeafFracrtal.png', 'green')

if __name__ == '__main__':
    pattern_example()
    leaf_example()