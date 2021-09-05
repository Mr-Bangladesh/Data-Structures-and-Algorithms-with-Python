class Trie():
	class node():
		def __init__(self):
			self.cnt=0
			self.endpoint=0
			self.child = [-1]*26

	def __init__(self):
		self.root = self.node()
		self.indx=0
		self.tri=[]
		self.tri.append(self.root)

	def Add(self,str,n):
		now = 0
		for i in range(n):
			id = ord(str[i]) - 97
			if self.tri[now].child[id] == -1:
				self.indx += 1
				self.tri[now].child[id] = self.indx
				next = self.node()
				self.tri.append(next)

			now = self.tri[now].child[id]
			self.tri[now].cnt += 1

		self.tri[now].endpoint += 1

	def Find(self,str,n):
		now = 0
		for i in range(n):
			id = ord(str[i]) - 97
			if self.tri[now].child[id] == -1:
				return False
			now = self.tri[now].child[id]
			if self.tri[now].cnt <= 0:
				return False
		return bool(self.tri[now].endpoint)

	def Delete(self,str,n):
		now = 0
		for i in range(n):
			id = ord(str[i]) -97
			now = self.tri[now].child[id]
			self.tri[now].cnt-=1
		self.tri[now].endpoint-=1

str = input()
t = Trie()
n = len(str)
t.Add(str,n)

print(t.Find("ab",2))
t.Delete("ab",2)
print(t.Find("ab",2))