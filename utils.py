from tabulate import tabulate
from itertools import permutations
import numpy as np

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
    perm = permutations([i for i in range(n)], n)
    return len(list(perm))

def sort_pop(pop:np.ndarray, fitness:dict) -> np.ndarray:
    # INCOMPLETE FUNCTION
    return pop
    