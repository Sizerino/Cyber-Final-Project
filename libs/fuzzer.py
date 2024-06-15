import socket
from print_color import print
import datetime


def fuzz():
    buffersize = 0
    while buffersize <= 65536:
        buffersize += 10

        datetimeformat = "".join([
            "[",
            datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "]"
        ])

        print(
            datetimeformat,
            "Transmiting {} bytes".format(buffersize),
            color="blue"
        )

# fuzz()
