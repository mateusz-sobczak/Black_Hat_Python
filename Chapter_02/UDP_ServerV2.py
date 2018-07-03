#!/home/slacker/.conda/envs/hacking/bin/python
import socketserver

# This is our client-hendeling thread
class RequestHandlerClass(socketserver.BaseRequestHandler):
    def handle(self):
        # Print Cennection request 
        print('[*] Accepted connection from: {}:{}'.format(self.client_address[0], self.client_address[1]))

        # Print out what client sends
        request = self.request[0]

        print('[*] Recieved: {}'.format(request.decode()))

        # Send back a packet
        
        socket = self.request[1]
        socket.sendto('ACK!'.encode(), self.client_address)


if __name__ == '__main__':
    bind_ip = '0.0.0.0'
    bind_port = 9999

    # create a socket object
    with socketserver.UDPServer((bind_ip, bind_port),RequestHandlerClass) as server:

        print('[*] Listening On {}:{}'.format(bind_ip, bind_port))

        server.serve_forever()
