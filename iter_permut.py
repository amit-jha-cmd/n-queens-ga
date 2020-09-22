from itertools import permutations


def perm_val(n:int) -> int:
    perm = permutations([i for i in range(n)], n)
    return len(list(perm))