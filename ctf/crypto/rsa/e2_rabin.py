#!/usr/bin/python
# coding=utf-8
import gmpy2
import libnum
from Crypto.PublicKey import RSA

# ��ȡ��Կ����
with open('pubkey.pem', 'r') as f:
    key = RSA.importKey(f)
    N = key.n
    e = key.e
print N

with open('flag.enc', 'r') as f:
    cipher = f.read()
    cipher = libnum.s2n(cipher)
print cipher

print "please input p"
p = int(raw_input(), 10)
print 'please input q'
q = int(raw_input(), 10)
# ����yp��yq
inv_p = gmpy2.invert(p, q)
inv_q = gmpy2.invert(q, p)

# ����mp��mq
mp = pow(cipher, (p + 1) / 4, p)
mq = pow(cipher, (q + 1) / 4, q)

# ����a,b,c,d
a = (inv_p * p * mq + inv_q * q * mp) % N
b = N - int(a)
c = (inv_p * p * mq - inv_q * q * mp) % N
d = N - int(c)

for i in (a, b, c, d):
  print libnum.n2s(i), "---"