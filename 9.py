def permute(List):
	'''returns all possible permutations of elements in the given list'''
	pl=[]
	if len(List)==0:
		return []
	elif len(List)==1:
		return [List]
	else:
		for i in List:
			remList=[a for a in List if a!=i]
			newList=permute(remList)
			for j in newList:
				pl.append([i]+j)
	return pl

print(permute([1,2,3]))
