#!/usr/bin/env python
#coding:utf-8

import gmpy2
from Crypto.Util.number import *

p = 782758164865345954251810941
q = 810971978554706690040814093
r = 1108609086364627583447802163
e = 59159
phi = (p - 1)*(q - 1)*(r - 1)
d = gmpy2.invert(e, phi)
c = 449590107303744450592771521828486744432324538211104865947743276969382998354463377
n = 703739435902178622788120837062252491867056043804038443493374414926110815100242619
m = pow(c, d, n)
print(long_to_bytes(m))
