import socket
BUFSIZE = 1024
ADDRESS = ('0.0.0.0',  5749)
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(ADDRESS)
    print("udp socket bind:{0}".format(ADDRESS  ))
    while True:
        data,client_addr = server.recvfrom(BUFSIZE)
        print('server.recvfrom:', data)
        server.sendto(data.upper(),client_addr)
    server.close()
main()
