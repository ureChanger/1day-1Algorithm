def solution(numbers):
    answer = []
    
    for pivot in range(len(numbers)):
        for i in range(pivot+1, len(numbers)):
            sum = numbers[pivot] + numbers[i]
            if not sum in answer:
                answer.append(sum)
    
    answer.sort()
    
    return answer
