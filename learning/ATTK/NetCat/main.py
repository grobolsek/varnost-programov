from pwn import *

# p = process( ["python3", "server.py"])
p = remote("inst-ukkko3baml.tls.vuln.si", 443, ssl=True)

p.recvline()

for i in range(25):
    line = p.recvuntil( b" = " )

    words = line.split( b" " )

    res = int( words[0] ) + int( words[2] )
    p.sendline( str( res ).encode() )

p.interactive()
