import socket
import sys
import time
socket.setdefaulttimeout(5)
def get_tick_count():
    current_time=time.time()
    return int(round(current_time * 1000))

def prob1(ip, port):
    addr = (ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket() fileno:{0}".format(s.fileno()))
    print("connect() addr:{0} ... ...".format(addr))
    t1 = get_tick_count()
    try:
        s.connect(addr)
        use_tick =get_tick_count() - t1
        print("connect() addr:{0};ok;use_tick:{1}".format(addr, use_tick))
    except socket.error as arg:
        print(arg)
        sys.exit(1)

    while True:
        inp = raw_input("please input:\n>>>")
        print(":::", inp)
        if inp == "q":
            print("END")
            s.sendall(inp)
            sys.exit(1)
        else:
            t1 =get_tick_count()
            bytes_sent = s.sendall(inp)
            print("sendall:", bytes_sent, "data:", inp)
            result = s.recv(1024 * 8)
            use_tick = get_tick_count() - t1
            print("use_tick=%d userecv:%s" % (use_tick, result))

if __name__ == '__main__':
    prob1("127.0.0.1",4777)
