import boofuzz

host = '192.168.80.129'
port = 9999


def main():
    session = boofuzz.Session(
        target=boofuzz.Target(
            connection=boofuzz.SocketConnection(
                host, port, proto='tcp'
            )
        )
    )

    boofuzz.s_initialize("TRUN")
    boofuzz.s_string("TRUN", fuzzable=False)
    boofuzz.s_delim(" ", fuzzable=False)
    boofuzz.s_string("FUZZ")

    session.connect(boofuzz.s_get("TRUN"))
    session.fuzz()


if __name__ == "__main__":
    main()
