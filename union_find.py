class QuickUnion:

	def __init__(self, n):
		self.id = [x for x in range(0, n)]
		self.sz = [0 for x in range(0, n)]

	def root(self, element):
		while(element != self.id[element]): 
			element = self.id[element]
		return element

	def union(self, left, right):
		i = self.root(left)
		j = self.root(right)
		if(self.sz[i] < self.sz[j]):
			self.id[i] = j
			self.sz[j] += self.sz[i]
		else:
			self.id[j] = i
			self.sz[i] += self.sz[j]

	def connected(self, left, right):
		return self.root(left) == self.root(right)



#Weighted quick union - avoid tall trees
#Path compression - make every node of the subtree point to the root
#No such linear algorithm for this problem!

qu = QuickUnion(100)
qu.union(1,2)
qu.union(1,10)
qu.union(1,29)
qu.union(1,40)



print qu.connected(1,40)