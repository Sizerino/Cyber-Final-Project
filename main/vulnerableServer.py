import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "0.0.0.0"
port = 19191
sock.bind((host, port))
sock.listen(2)

print("Listening on: {}:{}".format(host, port))

client_sock, client_addr = sock.accept()

print("Connection established from:", client_addr)

while True:
    message = client_sock.recv(1024)
    client_sock.send(message)
    print(message)
    
    if message == "exit":
        break

client_sock.close()
sock.close()
