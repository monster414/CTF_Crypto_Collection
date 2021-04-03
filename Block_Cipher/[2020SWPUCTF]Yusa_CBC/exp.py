#!/usr/bin/env python
#coding:utf-8

from pwn import *
import binascii
import time

p = remote('das.wetolink.com',42888)
p.recvline()
p.recvline()
p.recvline()
p.recvline()
p.sendline('1')
p.recv()
p.sendline('Admin')
data0 = p.recvline().decode()
data0 = data0[28:124]
iv0 = data0[:32]
cipher00 = data0[32:64]
cipher01 = data0[64:96]
replacement0 = str(hex(int(cipher00[:2],16)^ord('A')^ord('a')))[2:]
payload0 = iv0+replacement0+cipher00[2:]+cipher01
print('data0: ',data0)
print('payload0: ',payload0)
p.recvline()
p.recvline()
p.recvline()
p.recvline()
p.sendline('2')
p.recv()
p.sendline(payload0)
data1 = p.recvline()[:64+len('Admin')*2]
data1 = data1.decode()
plain1 = data1[32:64]
print('data1: ',data1)
print('plain1: ',plain1)
iv1 = str(hex(int(binascii.hexlify('yusa'.encode()).decode()*4,16)^int(plain1,16)^int(iv0,16)))[2:]
print('iv1: ',iv1)
payload1 = iv1+replacement0+cipher00[2:]+cipher01
print('payload1: ',payload1)
p.recvline()
p.recvline()
p.recvline()
p.recvline()
p.sendline('2')
p.recv()
p.sendline(payload1)
p.recvline()
p.recvline()
print(p.recvline())
