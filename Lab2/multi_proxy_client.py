import socket, time
from multiprocessing import Pool

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

def connect(addr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(addr)
    print("connected")
    s.sendall(payload.encode())
    print("Wait a bit before shutting down")
    time.sleep(8)
    s.shutdown(socket.SHUT_WR)
    
    fullData = s.recv(BUFFER_SIZE)
    #print(fullData)
    
   
def main():
    address = [('127.0.0.1', 8001)]
    with Pool() as p:
        p.map(connect, address * 10 )

if __name__ == "__main__":
    main()