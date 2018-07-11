import numpy as np
test_cases = int(input())

def dp(k, cache = {}):
        if k in cache:
            return cache[k]
        elif k < 0:
            return np.inf
        elif k == 0:
            return 0
        else:
            min_ = np.inf
            for i in arr:
                if min_ > dp(k-i, cache) :
                    min_ = 1 + dp(k-i, cache)
            cache[k] = min_
            return min_
        
for case in range(test_cases):
    N, K = [ int(i) for i in input().split()]
    #K = 20
    #N = [6, 3, 4, 2]
    arr = [int(i) for i in input().split()] 
    if dp(K) == np.inf:
        print('Not possible to collect coins that sum upto to the given Sum')
    else:
        print('Minimum number of coins are ', dp(K))
