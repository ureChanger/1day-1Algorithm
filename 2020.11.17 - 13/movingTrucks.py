def solution(bridge_length, weight, truck_weights):
    #문제이해
    #추상화: 남은 트럭들 중 넣을 수 있는 타이밍 잡기
    #계획: 1. [0,0,0,0,0,0,0] -> [1:]+([0] or [truck_weights[car]] 2. del truck_weights[0] 3. truck_weights의 길이가 0이면 종료  
    
    answer = 0
    bridge = [0]*bridge_length
    bridgeWeight = 0
    
    while True :
        if len(truck_weights) == 0 and bridgeWeight == 0:
            break
            
        answer += 1
        if bridge[0] != 0:
            bridgeWeight -= bridge[0]
        del bridge[0]
        nextNum = 0
        
        if truck_weights: 
            if bridgeWeight + truck_weights[0] <= weight:
                nextNum = truck_weights[0]
                bridgeWeight += truck_weights[0]
                del truck_weights[0]
                
        bridge.append(nextNum)
    return answer
