import os
print 'Hello'
os.execvp('ls',['ls','-l']) #Any line after this function will not be executed.
print 'Done'