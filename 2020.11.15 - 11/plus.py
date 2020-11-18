#정수 배열 numbers에서 서로다른 인덱스의 숫자를 더한 모든 결과 값을 넣은 배열(answer)을 반환.

def solution(numbers):
    answer = []
    
    for pivot in range(len(numbers)):
        for i in range(pivot+1, len(numbers)):
            sum = numbers[pivot] + numbers[i]
            if not sum in answer:
                answer.append(sum)
    answer.sort()
    
    return answer
