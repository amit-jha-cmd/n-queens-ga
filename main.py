import argparse
from nqueens import nqueens
from tabulate import tabulate
from tqdm import tqdm
import numpy as np

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
        # calculate fitness
        best_sol = model.calc_fit()
        history.append([epoch, 
                        tabulate(np.zeros((n, n)), 
                                 tablefmt="grid"), 
                        100,
                        tabulate(np.ones((n, n)), 
                                 tablefmt="grid"), 
                        0
                        ])
        # crossover
        model.crossover(5)
        # mutation
        model.mutate()
        # sort and clip the population
        model.sort_pop()
        
    print(tabulate(history, 
                   colalign=("center", 
                             "center",
                             "center",
                             "center",
                             "center"),
                   tablefmt="fancy_grid",
                   headers=["Epoch", 
                            "Best Solution",
                            "Score",
                            "Worst Solution", 
                            "Score"]
                   )
          )
    print("Reminder: Calculate fitness score")
    