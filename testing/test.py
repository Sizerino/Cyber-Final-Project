import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 9999

sock.connect((host, port))

testBuffer = b"A"*25000
sock.send((b'TRUN .' + testBuffer + b'\r\n'))
port = 19191

sock.connect((host, port))

testBuffer = "A"*2000
sock.send(testBuffer)

# sock.close()
