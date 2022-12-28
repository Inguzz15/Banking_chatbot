from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
from chatbot import get_response,get_response2


class ChatServer(WebSocket):

    def handleMessage(self):

        # echo message back to client
        message = self.data
        #message1=self.data

        response = get_response(message)
        a = get_response2(message)
        self.sendMessage(response)
        self.sendMessage(a)


        #self.sendMessage(a)


    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

import socket 
bindsocket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
bindsocket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
addr = [addr for addr in socket.getaddrinfo(self.TCP_IP, self.TCP_Port,
                                            socket.AF_INET6, socket.IPPROTO_TCP)]

try:
    bindsocket.bind((addr[0][-1]))
except socket.error as e:
    print(e)
bindsocket.listen(5)

server = SimpleWebSocketServer('', 8000, ChatServer)
server.serveforever()
