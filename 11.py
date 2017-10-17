def square(x):
	return x*x

def vectorize(f):
	'''takes a function f as argument and erturn a new function,which takes a list a list as arguments and calls f for every element in the list'''  
	def g(List):
		for i in range(len(List)):
			List[i]=f(List[i])
		return List
	return g

f=vectorize(square)
print(f([1,2,3,4]))
g=vectorize(len)
print(g(["Hello","world"]))
print(g([[1,2],[2,3,4]]))
