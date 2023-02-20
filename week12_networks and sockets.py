import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org' , 80) )
cmd ='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'. encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())











'''import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )'''
#Python build-in support for TCP sockets













'''telnet www.dr-chuck.com 80 #(to be written)
Trying 74.208.28.177...
Connected to www.dr-chuck.com.Escape character is '^]'.
GET http://www.dr-chuck.com/page1.htm HTTP/1.0 #(to be written)

HTTP/1.1 200 OK
Date: Thu, 08 Jan 2015 01:57:52 GMT
Last-Modified: Sun, 19 Jan 2014 14:25:43 GMT
Connection: close
Content-Type: text/html

<h1>The First Page</h1>
<p>If you like, you can switch to 
the <a href="http://www.dr-chuck.com/page2.htm">Second Page</a>.</p>
Connection closed by foreign host.'''
#RUNNING TELNET COMMANDS ON THE TERMINAL