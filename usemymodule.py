import mymodule
print mymodule.version
R=mymodule.Rectangle(2,3)
a=R.area()
print 'area=', a
#Another way of importing
from mymodule import version,Rectangle
print version
R=Rectangle(3,4)
print R
print mymodule.__doc__
print mymodule.isprime.__doc__
print mymodule.Rectangle.__doc__