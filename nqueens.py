import numpy as np
import torch
import torch.functional as f
from iter_permut import perm_val

class nqueens:
    
    def __init__(self:object, n:int, m:int = None):
        if m != None: 
            self.m = m
        else:
            self.m = perm_val(n)
        self.n = n #size of board & number of queens
        self.pop = torch.zeros((self.m, self.n * self.n), 
                               dtype=torch.float32) # gen 0
        self.hm = dict({}) # hash table to store fitness value
        
        # position n queens randomly 
        # on the chessboard
        for i in range(perm_val(n)): 
            temp = np.array([i for i in range(self.n * self.n)])
            temp = temp[np.random.choice(len(temp), 
                                         size=n, 
                                         replace=False)]
            self.pop[i, temp] = 1
        
    # def initialize(self : object):
    #     # assign init pop to self.pop
    #     print("Initialized")
        
    def calc_fit(self : object)-> tuple:
        # if not on any row/col/diagonal
        # assign + sum(all pair combination) to that soln
        # else
        # assign - sum (for all such pair) + sum (normal pairs) to the soln
        # return best solution
        pass
        
    def crossover(self : object, k: int):
        # select k best parents
        # generate offsprings from this set using
        # single point crossover
        # assign pop + offsprings to self.pop
        pass
        
    def mutate(self : object):
        # probabilistic mutation 
        # assign the population + mutated values to self.pop
        pass
        
    def sort_pop(self : object):
        # sorted the pop based on fitness score
        # assign the top n*n gnomes from sorted pop
        pass
        