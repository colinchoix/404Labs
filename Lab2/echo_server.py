import socket, time

# Empty = localhost
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Question 3 how we instruct OD to let us reuse the same bind port
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(2)

        while True:
            # Question 4 What information we get about the incoming connections. IP and PORT plus the connection used to send and receive data
            conn, addr = s.accept()
            # addr is IP and PORT
            print("connected by:" ,addr)
            # Question 5 recv returns bytes object representing the data received from the socket
            fullData = conn.recv(BUFFER_SIZE)
            print("Data Received: ",fullData)
            time.sleep(0.5)
            conn.sendall(fullData)
            conn.close()



if __name__ == "__main__":
    main()