#5x5 보글 게임판에서 단어(word)를 찾는 재귀 호출 알고리즘

#상대 좌표 정의 - 재귀 함수에서 순서에 따라 다음 좌표를 인자로 호출하기 위함
dx = [-1,-1,-1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]

#해당 위치에서 주어진 단어가 시작하는지 반환
def hasWord(y, x, word):
  #base case1 - in map?
  if y<0 or y>4 or x<0 or x>4 :
    return False
           
  #base case2 - first coincide?
  if not board[y][x] == word[0] :
    return False
    
  #base case3 - word length == 1?
  if len(word) == 1:
    return True
    
  #check 8 spaces around:
  for direction in range(0, 8):
    nextY = y+dy[direction], nextX = x+dx[direction]
    if hasWord(nextY, nextX, word[1:]:
      return True
  
  return False
