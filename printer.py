def solution(priorities, location):
    #문제이해
    #추상화: 남은 목록 중에서 인쇄할 문서 찾기
    #계획: 1. priorities의 길이만큼 원소가 0인 리스트(printed)를 선언 2. 무한 루프를 돌리며 printed의 인덱스에 순서를 입력
    printed = [0]*len(priorities)
    idx = 0
    num = 1
    
    while len(priorities) != 0:
        if priorities[0] < max(priorities):
            priorities.append(priorities[0])
            del priorities[0]
        else:
            printed[idx%len(printed)] = num
            num += 1
            del priorities[0]
        
        idx += 1
        
    return printed[location]
