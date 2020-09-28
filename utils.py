from tabulate import tabulate
from itertools import permutations
import numpy as np
import math

def print_table(history):
    print(tabulate(history, 
                   colalign=(["center" for i in range(5)]),
                   tablefmt="fancy_grid",
                   headers=["Epoch", 
                            "Best Solution",
                            "Score",
                            "Worst Solution", 
                            "Score"]
                   )
          )


def perm_val(n:int) -> int:
    # perm = permutations([i for i in range(n)], n)
    perm = math.factorial(n * n)
    return perm

def sort_pop(pop:np.ndarray, fitness:dict) -> np.ndarray:
    # INCOMPLETE FUNCTION
    return pop

def fitness_condition(loc1:tuple, loc2:tuple) -> bool:
    if(
        (loc1[0] + 1 == loc2[0] and loc1[1] + 1 == loc2[1]) or
        (loc1[0] - 1 == loc2[0] and loc1[1] - 1 == loc2[1]) or
        (loc1[0] - 1 == loc2[0] and loc1[1] + 1 == loc2[1]) or
        (loc1[0] + 1 == loc2[0] and loc1[1] - 1 == loc2[1])
    ):
        return True
    
    elif((loc1[0] == loc2[0]) or (loc1[1] == loc2[1])):
        return True
    
    else:
        return False
    