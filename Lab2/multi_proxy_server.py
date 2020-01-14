import socket, time, sys
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def getRemoteIP(host):
    # Used to get ip of google.com
    remoteIP = socket.gethostbyname( host )
    return remoteIP

def handleRequest(addr, conn, proxyEnd):

    fullData = conn.recv(BUFFER_SIZE)

    proxyEnd.sendall(fullData)
    proxyEnd.shutdown(socket.SHUT_WR)
    
    data = proxyEnd.recv(BUFFER_SIZE)

    conn.send(data)

def main():
    host = "www.google.com"
    port = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxyStart:
        print("Starting Proxy Server")
        proxyStart.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxyStart.bind((HOST, PORT))
        proxyStart.listen(1)

        while True: 
            conn, addr = proxyStart.accept()
            print("Connected by:",addr)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxyEnd:
                print("Connecting to Google")
                remoteIP = getRemoteIP(host)
        
                proxyEnd.connect((remoteIP, port))
                p = Process(target=handleRequest, args=(addr,conn, proxyEnd))
                p.daemon = True
                p.start()
                print("Started Process")

            conn.close()

if __name__ == "__main__":
    main()