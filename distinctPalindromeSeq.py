#https://practice.geeksforgeeks.org/problems/distinct-palindromic-substrings/0
test_cases = int(input())

for case in range(test_cases):
    text = input()
    subs = []
    count = 0
    for i in range(len(text)):
        for j in range(i, len(text)):
            sub_text = text[i:j+1]
            is_palin = True
            for k in range(int(len(sub_text)/2)):
                if sub_text[k] != sub_text[-1-k]:
                    is_palin = False
                    break
            if is_palin and sub_text not in subs: 
                count += 1
                subs.append(sub_text)
    print(count)
