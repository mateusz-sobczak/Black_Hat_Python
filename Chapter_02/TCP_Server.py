#!/home/slacker/.conda/envs/hacking/bin/python
import socket
import threading

# This is our client-hendeling thread
def handle_client(client_socket):
    # Print out what client sends
    request = client_socket.recv(1024)

    print('[*] Recieved: {}'.format(request.decode()))

    # Send back a packet
    client_socket.send('ACK!'.encode())
    client_socket.close()


if __name__ == '__main__':
    bind_ip = '0.0.0.0'
    bind_port = 9999

    # create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((bind_ip, bind_port))

    server.listen(5)

    print('[*] Listening On {}:{}'.format(bind_ip, bind_port))

    while True:
        client, addr = server.accept()

        print('[*] Accepted connection from: {}:{}'.format(addr[0], addr[1]))

        # spin up our client thread to handle incoming data
        client_handler = threading.Thread(target=handle_client,args=(client,))
        client_handler.start()
