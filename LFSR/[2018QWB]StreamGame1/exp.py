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
key = key[:19]
print(key)
flag = ""
for i in range(19):
	res = key[-1]
	key = key[:18]
	awns = chr(int(res) ^ int(key[-3]) ^ int(key[-4]) ^ int(key[-5]) ^ int(key[-9]) ^ int(key[-13]) ^ int(key[-14]) ^ int(key[-17]) + 48)
	key = awns + key
print("flag{" + key + "}")
