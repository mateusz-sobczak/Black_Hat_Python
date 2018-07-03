#!/home/slacker/.conda/envs/hacking/bin/python
import socket
import threading

# This is our client-hendeling thread
def handle_client(server_socket, client_socket, data):
    print('[*] Accepted connection from: {}:{}'.format(client_socket[0], client_socket[1]))

    # Print out what client sends
    print('[*] Recieved: {}'.format(data.decode()))

    # Send back a packet
    server.sendto('ACK!'.encode(),client)


if __name__ == '__main__':
    bind_ip = '0.0.0.0'
    bind_port = 9999

    # create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server.bind((bind_ip, bind_port))

    print('[*] Listening On {}:{}'.format(bind_ip, bind_port))

    while True:
        # Accept Connection
        data, client = server.recvfrom(1024)

        # Create Thread
        client_handler = threading.Thread(target=handle_client,args=(server, client, data,))
        client_handler.start()
