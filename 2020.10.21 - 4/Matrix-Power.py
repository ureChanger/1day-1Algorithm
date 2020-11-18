# 정방행렬을 표현하는 SquareMatrix 클래스가 있다고 가정
class SquareMatrix

# n*n크기의 항등행렬을 반환하는 identity() 함수
SquareMatrix identity(n)

# A^m을 반환

# 분할 정복을 이용해 거듭제곱을 구하는 아이디어 : A^m = A^(m/2) * A^(m/2)

SquareMatrix pow(A, m):
  #기저 사례
  if m==0: return identity(len(A))
  
  # m이 홀수인 경우 A*A^(m-1) 와 A^(m//2)*A^(m//2+1)에서 선택
  # 후자가 더 빠를 것 같지만 pow() 함수를 2번 호출함으로 pow()의 호출 횟수는 m에 대해 선형적으로 증가
  # O표기법으로 보면 m-1을 곱한 것과 같음 따라서 A*A^(m-1)가 더 빠른 계산
  if m%2 != 0: return pow(A, m-1)*A
  
  SquareMatrix half = pow(A, m//2)
  
  return half*half
