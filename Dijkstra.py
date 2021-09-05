from queue import PriorityQueue
INF = int(1e12)
class DIJKSTRA():
	def __init__(self,G,n):
		self.G=G
		self.dist = [INF]*(n+1)

	def dijkstra(self,s):
		self.dist[s]=0
		pq=PriorityQueue()
		pq.put((0,s))

		while pq.empty() == False:
			cost,u = pq.get()
			for v,w in self.G[u]:
				if self.dist[u] + w < self.dist[v]:
					self.dist[v] = self.dist[u] + w
					pq.put((self.dist[v],v))
		return self.dist


n,m = map(int,input().split())

g=[[] for _ in range(n+1)]

for i in range(m):
	x,y,w = map(int,input().split())
	g[x].append((y,w))
	g[y].append((x,w))


d = DIJKSTRA(g,n)

ans = d.dijkstra(1)

print(ans)
