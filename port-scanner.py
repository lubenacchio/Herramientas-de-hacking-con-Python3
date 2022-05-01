import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.1.88"  # IPv4 adress of the target
port = 443  # port tarjet


def portScanner(port):
    if sock.connect_ex((host, port)):
        print('Port %d is closed' % (port))
    else:
        print('port %d is closed' % (port))


portScanner(port)
