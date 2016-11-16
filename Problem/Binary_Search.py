from math import floor

class Binary_Search(object):
	
	# Recursive version
	def search_recur(self,A,p,r,n):
		if r >= p:
			q = int(floor((p+r)/2))
			if A[q] == n:
				return q
			elif A[q] > n:
				return self.search_recur(A,p,q-1,n)
			else:
				return self.search_recur(A,q+1,r,n)
		else:
			return -1
	
	# Iterative version
	def search_iter(self,A,p,r,n):
		while p <= r:
			q = int(floor((p+r)/2))
			if A[q] == n:
				return q
			elif A[q] > n:
				r = q-1
			else:
				p = q+1
		return -1
				

n = int(raw_input().strip())
A = [int(i) for i in raw_input().strip().split()]
p,r = 0,len(A)-1
x = Binary_Search()
recur_index = x.search_recur(A,p,r,n)
iter_index = x.search_iter(A,p,r,n)

if recur_index == iter_index:
	if recur_index != -1:
		print "The number is located at the index ",recur_index
	else:
		print "Number not found in the given list"
