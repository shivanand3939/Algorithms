#https://practice.geeksforgeeks.org/problems/close-to-perfection/0

test_case = int(input())

for case in range(test_case):
    len_ = int(input())
    arr = [ int(i) for i in input().split()]
    max_ = 0
    for i in range(len(arr) - 1):
        start, end = i, i
        diff = arr[i] - arr[i+1]
        is_first = True
        is_end = True
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                continue
            elif (is_first or (arr[i] - arr[j]) == diff ):
                if is_first:
                    is_first = False
                    diff = (arr[i] - arr[j]) 
                    if abs(diff) != 1:
                        break
                end = j 
            else:
                is_end = False
                break
        if max_ < j - i:
            if not is_end:
                max_ = j - i 
            else:
                max_ = j - i + 1  
    print(max_)
        