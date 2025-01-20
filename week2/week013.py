def solution(name, yearning, photo):
    
    dictionary = { n : y for n, y in zip(name, yearning)}
    
    answer = []
    for photos in photo:
        count = 0
        for p in photos:
            num = dictionary.get(p)
            count += num if num else 0
        answer.append(count)
            
    return answer