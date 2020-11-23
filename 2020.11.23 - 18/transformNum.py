def solution(n):
    # 문제 이해
    # 추상화: 3으로 나눈 값에 따른 변환
    # 계획하기: 재귀 함수 transform(num) 사용 -> while문으로!(python에서 재귀함수 1,000번 이상 호출시 Recursion Error 발생 )
    #               * 기저사례: 몫이 0 일 때, rule [1,2,4]에서 나머지를 인덱스로 사용해 반환(type: string)
    #              1. num을 3으로 나눈 후,  transform(몫-1) + rule[나머지]를 반환
    
    answer = ""
    rule = ["1","2","4"]
    
    while not n == 0:
        n -= 1
        quotient = n//3
        remainder = n%3
        
        answer += rule[remainder]
        n = quotient
        
    answer = answer[::-1]
    
    return answer
