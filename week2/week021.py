def solution(mats, park):
    # https://j-sik.tistory.com/129
    
    # 점유된 것 = 0, 아닌 것 = 1
    for parks in park:
        for i, p in enumerate(parks):
            if(parks[i] == '-1'):
                parks[i] = 1
            else:
                parks[i] = 0
    
    for row in range(0, len(park)):
        for col in range(0, len(park[0])):
            # 첫열과 첫행 부분은 넘기며, 현재 블록 값이 1인 경우만 계산
            if(row > 0 and col > 0 and park[row][col] == 1):
                park[row][col] = min(park[row][col-1], park[row-1][col], park[row-1][col-1]) + 1
    for l in park :
        print(l)
    
    answer = -1
    maxVal=-1
    for p in park:
        tmp = max(p)
        maxVal = max(maxVal, tmp)
    
    mats.sort(reverse=True)
    for m in mats:
        if(m <= maxVal):
            answer = m
            break
    
    return answer