#https://practice.geeksforgeeks.org/problems/sum-of-all-substrings-of-a-number/0

test_cases = input()
for case in range(int(test_cases)):
    text = input()
    nums = [int(each) for each in text]
    score = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1): 
            score += int(text[i:j])
    print(score)