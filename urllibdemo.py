import urllib2
con=urllib2.urlopen('http://www.google.co.in')
html=con.read()
con.close()
print html