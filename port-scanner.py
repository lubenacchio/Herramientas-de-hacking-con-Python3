import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input(" -$- Ingrese Host a Escanear : ")


def portScanner(puerto):
    if sock.connect_ex((host, puerto)):
        print(' -$- El Puerto %d Esta Cerrado' % (puerto))
    else:
        print(' -$- Puerto %d Esta Abierto' % (puerto))


for puerto in range(1, 10):
    portScanner(puerto)
