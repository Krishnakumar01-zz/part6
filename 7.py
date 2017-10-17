import os
def directtree(direct,width=0):
	'''returns the tree structure of the directory'''
        a=os.listdir(direct)
        a.sort()
        for i in a:
        	p=os.path.join(direct,i)
                if os.path.isfile(p):
                	if a[-1]!=i:
                        	print(('|\t'*width)+'|--'+i)
                        else:
                                print(('|\t'*width)+'`--'+i)
                else:
                	print(('|\t'*width)+'|--'+i)
                        directtree(p,width+1)
  
  
import sys
directtree(sys.argv[1])

