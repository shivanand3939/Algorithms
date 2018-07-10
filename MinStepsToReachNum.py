#https://practice.geeksforgeeks.org/problems/minimum-number-of-steps-to-reach-a-given-number/0

test_cases = input()

for case in range(int(test_cases)):
    num = int(input())

    i=0
    sum_nums = 0
    while True:
        sum_nums += i
        if sum_nums >= num: 
            break
        i += 1

    if (sum_nums - num)%2 == 0: 
        print(i)
    else:
        print(i+1)
