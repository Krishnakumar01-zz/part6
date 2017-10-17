def product(a,b):
	'''returns the product of two numbers usng + and -'''
	if b==0:
		return 0
	elif b<0:
		return -(product(a,-b))
	else:
		return a+product(a,b-1)


import sys
print(product(int(sys.argv[1]),int(sys.argv[2])))
