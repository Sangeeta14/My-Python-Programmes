print 'Enter first number:'
x=raw_input()
x=int(x)
y=int(raw_input('Enter second number:'))
z=int(raw_input('Enter third number:'))

if x<y:
  if x<z:
   print x,'is Smallest'

  else:
    print z,'is Smallest'

else:
   if y<z:
    print y,'is Smallest'
   else:
     print z,'is Smallest'
