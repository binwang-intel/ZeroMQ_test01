# -*-coding:utf-8 -*-

import zmq 
context = zmq.Context()  

# Subscriber tells us when it's ready here
rec = context.socket(zmq.REP)  
rec.bind("tcp://127.0.0.1:5555")  

# We send updates via this socket
pub = context.socket(zmq.PUB)  
pub.bind("tcp://127.0.0.1:5556")  

# Wait for synchronization request
#sync_request = sync.rece()

# Now broadcast exactly 10 updates with pause
print("Ready go")
while True:  
    message = rec.recv()
    print(message)
    rec.send("server response!".encode('utf-8'))

    print(message.decode('utf-8'))
    pub.send(message)
