def tree_reverse(List):
	'''reverses a nested list recursively'''
	for i in range(len(List)):
		if isinstance(List[i],list):
			List[i].reverse()
			tree_reverse(List[i])
		else:
			List[i]=List[i]
	
	return List[::-1]
print(tree_reverse([[1,2],[3,[4,5]],6]))
