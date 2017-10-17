import time
def fib(n):
	'''implements the fibnocci function'''
	cache={}
	cache[0]=0
	cache[1]=1
	if n==0 or n==1:
		return cache[n]
	else:
		if n not in cache:
			cache[n]=fib(n-1)+fib(n-2)
		return cache[n]

def profile(f):
	'''takes a function as arguments works as similiar as function and returns execution time of that function'''
	def g(x):
		first=time.time()
		res=f(x)
		last=time.time()
		tt=last-first
		print "Time taken :"+str(tt)+"sec"
		print "Output:",res	
	return g

ab=profile(fib)
ab(20)
