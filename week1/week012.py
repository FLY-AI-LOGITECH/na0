def solution(arr):
    answer = []
    for i, num in enumerate(arr):
        if(len(answer) == 0 or answer[-1] != num):
            answer.append(num)
    return answer