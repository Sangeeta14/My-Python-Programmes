import re
S='hello how 1234 ok 56789 done'
pat=raw_input('Enter some pattern:')
if re.search(pat,S):
	print 'found'
else:
		print 'not found'