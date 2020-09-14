import numpy as np

class nqueens:
    def __init__(self:object, n:int):
        self.n = n #size of board & number of queens
        self.pop = None # population of gnomes
        self.hm = None # hashmap (soln, fitness)
        
    def initialize(self : object):
        # assign init pop to self.pop
        print("Initialized")
        
    def fitness(self : object):
        # if not on any row/col/diagonal
        # assign + sum(all pair combination) to that soln
        # else
        # assign - sum (for all such pair) + sum (normal pairs) to the soln
        print("fitted")
        
    def crossover(self : object, k: int):
        # select k best parents
        # generate offsprings from this set using
        # single point crossover
        # assign pop + offsprings to self.pop
        print("crossed")
        
    def mutation(self : object):
        # probabilistic mutation 
        # assign the population + mutated values to self.pop
        print("mutated")
        
    def sort_pop(self : object):
        # sorted the pop based on fitness score
        # assign the top n*n gnomes from sorted pop
        print("sorted")