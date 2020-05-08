# -*-coding:utf-8 -*-

import zmq 
context = zmq.Context()  
socket = context.socket(zmq.PUB)  
socket.bind("tcp://127.0.0.1:5000")  
while True:  
    data = input('input your data:')
    socket.send(data.encode('utf-8'))
