#!/usr/bin/env python3

import socket

HOST = '127.0.0.1' # Standard loopback interface address (localhost)
PORT = 9999     # Port to listen on 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'hello, Server')
    data = s.recv(1024)
    
print ('Received', repr(data))