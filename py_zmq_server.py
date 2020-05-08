import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("hello, I'm ready!")

while True:
    message = socket.recv()
    print("Received: %s" % message)

    time.sleep(1)

    socket.send(b"I am OK!")