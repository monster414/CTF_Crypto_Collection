#!/usr/bin/env python
#coding:utf-8

import gmpy2
from Crypto.Util.number import *
c=0x7a7e031f14f6b6c3292d11a41161d2491ce8bcdc67ef1baa9e
e=0x872a335
#q + q*p^3 =1285367317452089980789441829580397855321901891350429414413655782431779727560841427444135440068248152908241981758331600586
#qp + q *p^2 = 1109691832903289208389283296592510864729403914873734836011311325874120780079555500202475594
a = 1285367317452089980789441829580397855321901891350429414413655782431779727560841427444135440068248152908241981758331600586
b = 1109691832903289208389283296592510864729403914873734836011311325874120780079555500202475594
x = gmpy2.gcd(a,b)
print(a%x)
print(b%x)
print(x)
print(a//x)
print(b//x)
p = b//x
q = b//(p+p**2)
n = p*q
phi = (p-1)*(q-1)
d = gmpy2.invert(e, phi)
m = pow(c,d,n)
print(long_to_bytes(m))
