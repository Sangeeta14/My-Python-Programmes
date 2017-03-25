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

P= Person('Sangeeta','Patnaik','abc@gmail.com')
print P
fn=P.fullname()
print 'my name is', fn
emp=Employee('Sangeeta','Patnaik','abc@gmail.com','98765432','890000')
print emp
fn=emp.fullname()
print fn
fn=emp.getsalary()
print fn
