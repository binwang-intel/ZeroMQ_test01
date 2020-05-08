#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response

#for request in range(10):
#    print("Sending request %s …" % request)
#    socket.send(b"Hello")#
while True:
    data = input('input your data:')
    if data == 'q':
        sys.exit()
    
    print(data)
    socket.send(data.encode('utf-8'))
    #  Get the reply.
    response = socket.recv()
    print(response)
