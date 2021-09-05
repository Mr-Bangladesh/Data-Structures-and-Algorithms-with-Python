from queue import Queue

class DFS():
	def __init__(self,g,n):
		self.G=g
		self.topsort=[]
		self.mark = [0]*(n+1)

	def dfs(self,u):
		self.mark[u]=True
		for v in self.G[u]:
			if self.mark[v] == False:
				self.dfs(v)
		self.topsort.append(u)


n,m = map(int,input().split())

g=[[] for _ in range(n+1)]

for i in range(m):
	x,y = map(int,input().split())
	g[x].append(y)
	g[y].append(x)

b = DFS(g,n)

b.dfs(1)
a = b.topsort
a.reverse()
print(a)