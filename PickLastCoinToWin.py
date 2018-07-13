test_cases = int(input())
for case in range(test_cases):
    n, x, y =  [int(i) for i in input().split()]

    def play(n, x, y):
        dp = {}
        my_turn = True
        for j in range(1, max(x, y)):
            dp[-j] = True  
        dp[0] = False 
        i = 1 
        while True:  
            dp[i] = not dp[(i-1)] or not dp[(i-x)] or not dp[(i-y)] 
            if i == n:
                break
            i +=1
        return dp[n]

    if (play(n, x, y)):
        print('G')
    else:
        print('N')