#!/usr/bin/env python
#coding:utf-8

from pwn import *
import binascii
import time

plain = "flag{********************************}"
flag = "}"
BLOCKSIZE = 16
char = '0123456789abcdef'
p = remote('das.wetolink.com',42887)
text = p.recv()
for pad1 in range(12, 46):
	#print('61'*pad1)
	p.sendline('61'*pad1)
	text = p.recvline()
	print(len(text))
	if len(text) <= 147:
		res = text.decode()[-33:-1]
	elif len(text) <= 179:
		res = text.decode()[-33-32:-1-32]
	else:
		res = text.decode()[-33-64:-1-64]
	#print(res)
	pad2 = (26-pad1)%16
	#print(pad1)
	for j in char:
		time.sleep(0.1)
		payload = str(hex(ord(j)))[2:]+binascii.hexlify(flag.encode()).decode()+('0'+str(hex(pad2)[2:]))*pad2
		#print(payload)
		p.sendline(payload)
		text = p.recvline().decode()
		#print(text)
		if res == text[18:18+32]:
			flag = j + flag
			print(flag)
			break
flag = "flag{" + flag
print(flag)
