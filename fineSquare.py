#77.0/100.0 오답:1개 시간초과:3개 -> O(n)이 아닌 O(1)로 계산해야 함

def solution(w,h):
    #w,h를 좌표로 생각
    #y를 구하는 방정식
    def getY(x):
        y = h/w*x
        return y
    
    answer = 0
    
    for x in range(w):
        answer += int(getY(x))
    
    return answer*2
