import math
from math import sqrt, ceil, pow
import numpy as np

class SieveOfAtkin:
	def __init__(self, limit):
		self.limit = limit		
		self.primes = []	
		self.sieve = [False]*(self.limit+1)	
	def flip(self, prime):
		try:self.sieve[prime] = not self.sieve[prime]
		except KeyError:pass
	def invalidate(self, prime):
		try:
			if self.sieve[prime]:self.sieve[prime] = False
		except KeyError:pass
	def isPrime(self, prime):
		try:return self.sieve[prime]
		except KeyError:return False
	def getPrimes(self):			
		testingLimit = int(ceil(sqrt(self.limit)))
		for i in range(testingLimit):
			for j in range(testingLimit):
				n = 4*int(pow(i, 2)) + int(pow(j,2))
				if n <= self.limit and (n % 12 == 1 or n % 12 == 5):self.flip(n)
				n = 3*int(pow(i, 2)) + int(pow(j,2))
				if n <= self.limit and n % 12 == 7:self.flip(n)
				n = 3*int(pow(i, 2)) - int(pow(j,2))
				if n <= self.limit and i > j and n % 12 == 11:self.flip(n)
		for i in range(5, testingLimit):			
			if self.isPrime(i):
				k = int(pow(i, 2))
				for j in range(k, self.limit+1, k):self.invalidate(j)							
		self.primes = [1, 2, 3] + [x for x in range(len(self.sieve)) if self.isPrime(x) and x>=5]
		return self.primes

primos_column = SieveOfAtkin(1000).getPrimes()
primos_row = primos_column.copy()

primos_matriz = np.outer(primos_column, primos_row)

print(primos_matriz)




# RSA_1 = 550127
# RSA_2 = 636149
RSA_1 = 137
RSA_2 = 797


RSA = RSA_1 * RSA_2

print("RSA_1:               ", RSA_1)
print("RSA_2:               ", RSA_2)
print("RSA:                 ", RSA)

print("")
print("Raiz inteira:        ", int(math.sqrt(RSA)))
print("RSA % Raiz0:         ",RSA % int(math.sqrt(RSA)))
print("RSA % Raiz1:         ",RSA % int(math.sqrt(RSA)-1))
print("RSA % Raiz2:         ",RSA % int(math.sqrt(RSA)-2))
print("RSA % Raiz3:         ",RSA % int(math.sqrt(RSA)-3))
print("RSA % Raiz4:         ",RSA % int(math.sqrt(RSA)-4))
print("RSA % Raiz5:         ",RSA % int(math.sqrt(RSA)-5))
print("RSA % Raiz6:         ",RSA % int(math.sqrt(RSA)-6))
print("RSA % Raiz7:         ",RSA % int(math.sqrt(RSA)-7))

print("Raiz - (RSA % Raiz):  ",(int(math.sqrt(RSA)) - (RSA % int(math.sqrt(RSA)))))

print("")
print("(RSA_2 - RSA_1)/2:    ", (RSA_2 - RSA_1)/2)
print("RSA_1 - raiz:         ", int(math.sqrt(RSA)) - RSA_1)
print("RSA_2 - raiz:         ", RSA_2 - int(math.sqrt(RSA)))
print("dif das dif:           ",(RSA_2 - math.sqrt(RSA)-(math.sqrt(RSA) - RSA_1)))



