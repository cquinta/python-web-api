import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP
server.bind(('localhost', 9000))
server.listen()
try:
    while True:
        client, addr = server.accept()
        # client is a new socket object usable to send and receive data on the connection(request)
        data = client.recv(5000).decode()
        print(f"{data}")

        #Response
        client.sendall(
            "HTTP/1.1 200 OK\r\n\r\n<html><body>Hello</body></html>\r\n\r\n".encode()
            )
        client.shutdown(socket.SHUT_WR)
            
except Exception:
    server.close()
