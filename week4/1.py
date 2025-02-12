import math

def solution(n):
    answer = 0
    for i in range(2, n + 1):
        flag = False
        for k in range(2, int(math.sqrt(i)+1)):
            if(i % k == 0):
                flag = True
                break
        if(flag == False):
            answer += 1
    return answer
