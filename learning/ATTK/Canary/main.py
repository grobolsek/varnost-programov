from pwn import *

p = process('./main')
p = gdb.debug('./main', gdbscript='''
    b *main
''')

p.sendline(cyclic(100))

p.interactive()
