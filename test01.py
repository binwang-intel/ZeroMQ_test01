# -*-coding:utf-8 -*-

import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:5555")

while(True):
    data = input("input your data:")
    if data == 'q':
        sys.exit()

    print(data)
    socket.send(data.encode('utf-8'))

    response = socket.recv()
    print (response)    