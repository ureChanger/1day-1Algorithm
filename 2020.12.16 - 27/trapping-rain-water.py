class Solution:
    def trap(self, height: List[int]) -> int:
        #문제이해
        #추상화: 남은 블록들 중에서 높은 블록 찾기
        #계획하기: 1. 각자 인덱스에서 왼쪽과 오른쪽의 가장 높은 높이를 찾고 계산한다.
        ret = 0
        
        for i in range(1, len(height)-1):
            left = max(height[:i])
            right = max(height[i:])
            if left <= height[i] or right <= height[i]:
                continue
            else:
                ret += min(left, right) - height[i]
        
        return ret
