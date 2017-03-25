r=int(raw_input('Enter number of rows'))
c=int(raw_input('Enter number of coloumns'))
print 'Enter Elements'
M=[]
i=0
while i<r:
	j=0
	L=[]
	while j<c:
		x=int(raw_input())
		L.append(x)
		j=j+1
	M.append(L)
	i=i+1
print 'The given matrix is'
for row in M:
		for x in row:
			print x,'',
		print