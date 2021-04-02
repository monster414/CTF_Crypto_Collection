#!/usr/bin/env python3
#coding:utf-8

f = open("key", "rb")
bytes = f.read(4)
f.close()
key = ""
for i in bytes:
	if len(bin(i)[2:]) != 8:
		key += (8 - len(bin(i)[2:])) * "0" + bin(i)[2:]
	else:
		key += bin(i)[2:]
print(key)
for i in range(32):
	res = key[-1]
	key = key[:31]
	awns = chr(int(res) ^ int(key[-30]) ^ int(key[-27]) ^ int(key[-20]) ^ int(key[-12]) ^ int(key[-8]) ^ int(key[-5]) ^ int(key[-3]) + 48)
	key = awns + key
print("flag{" + hex(int(key,2)) + "}")
