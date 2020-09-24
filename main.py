import argparse
from nqueens import nqueens
from tabulate import tabulate
from tqdm import tqdm
import numpy as np
from print_table import print_table

msg = 'Genetic Algorithm implementation for N-Queens problem'
parser = argparse.ArgumentParser(description=msg)
parser.add_argument('--n', 
                    type=int,
                    help="Specify n in n-queens")
parser.add_argument('--epochs', 
                    type=int, 
                    help="Specify number of Generations to run.")
parser.add_argument('--m',
                    type=int,
                    help="Specify size of a geneation. It has to be greater than (n*n)Cn")

if __name__ == "__main__":
    args = parser.parse_args()
    n = args.n
    epochs = args.epochs
    model = nqueens(n)
    history = []
    
    for epoch in tqdm(range(epochs)):
        sol_ele = model.calc_fit(2)
        
        # temp -------------------------------------
        sol_ele = [epoch,  tabulate(np.zeros((n, n)), 
                    tablefmt="grid"), 100,
                    tabulate(np.ones((n, n)), 
                    tablefmt="grid"), 0]
        # ------------------------------------------
        
        history.append(sol_ele)
        model.crossover(5)
        model.mutate()
        model.sort_pop()
        
    print_table(history)
    print("Reminder: Calculate fitness score")
    