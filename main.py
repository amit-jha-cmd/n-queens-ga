import argparse
from nqueens import nqueens
from tabulate import tabulate
from tqdm import tqdm
import numpy as np
from utils import print_table

msg = 'Genetic Algorithm implementation for N-Queens problem'
parser = argparse.ArgumentParser(description=msg)
parser.add_argument('--n', type=int)
parser.add_argument('--epochs', type=int)
parser.add_argument('--m', type=int)

if __name__ == "__main__":
    args = parser.parse_args()
    n = args.n
    epochs = args.epochs
    model = nqueens(n)
    history = []
    
    for epoch in tqdm(range(epochs)):
        bs, bss, ws, wss = list(model.calc_fit(2))
        history.append((epoch, 
                        tabulate(bs, tablefmt="grid"), bss, 
                        tabulate(ws, tablefmt="grid"), wss
                        ))
        model.crossover(2)
        model.mutate()
        model.clip_pop()
        
    print_table(history)
    print("Reminder: Calculate fitness score")
    