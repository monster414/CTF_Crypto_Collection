#!/usr/bin/env python
#coding:utf-8

import binascii
import string
import subprocess
import os
from Crypto.Cipher import AES

plain = b"UNCTF2020_Enjoy_Crypto~"
plain += (16 - len(plain) % 16) * b"\x00"
cipher = b'01a4e429e76db218fa0eb18f03ec69c9200a2362d8b4d7ea46170ce698389bbd'
cipher = binascii.unhexlify(cipher)
flag_enc = b'196cc94c2d685beb54beeaa14c1dc0a6f3794d65fca0d1a1274515166e4255ab367383092e42d774992f74bc138faaad'
flag_enc = binascii.unhexlify(flag_enc)
dic = string.printable
p_to_c1_keys = []
p_to_c1_cipher = []
c2_to_c1_keys = []
c2_to_c1_cipher = []
key = b""


f1 = open("c1", "w")
for i in dic:
	for j in dic:
		for k in dic:
			key1 = "0" * 13 + i + j + k
			cipher1 = AES.new(key=key1.encode(), mode=AES.MODE_ECB)
			c1 = cipher1.encrypt(plain)
			p_to_c1_keys.append(i+j+k)
			p_to_c1_cipher.append(binascii.hexlify(c1))
			f1.write(binascii.hexlify(c1).decode()+"\n")
f1.close()

f2 = open("c2", "w")
for i in dic:
	for j in dic:
		for k in dic:
			key2 = i + j + k + "0" * 13
			cipher2 = AES.new(key=key2.encode(), mode=AES.MODE_ECB)
			c2 = cipher2.decrypt(cipher)
			c2_to_c1_keys.append(i+j+k)
			c2_to_c1_cipher.append(binascii.hexlify(c2))
			f2.write(binascii.hexlify(c2).decode()+"\n")
f2.close()


process = subprocess.Popen("grep -wf c1 c2", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
result_f = process.stdout
c1 = result_f.read().strip()
key1 = p_to_c1_keys[p_to_c1_cipher.index(c1)]
key2 = c2_to_c1_keys[c2_to_c1_cipher.index(c1)]
key3 = "0" * 13 + key1
key4 = key2 + "0" * 13
cipher3 = AES.new(key=key3.encode(), mode=AES.MODE_ECB)
cipher4 = AES.new(key=key4.encode(), mode=AES.MODE_ECB)
c3 = cipher4.decrypt(flag_enc)
flag = cipher3.decrypt(c3)
print(flag)
