#!/usr/bin/python
# -*- encoding: utf-8 -*-
# https://www.dlitz.net/software/pycrypto/api/current/

from Crypto.PublicKey import RSA
from base64 import b64encode
from base64 import b64decode

f = open('keypair.pem', 'r')
keypair = RSA.importKey(f.read())
f.close()

m = "Mensagem em claro"

# cifragem
c = keypair.encrypt(m, 0)
c64 = b64encode(c)
print "-----INICIO MENSAGEM CIFRADA-----"
print c64
print "-----FIM MENSAGEM CIFRADA-----"

# decifragem
c, = b64decode(c64)
m = keypair.decrypt(c)
print m

# assinatura
s, = keypair.sign(m, 0)
s64 = b64encode(str(s))
print "-----INICIO ASSINATURA-----"
print s64
print "-----FIM ASSINATURA-----"