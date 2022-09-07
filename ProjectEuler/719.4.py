from math import isqrt

def recurse(n, d, m):
  a = int(d)
  if n == a: return True
  if n > a: return False
  for i in range(1,m+1):
    a = int(d[:i])
    if n>=a and recurse(n-a, d[i:], m): return True
  return False

def f(n):
  return sum(x**2 for x in range(4,isqrt(n)+1) if x%9<2 and recurse(x,str(x**2), len(str(x))))

print(f(10**4))
print(f(10**12))