class EulerTotient():
	def __init__(self):
		self.MAX = int(21)
		self.phi = [0]*self.MAX

	def computetotient(self):
		self.phi[1]=1
		for i in range(2,self.MAX):
			if self.phi[i]==0:
				self.phi[i]=i-1
				j = i*2
				while j<self.MAX:
					if self.phi[j]==0:
						self.phi[j]=j
					self.phi[j]=(self.phi[j]//i)*(i-1)
					j+=i
		return self.phi

t = EulerTotient()

ans = t.computetotient()

print(ans)