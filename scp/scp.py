#!/usr/bin/env python3

import socket

class SCPClient():

        def __init__(self, hostname, port, user_id, user_pw, file_location):
             self.socket = None
             self.hostname = hostname
             self.port = port
             self.user_id = user_id
             self.user_pw = user_pw
             self.file_location = None

        def connect_vm(self):

             family, sockaddr = self.get_vm_socket()
             print(f'family: {family}')
             print(f'sockaddr: {sockaddr}')

             self.socket = socket.socket(family, socket.SOCK_STREAM)
             self.socket.connect(sockaddr)
             self.socket.sendall(self.user_id.encode())
             self.socket.sendall(self.user_pw.encode())

             data = self.socket.recv(1024)
             print(f'Received: {data.decode()}')

        def get_vm_socket(self):
              addrinfos = socket.getaddrinfo(self.hostname, self.port, socket.AF_UNSPEC, socket.SOCK_STREAM)

              for (family, socktype, proto, canonname, sockaddr) in addrinfos:
                    # we assume family is 2, AF_INET, which is the address family for IPv4 addresses.
                    # we aslo assume socktype is 1, SOCK_STREAM, which is the socket type for TCP connections.
                    if family == 2 and socktype == 1:
                     return family, sockaddr

        def send_file(self):
             if not self.socket:
                  raise Exception("You must connect to the VM before sending a file.")

             with open(self.file_location, 'rb') as file:
                  while True:
                       chunk = file.read(104)
                       if not chunk:
                            break
                       self.socket.sendall(chunk)

             print('File sent successfully.')



# TODO: need to look at example in paramiko how they send a file to a remote server








