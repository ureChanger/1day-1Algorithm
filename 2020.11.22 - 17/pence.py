def solution(boards):
  def solve(left, right):
    if left==right:
      return boards[left]

    mid = (left+right)//2
    ret = max(solve(left, mid), solve(mid+1, right))

    lo = mid, hi = mid+1
    height = min(boards[lo], boards[hi])
    ret = max(ret, height*2)

    while left < lo or right > hi:
      if hi<right and (lo == left or boards[lo-1] < boards[hi+1]): 
        hi += 1
        height = min(height, boards[hi])
      else:
        lo -= 1
        height = min(height, boards[lo])

      ret = max(ret, (hi-lo+1)*height)

    return ret

answer = solve(0, len(boards)-1)

return answer
