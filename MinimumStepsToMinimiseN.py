#https://practice.geeksforgeeks.org/problems/minimum-steps-to-minimize-n-as-per-given-condition/0
import numpy as np

test_cases = int(input())

for case in range(test_cases):
    num = int(input())
    res = {}
    for i in range(num+1):
        if i <= 1:
            res[i] = 0
        elif i <= 3:
            res[i] = 1
        else:
            res[i] = min(res[i-1], res[i/2] if i%2 == 0 else np.inf,  res[i/3] if i%3 == 0 else np.inf) + 1
    print(res) 