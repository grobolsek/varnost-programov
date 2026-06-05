from pwn import *

# Use one of the following at a time
p = process('./main') # Local challenge
p = gdb.debug('./main', gdbscript='''
    b *main
''') 

# Exploit goes here



p.interactive()