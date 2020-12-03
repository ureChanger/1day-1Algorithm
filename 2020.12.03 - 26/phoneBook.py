def solution(phone_book):
    #문제이해
    #추상화: 뒤의 번호들과 비교
    #계획하기: phone_book를 차례로 뒤에 위치한 원소들의 접두어들과 비교
    answer = True
    
    phone_book.sort()
    
    for num in range(len(phone_book)):
        phone_num = phone_book[num]
        for nextNum in range(num+1, len(phone_book)):
            if phone_num == phone_book[nextNum][:len(phone_num)]:
                return False
    
    return answer
