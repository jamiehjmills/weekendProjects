#!/usr/bin/env python3

import socket

def connect_vm(hostname, port, user_id, user_pw):
    family, sockaddr = get_vm_socket(hostname, port)
    print(f'family: {family}')
    print(f'sockaddr: {sockaddr}')

    s = socket.socket(family, socket.SOCK_STREAM)

    s.connect(sockaddr)

    s.sendall(user_id.encode())
    s.sendall(user_pw.encode())

    data = s.recv(1024)
    print(f'Received: {data.decode()}')


def get_vm_socket(hostname, port):
    addrinfos = socket.getaddrinfo(
            hostname, port, socket.AF_UNSPEC, socket.SOCK_STREAM
        )

    for (family, socktype, proto, canonname, sockaddr) in addrinfos:

        # we assume family is 2, AF_INET, which is the address family for IPv4 addresses.
        # we aslo assume socktype is 1, SOCK_STREAM, which is the socket type for TCP connections.
        if family == 2 and socktype == 1:
            return family, sockaddr
