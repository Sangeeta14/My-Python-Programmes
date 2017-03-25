print 'Hello'
L=[10,20,30,40,50]
try:
	#import sangeeta
	x=int(raw_input('Enter first number:'))
	y=int(raw_input('Enter second number:'))
	z=x/y
	print z
	#print L[20]
	print L[4]
	#print L[i]
except ValueError:
	print 'I get value error'
except IndexError:
	print 'I get index error'
except ZeroDivisionError:
	print 'I get zero division error'
except Exception,e:
	print 'I get some other error',e
else: print 'No Exception'
finally: print 'I do always'
print 'Rest of the apps goes here'