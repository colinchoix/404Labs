import socket, time, sys

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def getRemoteIP(host):
    # Used to get ip of google.com
    remoteIP = socket.gethostbyname( host )
    return remoteIP

def main():
    host = "www.google.com"
    port = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxyStart:
        print()
        proxyStart.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxyStart.bind((HOST, PORT))
        proxyStart.listen(1)

        while True: 
            conn, addr = proxyStart.accept()
            print("Connected by:",addr)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxyEnd:
                print("Connecting to Google")
                remoteIP = getRemoteIP(host)
                # connect to google
                proxyEnd.connect((remoteIP, port))
                # receive data from first socket
                fullData = conn.recv(BUFFER_SIZE)
                # send data to second socket
                proxyEnd.sendall(fullData)
                proxyEnd.shutdown(socket.SHUT_WR)
                # receive data from google 
                data = proxyEnd.recv(BUFFER_SIZE)
                # sendresponse to orignal
                conn.send(data)

            conn.close()

if __name__ == "__main__":
    main()