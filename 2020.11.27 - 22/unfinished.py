def solution(participant, completion):
    completion += "zzzzzzzzzzz"
    completion.sort()
    participant.sort()
    
    for i, j in zip(participant, completion):
        if i != j :
            print(i)
            return i
