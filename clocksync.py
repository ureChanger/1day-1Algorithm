#문제:시계 맞추기
#모든 시계가 12시를 가르키기 위해 스위치를 눌러야 하는 최소한의 수
#12시로 만들 수 없다면 -1 반환

#maxSwitch = 10
#linked = [...]
#clock = [...]

def Aligend(clock):
  for i in clock:
  if not i == 12:
    return false
  return true
  
def push(clock, switch):
  for i in linked[switch]:
    clock[i] += 3
    
def solution(clock, switch):
  if switch==10:
    return Aligend?0:99999
  ret = 99999
  for cnt in range(4):
    ret = min(ret, cnt+solution(clock, switch+1)
    push(clock, switch)
  return ret
