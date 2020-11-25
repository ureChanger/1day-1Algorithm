def solution(lines):
    #문제이해
    #추상화: 가장 많은 범위에 속하는 1초의 순간 찾기
    #계획하기: 1. 각 로그들의 시작과 끝 시간을 리스트로 만들고, 그 리스트들을 원소로 하는 리스트(time)를 만듦
    #         2. 각 시작과 끝을 정렬해 검사해볼 타임 리스트(testTime)를 만듦
    #         3. testTime의 원소들을 기준으로 반복문을 실행시켜 time~time+0.999에서 포함되는 time의 원소들을 찾는다
    #         4. 가장 많은 원소를 가진 시간의 원소를 반환
    time = []
    for i in range(lines):
        prossesedTime = i.split(' ')
        time.append([])
    answer = 0
    return answer
