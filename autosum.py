import pexpect
proc=pexpect.spawn('python sum.py')
fout=open('sumstatus.log','w')
proc.logfile_read=fout
proc.expect('number:')
proc.send('2\n')
proc.expect('number:')
proc.sendline('3')
proc.expect('Sum= \d+')
r=proc.after
print r
proc.close()