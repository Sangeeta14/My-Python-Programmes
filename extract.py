import re
s='hello how 1234 ok 56789 done'
pat=raw_input('enter some pattern:')
result=re.findall(pat,s)
print result
