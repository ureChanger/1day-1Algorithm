#1+2+3+4+...+n = (1+2+...+n/2)+((n/2+1)+(n/2+2)+...+(n/2+n/2))
#2*(1+2+...+n/2) + n^2//4

def fastSum(n):
  if n==1: return 1
  if n%2==0: return fastSum(n-1)+n
  
  return 2*fastSum(n//2)+n*n//4
