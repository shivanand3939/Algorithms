#https://practice.geeksforgeeks.org/problems/paths-to-reach-origin/0
test_cases = input()

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*factorial(n-1)

for case in range(int(test_cases)):
    m, n = [ int(i) for i in input().split()]
    m_n = factorial(m+n)
    m_ = factorial(m)
    n_ = factorial(n)
    print(int(m_n/(n_*m_)))