#code
test_cases = int(input())

for case in range(test_cases):
    bin_str = input()
    if int(bin_str)/int('1'*len(bin_str)) == 1:
        print(-1)
    else:
        scores = []
        for each in bin_str:
            if int(each) == 1:
                if len(scores) == 0:
                    scores.append(0)
                else:
                    score = scores[-1] - 1
                    if score < 0:
                        scores.append(0)
                    else:
                        scores.append(score)
            else:
                if len(scores) == 0:
                    scores.append(1)
                else:
                    score = scores[-1] + 1
                    scores.append(score)
        print(max(scores))