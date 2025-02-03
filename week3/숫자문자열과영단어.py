def solution(s):
    answer = 0
    i = 0
    while(i < len(s)):
        print(i - len(s)-1)
        if(s[i].isdigit()):
            answer *= 10
            answer += int(s[i])
            i += 1
        else:
            jump = 0
            answer *= 10
            if(s[i] == 'z'):
                jump = 4
            elif(s[i] == 'o'):
                jump = 3
                answer += 1
            elif(s[i] == 't' and s[i+1] == 'w'):
                jump = 3
                answer += 2
            elif(s[i] == 't' and s[i+1] == 'h'):
                jump = 5
                answer += 3
            elif(s[i] == 'f' and s[i+1] == 'o'):
                jump = 4
                answer += 4
            elif(s[i] == 'f' and s[i+1] == 'i'):
                jump = 4
                answer += 5
            elif(s[i] == 's' and s[i+1] == 'i'):
                jump = 3
                answer += 6
            elif(s[i] == 's' and s[i+1] == 'e'):
                jump = 5
                answer += 7
            elif(s[i] == 'e'):
                jump = 5
                answer += 8
            elif(s[i] == 'n'):
                jump = 4
                answer += 9
            i += jump
    return answer