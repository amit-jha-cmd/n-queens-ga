import argparse
from .nqueens import nqueens


msg = 'Genetic Algorithm implementation for N-Queens problem'
parser = argparse.ArgumentParser(description=msg)
parser.add_argument('n', type=int)


if __name__ == "__main__":
    args = parser.parse_args()
    n = args.n
    model = nqueens(n)
    
    