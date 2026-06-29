from pwn import cyclic_find, process, gdb, cyclic

p = process('./main')
p = gdb.debug('./main', gdbscript='''
    b *main
''')

p.sendline(cyclic(100))

p.interactive()
