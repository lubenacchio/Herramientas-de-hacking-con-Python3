
import socket as s
import threading


def connScan(tgtHost, tgtPort):

    sock = None
    try:
        sock = s.socket(s.AF_INET, s.SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print('-$- %d/TCP abierto!' % tgtPort)
    except s.error:
        print('-$- %d/TCP cerrado!' % tgtPort)
    finally:
        if sock is not None:
            sock.close()


# Scanner de puertos
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = s.gethostbyname(tgtHost)
    except s.gaierror:
        print('Host %d Desconocido' % tgtHost)
        return None
    try:
        tgtName = s.gethostbyaddr(tgtIP)
        print('-$- Resultado de scanner para: ' + tgtName[0])
    except s.gaierror:
        print('-$- Resultado de sccaner para: ' + tgtIP)
    s.setdefaulttimeout(10)
    for port in tgtPorts:
        t = threading.Thread(target=connScan, args=(tgtHost, int(port)))
        t.start()


# Metodo Main
def main():
    from sys import argv
    import logging
    if len(argv) < 3:
        logging.error(
            "-$- Uso del programa: %s <Target Host> <Target Port> ", argv[0].split('/')[-1])
        exit(2)
    portScan(argv[1], argv[2:])


if __name__ == '__main__':
    main()
