import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "100.00.0.0"  # IPv4 adress of the target
port = 445  # port tarjet


def portScanner(port):
    if sock.connect_ex((host, port)):
        print('Port %d is closed' % (port))
    else:
        print('port %d is closed' % (port))


portScanner(port)
