# -*-coding:utf-8 -*-

import time
import zmq  
context = zmq.Context()  
socket = context.socket(zmq.SUB)  
socket.connect("tcp://127.0.0.1:5556")  

socket.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8')) 
while True:  
    print(socket.recv()) 