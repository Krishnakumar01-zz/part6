def treemap(a,List):
	'''implements map function for a neseted list and returns the list'''
	for i in range(len(List)):
		if isinstance(List[i],list):
			treemap(a,List[i])
		else:
			List[i]=f(List[i])
	return List


f=lambda x:x*x
List=[1,2,[3,4,[5]]]
print(treemap(f,List))
