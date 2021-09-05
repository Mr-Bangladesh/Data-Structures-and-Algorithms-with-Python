class Sieve():
	def __init__(self):
		self.MAX = int(10000)
		self.Primes =[]
		self.least =[0]*self.MAX

	def linearsieve(self):
		for i in range(2,self.MAX):
			if self.least[i] == False:
				self.least[i] = i
				self.Primes.append(i)
			for x in self.Primes:
				if x>self.least[i] or i*x>=self.MAX:
					break
				self.least[i*x] = x

		return self.Primes

s = Sieve()

res = s.linearsieve()

print(res)