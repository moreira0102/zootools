#!/usr/bin/env python3

import socket
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 9009       # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    for i in range(3):
        s.sendall(b'get /home/xap 12\n\nlucas::toma\nleo::toma\narthur::toma\n\nmoreiralucas')
        data = s.recv(1024)
        import pdb
        pdb.set_trace()
        print('Received', repr(data))
        time.sleep(5)