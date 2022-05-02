import socket


def returnBanner(ip, port):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return


def main():
    ip = input("-$- Ingrese La Ip: ")
    for port in range(1, 100):
        banner = returnBanner(ip, port)
        if banner:
            print("-$- " + ip + "/" + str(port) + " :" + banner.split("/n"))


main()
