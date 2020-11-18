def pick(n, picked, toPick):
    print("Welcome!")
    answer = []
    if toPick == 0:
        return picked
    if(len(picked) == 0):
        smallest = 0
    else:
        smallest = picked[-1]+1
    for i in range(smallest, n):
        picked.append(i)
        print("i : " + str(i) + " / toPick : " + str(toPick))
        answer.append(pick(n, picked, toPick-1))
        picked.remove(i)
    print("toPick : " + str(toPick))
    print(answer)
    return answer

pick(7, [], 5)
