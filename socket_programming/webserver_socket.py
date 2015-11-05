'script to show webserver socket'

import socket

#create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to public host and a well known port
server_host_port = ('', 3558)
serversocket.bind(server_host_port)

#become a server socket
serversocket.listen(5)

while True:
    MSGLEN = 100
    bytes_recd = 0
    chunks = []
    '''
    while  bytes_recd < MSGLEN:
        chunck = clientsocket.recv(min(MSGLEN - bytes_recd, 2048))
        chunks.append(chunck)
        bytes_recd += len(chunck)
    '''
    client_sockets = []
    while True:
        #accept connections from outside
        (clientsocket, address) = serversocket.accept()

        bytes_recd = clientsocket.recv(1024)
        print(bytes_recd)

        #print(dir(clientsocket))
        clientsocket.close()

        
    print("msg --> ", ''.join(map(lambda x: x.decode(), chunks)))
    #print('(clientsocket, address) -->', (clientsocket, address))


