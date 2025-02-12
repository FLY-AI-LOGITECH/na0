def solution(numbers):
    answer = []
    for i, n in enumerate(numbers):
        for nn in numbers[i+1:]:
            answer.append(n+nn)
            
    answer = set(answer)
    answer = sorted(list(answer))
    return answer
