def flatten_dict(a,result=None):
	'''returns a flattened dict by joining the keys with "."'''
	if result is None:
		result={}
	for i in a:
		if isinstance(a[i],dict):
			b={}
			for k in a[i]:
				p=a[i][k]
				b[i+'.'+k]=p
			flatten_dict(b,result)
		else:
			result[i]=a[i]
		
	return result

print(flatten_dict({'a':1,'b':{'x':2,'y':3},'c':{'w':3,'r':4}}))
			
