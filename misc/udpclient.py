import socket

ADDRESS = ('116.85.23.24', 5749)
BUFSIZE = 1024
def main():
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        msg = raw_input(">> ").strip()
        msg=str(msg)
        client.sendto(msg.encode('utf-8'),ADDRESS)
        data,server_addr = client.recvfrom(BUFSIZE)
        print('client.recvfrom: ',data,server_addr)
main()
