def solution(prices):
    #문제 이해
    #추상화: 뒤의 원소들 중에서 더 작은 원소가 나오는 곳까지의 거리 찾기
    #계획하기: 1. prices를 기준으로 반복문을 돌림
    #          2. prices뒤의 원소들 중 pivot과 더 작은 값의 인덱스와의 차를 answer에 더함
    answer = []
    maxTime = len(prices)
    
    for pivot in range(maxTime):
        time = maxTime-pivot-1
        for nextNum in range(pivot+1, maxTime):
            if prices[nextNum] < prices[pivot]:
                time = nextNum-pivot
                break
                
        answer.append(time)
        
    return answer
