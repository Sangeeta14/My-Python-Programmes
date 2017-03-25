import socket
import os, sys

def testprime(m):
    if m < 2: return False
    i = 2
    while i < m:
        if m % i == 0:
            return False
        i = i + 1
    return True

def nextprime(m):
    while True:
        m = m + 1
        if testprime(m): return m
        
lookup = { '1':testprime, '2':nextprime }

HOST = ''
PORT = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #AF-Address Family Internet(3 types of address family)
s.bind((HOST, PORT)) #Bind method can take the IP of the machine on which it is running,if you have not given(Host is emoty in this program)Bind is mandatory.
s.listen(5)
os.system("clear")
print "server is up and ready...",
sys.stdout.flush()
while True: #server is going into infinite state
    conn, addr = s.accept() #waiting for client (it returns 2 bits of info, address object and conn of client)
    print "\nconnection established from", addr[0],
    sys.stdout.flush()
    child = os.fork() #create a new process after connection is established.
    if child == 0:
        while True: #as client is uncertain till what time it will be alive
            data = conn.recv(1024)
            if data == '3' : break # here control goes to parent level conn.close()
            li = data.split(':')
            result = lookup[li[0]](int(li[1]))#lookup is returning the function def name and (int(li[1])) is the call of the function
            conn.sendall(str(result))
        conn.close()
        print "\nconnection closed by ", addr[0],
        sys.stdout.flush()
        os._exit(0)# releasing the space and time back to OS and gives a signal to the parent
    conn.close()




