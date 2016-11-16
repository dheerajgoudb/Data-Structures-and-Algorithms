class Bubble_Sort(object):
	def Sort(self,A):
		for i in xrange(0,len(A)-1):
			for i in xrange(len(A)-1,0,-1):
				if A[i] < A[i-1]:
					A[i], A[i-1] = A[i-1], A[i]
		return A
		
A = [int(i) for i in raw_input().strip().split()]		
x = Bubble_Sort()
print x.Sort(A)
