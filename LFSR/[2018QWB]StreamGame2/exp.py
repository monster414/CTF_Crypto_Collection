#!/usr/bin/env python3
#coding:utf-8

f = open("key", "rb")
bytes = f.read(3)
f.close()
key = ""
for i in bytes:
	if len(bin(i)[2:]) != 8:
		key += (8 - len(bin(i)[2:])) * "0" + bin(i)[2:]
	else:
		key += bin(i)[2:]
key = key[:21]
for i in range(21):
	res = key[-1]
	key = key[:20]
	awns = chr(int(res) ^ int(key[-2]) + 48)
	key = awns + key
print("flag{" + key + "}")
