#!/home/slacker/.conda/envs/hacking/bin/python
import socket
import socketserver
import sys
import argparse
import threading
import subprocess

# Global Variables
listen              = False
command             = False
execute             = ''
target              = '0.0.0.0'
upload_destination  = ''
port                = 9999

def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((target, port))
        
        if len(buffer):
            client.send(str(buffer).encode())

        while True:
            recv_len = 1
            response = ''

            while True:
                data = client.recv(4096)
                recv_len = len(data)
                response += data.decode()

                if recv_len < 4096:
                    break

            print(response)
            buffer = input()
            buffer += '\n'
            client.send(buffer.encode())
    except:
        client.close()


class RequestHandlerClass(socketserver.BaseRequestHandler):
    def handle(self):
        request = self.request.recv(4096)

        self.request.send(''.encode())
    
    def run_command(command):
        command = command.rstrip()

        try:
            output = subprocess.check_output(command, stderr=suprocess.STDOUT, shell=True)
        except:
            output = 'Failed to execute command.\r\n'

        return output


def server_loop():
    with socketserver.TCPServer((target, port), RequestHandlerClass) as server:
        server.serve_forever()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='NetCat')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-l', '--listen', metavar='[boolenan]', help='listen on [0.0.0.0]:[port] for incoming connections', type=bool)
    group.add_argument('-t', '--target', metavar='[host]', help='specify terget', type=str)

    parser.add_argument('-p', '--port', metavar='[port]', help='specify target port', type=int, required=True)
    
    parser.add_argument('-c', '--command', metavar='[command]', help='initialize command shell', type=bool)
    parser.add_argument('-u', '--upload', metavar='[destination]', help='Upon recieving a connection upload a file and write to [destination]', type=str)
    parser.add_argument('-e', '--execute',metavar='[file_to_run]', help='execute given file upon recieving a connection', type=str)

    args = parser.parse_args()

    if args.listen != None:
        listen = args.listen
    if args.command != None:
        command = args.command
    if args.upload != None:
        upload_destination = args.upload
    if args.execute != None:
        execute = args.execute
    if args.target != None:
        target = args.target
    if args.port != None:
        port = args.port

    if listen:
        server_loop()
    else:
        buffer = sys.stdin.read()

        client_sender(buffer)
