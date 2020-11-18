def findCombination(num, toPick, pickedNum):
    comList = []
    beforeList = []
    
    for i in range(pickedNum, num - toPick+1):
        print("toPick : " + str(toPick))
        print(i)
        if(toPick == 1):
            comList.append([i])
        else:
            beforeList = findCombination(num, toPick -1, i+1)
            for j in beforeList:
                j = [i] + j
                comList.append(j)
    return comList

answer = findCombination(7, 5, 0)

print(answer)
print("총합 : "+str(len(answer)))
print([0, 1, 2, 3, 4, 5, 6])
