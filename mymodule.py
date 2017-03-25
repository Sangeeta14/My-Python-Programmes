'''
This module contains the following services
 a)Data: version,L
 b)Function: isprime
 c)Classes:Rectangle,Person,Employee
'''

version=2.3
L=[10,20,30,40,50]

def isprime(m):
	'''isprime function takes integer as input and returns True or False
	'''
	
	if m<2: return false
	i=2
	while i<m:
		if m%i==0:
			return False
		i=i+1
	return True

class Rectangle:
	'''This class Rectangle calculates the area,compare the rectangle,and find whether a given rectangle is square or not
	'''
	
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
class Person:
	def __init__(self,fname,lname,email):
		self.fname=fname
		self.lname=lname
		self.email=email
	def __str__(self):
		return 'Person({0},{1},{2})'.format(self.fname,self.lname,self.email)
	def fullname(self):
		return self.fname + ' ' + self.lname

	def getemail(Self):
		return self.email

class Employee(Person):
	def __init__(self,fname,lname,email,mobile,salary):
		Person.__init__(self,fname,lname,email)
		self.mobile=mobile
		self.salary=salary
	def __str__(self):
		return 'Employee({0},{1},{2},{3},{4})'.format(self.fname,self.lname,self.email,self.mobile,self.salary)
	def getsalary(self):
		return self.salary