import re 
s='hello how 1234 ok 56789 done'
pat=raw_input('Enter some pattern:')
S1=re.sub(pat,'ABC',s)
print S1
