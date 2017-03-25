import sys, time
for i in range(10):
	print '......', # here dots are added to the console as buffer but we cant see, once the program exits the buffer will be cleaned and OS will show.
	sys.stdout.flush()
	time.sleep(2)
