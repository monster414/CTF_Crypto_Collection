import random
from Crypto.Cipher import AES
from os import urandom
from string import printable
from binascii import hexlify
from secret import flag

random.seed(urandom(32))

key1 = '0'*13 + ''.join([random.choice(printable) for _ in range(3)])
key2 = ''.join([random.choice(printable) for _ in range(3)]) + '0'*13

cipher1 = AES.new(key=key1.encode(), mode=AES.MODE_ECB)
cipher2 = AES.new(key=key2.encode(), mode=AES.MODE_ECB)

pt = input("You have a chance to get something: ")
pt = pt.encode()

val = len(pt) % 16
if not val == 0:
    pt += b'\x00'*(16 - val)

c1 = cipher1.encrypt(pt)
c2 = cipher2.encrypt(c1)
print('Your cipher:{}'.format(hexlify(c2)))

assert(len(flag) % 16 == 0)
c3 = cipher1.encrypt(flag)
c4 = cipher2.encrypt(c3)
print('Your flag:{}'.format(hexlify(c4)))