test_cases = int(input())
for case in range(int(test_cases)):
    L, K = [ int(i) for i in input().split()]
    text = input()
    def is_palindrome(res):
        if res == reversed(res):
            return True
        else:
            return False

    def solve_dp(text, L, K, cache={}):
        if K<0:
            return 0
        elif L==0 or L==1: 
            return 1 
        if text[0] == text[-1]:
            if text[1:-1] not in cache:
                cache[text[1:-1]] = solve_dp(text[1:-1], L-2, K, cache)
            return cache[text[1:-1]]
        else: 
            if text[:-1] not in cache:
                cache[text[:-1]] = solve_dp(text[:-1], L-1, K-1, cache)
            if cache[text[:-1]]:
                return cache[text[:-1]]
            else:
                if text[1:] not in cache:
                    cache[text[1:]] = solve_dp(text[1:], L-1, K-1,cache)
                return cache[text[1:]]

    print(solve_dp(text,L, K))