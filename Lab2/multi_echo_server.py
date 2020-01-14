import socket, time
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)

        while True:
            conn, addr = s.accept()

            p = Process(target=handleEcho, args=(addr,conn))
            p.daemon = True
            p.start()
            print("Starting Process",p)

def handleEcho(addr, conn):
    print("Connected by",addr)

    fullData = conn.recv(BUFFER_SIZE)
    conn.sendall(fullData)
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()


if __name__ == "__main__":
    main()