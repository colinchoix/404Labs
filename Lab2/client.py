import socket, sys

def createTCPsocket():
    # Question 1 how to specify TCP socket SOCK_STREAM
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return s

def getRemoteIP(host):
    remoteIP = socket.gethostbyname( host )
    return remoteIP

def sendData(serversocket, payload):
    # must send as a string of bytes either by encoding or wrap in b tag
    serversocket.sendall(payload.encode())

def main():
    host = "www.google.com"
    port = 80
    payload = "GET / HTTP/1.0\r\nHost: "+host+"\r\n\r\n"
    bufferSize = 4096

    s = createTCPsocket()
    remoteIP = getRemoteIP(host)

    s.connect((remoteIP, port))
    print ("Connecting to",host,"on port",port,"with remote ip",remoteIP,"\n\nResponse:" )

    sendData(s, payload)
    s.shutdown(socket.SHUT_WR)

    
    fullData = b""
    while True:
        data = s.recv(bufferSize)
        if not data:
            break
        fullData += data

    #print out first 100 of response
    print(fullData[:100],"...\n")


if __name__ == "__main__":
    main()