#To find the number of even numbers available in a given list of numbers

L=[10,7,8,0,3,43,12,76,98,100]
C=0
for x in L:
	if x%2==0:
		C=C+1
print 'Number of even numbers =',C 

