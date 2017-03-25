import MySQLdb as mydb 
con=mydb.connect('localhost','root','root123','test')
cur=con.cursor()
cur.execute('Select Version()')
data=cur.fetchone()
print data
con.close()