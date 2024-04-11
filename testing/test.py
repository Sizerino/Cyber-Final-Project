import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((127.0.0.1,19191))

buffer = "A"*2000
sock.send(buffer)

sock.close()