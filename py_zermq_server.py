# -*- coding=utf-8 -*-
import zmq

context = zmq.Context()
socket = context.socket(zmq.)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    print("Received: %s" % message)
    socket.send("I am OK!")