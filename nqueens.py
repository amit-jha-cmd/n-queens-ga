import numpy as np
import torch
import torch.functional as f
from iter_permut import perm_val
from itertools import combinations

class nqueens:
    
    def __init__(self:object, n:int, m:int = None):
        if m != None: 
            self.m = m
        else:
            self.m = perm_val(n)
        self.n = n #size of board & number of queens
        self.pop = torch.zeros((self.m, self.n * self.n), 
                               dtype=torch.int32) # gen 0
        self.hm = dict({}) # hash table to store fitness value
        
        # position n queens randomly 
        # on the chessboard
        for i in range(perm_val(n)): 
            temp = np.array([i for i in range(self.n * self.n)])
            temp = temp[np.random.choice(len(temp), 
                                         size=n, 
                                         replace=False)]
            self.pop[i, temp] = 1
            

    def calc_fit(self : object, bias:int) -> tuple:
        for gnome in self.pop:
            gnome = np.reshape(gnome, (self.n, self.n))
            ind = np.where(gnome == 1)
            ind = [(p, q) for p, q in zip(ind[0], ind[1])]
            comb = list(combinations(ind, 2))
            score = 0
            for (p, q) in comb:
                # p and q are the tuples indicating the index
                # on the chess board where n queens are placed
                if(False): # if on diag, Row, Col
                    score -= sum(p) + sum(q) + bias # reduce 
                else:
                    score += sum(p) + sum(q) + bias # increase
                    
            self.hm["-".join(str(v) for v in gnome.flatten().tolist())] = score
            
            bs = np.reshape(max(self.hm, 
                            key=self.hm.get).split("-"),
                            (self.n, self.n))
            
            bss = max(self.hm.values())
            
            ws = np.reshape(min(self.hm, 
                            key=self.hm.get).split("-"),
                            (self.n, self.n))
            
            wss = min(self.hm.values())
            
        return (bs, bss, ws, wss) # return (best_solution, score, worst solution, score)
        
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
        