import socket

MSGLEN = 4096

class MySocket:
    ' demo class for webserver sockets '

    def __init__(self, sock = None):
        if sock is None:
            self.sock = socket.socket(
                    socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        MSGLEN = len(msg)
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent


