def solution(progresses, speeds):
    #문제이해
    #추상화: 뒤에 있는 기능들의 개발 완성 여부 확인
    #계획하기: 1. 각 기능이 완성 여부를 저장하는 리스트(developed: [0]*기능들의 길이)선언
    #          2. 무한 루프를 돌리며 developed에서 0이 최초로 등장하는 인덱스의 기능의 진도율이 100이상이 될 때까지 개발을 진행
    #          3. 만약 developed의 모든 원소가 1일 경우, break
    answer = []
    developed = [0]*len(progresses)
    frontFunc = 0
    
    while True:            
        #2 개발 진행
        if progresses[frontFunc] >= 100:
            funcs = 0
            for backFunc in range(frontFunc, len(progresses)):
                if developed[backFunc] == 0:
                    break
                funcs += 1
            answer.append(funcs)
            
            if 0 in developed:
                frontFunc = developed.index(0)
            else:
                break
            
        else:
            for func in range(frontFunc, len(progresses)):
                progresses[func] += speeds[func]
                if progresses[func] >= 100:
                    developed[func] = 1
    return answer
