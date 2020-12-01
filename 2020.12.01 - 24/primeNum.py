def solution(numbers):
    # 문제이해
    # 추상화: 모든 조합의 수 만들기(재귀-완전탐색)
    # 계획하기: 1. 모든 조합의 수 만들기 2. 소수인지 체크
    def makeNum(num, numList):
        #기저사례
        if len(numList) == 0:
            return 0
        
        ret = 0
        
        for i in numList:
            currentNum = num+i
            if isPrimeNum(int(currentNum)):
                ret += 1
            
            ret += makeNum(currentNum, numList.pop(i))
            
        return ret
    
    def isPrimeNum(num):
        for i in range(2, num+1):
            if num%i == 0:
                return False
            
        return True
    
    numList = list(numbers)
    answer = makeNum('',numList)
    return answer
