import numpy as np 

sizes = [1, 2, 3 ,4]
no_of_ele = len(sizes) - 1

dp_mul = [ [ 0 for i in range(no_of_ele)] for j in range(no_of_ele)]

for i in range(1, no_of_ele):
    for j in range(no_of_ele-i): 
        min_score = np.inf
        for k in range(j, i+j): 
            score = dp_mul[j][k] + sizes[j]*sizes[k+1]*sizes[i+j+1] + dp_mul[k+1][i+j]
            if min_score > score:
                min_score = score 
                best_p = k
        dp_mul[j][i+j] = min_score 

print("Minimum Number of multiplications: ", dp_mul[0][-1])