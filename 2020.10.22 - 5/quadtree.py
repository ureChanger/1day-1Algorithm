#분할 정복을 이용한 쿼드 트리 뒤집기 문제 알고리즘
def reverse(compressed, idx):
  ret = compressed[idx]
  
  #기저사례
  if(ret == 'b' or ret == 'w'):
    return ret
    
  idx += 1
  upperLeft = reverse(compressed, idx)
  idx += len(upperLeft)
  upperRight = reverse(compressed, idx)
  idx += len(upperRight)
  lowerLeft = reverse(compressed, idx)
  idx += len(lowerLeft
  lowerRight = reverse(compressed, idx)
  
  return 'x'+upperLeft+upperRight+lowerLeft+lowerRight
