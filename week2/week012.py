def go(m_direct, m_count, m_position, park):
    revert_position = list(m_position)
    
    if(m_direct == 'E'):
        account = [0, 1]
    elif(m_direct == 'W'):
        account = [0, -1]
    elif(m_direct == 'N'):
        account = [-1, 0]
    elif(m_direct == 'S'):
        account = [1, 0]
    
    while(m_count):
        m_position[0] += account[0]
        m_position[1] += account[1]
        if(m_position[0] > len(park)-1 or m_position[0] < 0
           or m_position[1] > len(park[0])-1 or m_position[1]< 0
           or park[m_position[0]][m_position[1]] =='X'):
            break
        m_count -= 1
    if(m_count == 0):
        return m_position
    else:
        return revert_position
    

def solution(park, routes):
    
    # S 위치에 대한 값 저장
    i, j = 0, 0
    for p in park:
        if 'S' in p:
            j = p.index('S')
            break
        i += 1
    
    # routes 진행
    for r in routes:
        i, j = go(r[0], int(r[2]), [i, j], park
                  
    
    answer = [i, j]
    return answer