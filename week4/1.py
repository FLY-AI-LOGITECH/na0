import math

def solution(n):
    answer = 0
    for i in range(2, n + 1):
        tmp = 0
        for k in range(2, i):
            tmp += 1
            if(i % k == 0):
                break
        if(tmp == i-2):
            answer += 1
    return answer
