import socket

ip = "192.168.1.132"
openPorts = []

for port in range(65535):
    sock = socket.socket()
    sock.settimeout(0.001)
    attempt = sock.connect_ex((ip, port))
    if attempt == 0:
        print("The Server's COULD be using the port:", port)
        openPorts.append(port)

    else:
        print("The Server is NOT using the port:", port)

sock.close()
