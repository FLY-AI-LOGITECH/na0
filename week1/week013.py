def solution(bandage, health, attacks):
    # t 초 붕대 -> x 만큼 체력 회복
    # t 초 연속 붕대 성공 -> y만큼 추가 회복
    answer = health
    
    past_i = attacks[0][0]
    answer -= attacks[0][1]
    
    for num in attacks[1:]:
        
        print(num, answer)
        
        number = num[0] - past_i - 1
        answer += number*bandage[1] + (number//bandage[0]*bandage[2])
        
        if(answer > health):
            answer = health
            
        answer -= num[1]
        
        if(answer <= 0):
            return -1
        
        
        
        # 이전 값 저장
        past_i = num[0]
    return answer