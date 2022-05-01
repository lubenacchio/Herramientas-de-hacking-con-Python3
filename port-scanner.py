import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input(" -$- Ingrese Host a Escanear : ")
port = int(input(" -$- Ingrese Puerto a Escanear : "))


def portScanner(port):
    if sock.connect_ex((host, port)):
        print('Port %d is open' % (port))
    else:
        print('port %d is closed' % (port))


portScanner(port)
