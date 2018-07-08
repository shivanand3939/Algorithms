#https://practice.geeksforgeeks.org/problems/minimal-moves-to-form-a-string/0
from collections import deque
test_size = input(" Enter the size of Test Cases ")
user_inputs = []
for i in range(int(test_size)):
    user_input = input(" Enter the Test Cases ")
    user_inputs.append(user_input)
    
for text in user_inputs:
#text = "abcabca"
    step = 1

    word = text[0]
    stack = deque([(word, step)])
    while True:
        word, step = stack.popleft()
        if word == text:
            print(step)
            break
        else:
            word_add = word+text[len(word)] 
            if word_add == text[:len(word_add)]: 
                stack.append((word_add, step+1))
            word_append = word+word
            if word_append == text[:len(word_append)]:
                stack.append((word_append, step+1)) 