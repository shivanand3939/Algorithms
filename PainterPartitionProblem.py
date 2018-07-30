import numpy as np

test_cases = int(input())
for case in range(test_cases):
    partitions, len_ = [ int(each) for each in input().split()]
    arr = [ int(each)  for each in input().split()]

    dp = {}
    for i, v in enumerate(arr):
        dp[(i, 1)] = sum(arr[i:])
    
    if partitions == 1:
        print(dp[(0, 1)])
    is_end = False
    for i in range(2, partitions+1):
        for k, v in enumerate(arr): 
            min_ = np.inf
            for j in range(k+1, len(arr)):
                if min_ > max(sum(arr[k:j]), dp[( j, i-1)]):
                    min_ = max(sum(arr[k:j]), dp[( j, i-1)])
            if min_ == np.inf:
                dp[(k, i)] = dp[(k, i-1)] 
            else:
                dp[(k, i)] = min_
            if (0, partitions) in dp:  
                print(dp)
                print(dp[(0, partitions)])
                is_end = True
                break
        if is_end:
            break