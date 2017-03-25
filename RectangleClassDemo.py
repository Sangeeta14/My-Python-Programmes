class Rectangle:
	def __init__(self,x,y):
		self.length=x
		self.width=y
	def area(self):
		return self.length*self.width
	def __str__(self):
		return 'Rectangle({0},{1})'.format(self.length,self.width)
	def __add__(self,other):
		return Rectangle(self.length+other.length,self.width+other.width)
	def __eq__(self,other):
		return self.length==other.length and self.width==other.width
	def IsSquare(self):
		return self.length == self.width

#Find Area
R= Rectangle(2,3)
a=R.area()
print 'area=',a
print 'value of R is =',R
#Sum of two Rectangle
R1=Rectangle(2,3)
R2=Rectangle(2,4)
R3=R1+R2
print 'Sum of two rectangle R1 and R2 is =',R3
#Check if two rectangle is same nor not
if R1==R2:
	print 'same'
else:
	print 'not same'

#Check if a rectangle is Square
R4=Rectangle(4,4)
if R4.IsSquare():
	print 'is square'
else:
	print 'not square'


