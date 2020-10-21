def solution(board, moves):
    
    answer = 0
    picked = [999]
    
    for i in moves:
        #인형 뽑기
        for j in range(len(board)):
            if not board[j][i-1] == 0 :
                picked.append(board[j][i-1])
                board[j][i-1] = 0
                
                print(len(board))
                
                #터트리기
                if(picked[-2] == picked[-1]):
                    del picked[-2]
                    del picked[-1]
                    answer += 2
            
                break
    return answer
