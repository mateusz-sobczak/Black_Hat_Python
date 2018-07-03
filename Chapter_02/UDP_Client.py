#!/home/slacker/.conda/envs/hacking/bin/python
import socket

if __name__ == '__main__':
    target_host = '127.0.0.1'
    target_port = 80

    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # send some data
    client.sendto('GET / HTTP/1.1\r\nHost: google.com\r\n\r\n'.encode(), (target_host, target_port))

    # recieve some data
    response = client.recvfrom(4096)

    print(response[0].decode())
