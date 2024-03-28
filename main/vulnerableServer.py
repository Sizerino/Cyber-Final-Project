import socket

sock = socket.socket()

host = "0.0.0.0"
port = 15151
sock.bind((host, port))
sock.listen(2)

client_socket, client_address = sock.accept()

while True:
    message = client_socket.recv(1024)
    client_socket.send(message)
    print(message)
    
    if message == "exit":
        break

client_socket.close()
sock.close()