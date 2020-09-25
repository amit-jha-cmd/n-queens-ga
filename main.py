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
parser.add_argument('--history', type=bool)

if __name__ == "__main__":
    args = parser.parse_args()
    n = args.n
    epochs = args.epochs
    history = args.history
    model = nqueens(n)
    history_lst = []
    
    for epoch in tqdm(range(epochs)):
        bs, bss, ws, wss = list(model.calc_fit(2))
        if(history):
            history_lst.append((epoch, 
                            tabulate(bs, tablefmt="grid"), bss, 
                            tabulate(ws, tablefmt="grid"), wss
                            ))
        model.crossover(2)
        model.clip_pop()
        
    if(history):
        print_table(history_lst)
    print("Reminder: Calculate fitness score")
    