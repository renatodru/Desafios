import time
def isSnumber (NS, N) :
  if NS <= N : return NS == N
  div = 10
  while True :
    r = NS % div
    if r >= N : return False
    if isSnumber(NS // div, N - r) : return True
    div *= 10
    
def T(N):
	time1 = time.time()
	c = 0
	s = 0
	for i in range(9,(10**N)+1,9):
		if isSnumber(i*i,i):
			c+=1
			s+=i*i
			print(i)
		i+=1
		if isSnumber(i*i,i):
			c+=1
			s+=i*i
			print(i)
	time2 = time.time()
	print({'count':c,'sum':s,'time':round(time2-time1)})
print(T(2))