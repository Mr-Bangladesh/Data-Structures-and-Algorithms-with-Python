from queue import Queue

class BFS():
	def __init__(self,g,n):
		self.G=g
		self.D=[-1]*(n+1)
		self.mark = [0]*(n+1)

	def bfs(self,s):
		q = Queue()
		q.put(s)
		self.mark[s]=True
		self.D[s]=0
		while q.empty()==False:
			u = q.get()
			for v in self.G[u]:
				if self.mark[v]==False:
					self.mark[v]=True
					self.D[v] = self.D[u]+1
					q.put(v)

		return self.D


n,m = map(int,input().split())

g=[[] for _ in range(n+1)]

for i in range(m):
	x,y = map(int,input().split())
	g[x].append(y)
	g[y].append(x)

b = BFS(g,n)

dist  = b.bfs(1)

for i in range(1,n+1):
	print(i,dist[i])