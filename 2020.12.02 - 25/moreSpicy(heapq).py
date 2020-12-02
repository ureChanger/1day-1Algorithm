def solution(scoville, K):
    #문제 이해
    #추상화: 해당 공식의 값이 K이상이 될 때까지 계산
    #계획하기: heapq를 이용해 scoville의 원소를 차례대로 계산
    #heapq: heapq.heappush(h,(num)), heapq.heappop(h)
    import heapq
    heapq.heapify(scoville)
    
    answer = 0
    
    def getScovilleFigure(food1, food2):
        return food1 + (food2*2)
    
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        
        heapq.heappush(scoville,(getScovilleFigure(heapq.heappop(scoville), heapq.heappop(scoville))))
        answer += 1
    
    return answer
