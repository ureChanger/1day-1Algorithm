def solution(s):
    answer = 999999
    
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)//2+1):
        compressedS = compress(s, i, 1)
        if answer > len(compressedS) : answer = len(compressedS)
    return answer

def compress(s, compSize, repeat):
        #기저 사례 - s의 길이가 compSize보다 작을 경우
        if len(s) < compSize:
            return s
    
        prevS = s[0:compSize]
        nextS = s[compSize:]
        
        #앞의 기준 문자와 다음 문자가 같지 않을 경우
        if not prevS == nextS[0:compSize]:
            #처음
            if repeat == 1:
                return prevS+compress(nextS, compSize, 1)
            #압축 문자 찾음
            else:
                return str(repeat)+prevS+compress(nextS, compSize, 1)
        
        return compress(nextS, compSize, repeat+1)
