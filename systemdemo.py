import os,time
#os.system('ls -l') 
fin=os.popen('ls -l')
records=fin.readlines()
for record in records:
	print record
	time.sleep(1)