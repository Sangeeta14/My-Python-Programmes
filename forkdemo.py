import os,time
'''
print 'Hello'
os.fork()
print 'Hi'
os.fork()
print 'Done'
'''

child=os.fork()
if child == 0:
	print 'child started with PID:',os.getpid()
	for i in range(10):
		print 'CHILD: value=', i
		time.sleep(2)
	os._exit(0)

os.wait()
print 'parent started with PID:',os.getpid()
for j in range(10):
	print 'PARENT:value=', j
	time.sleep(2)
os._exit(0)
