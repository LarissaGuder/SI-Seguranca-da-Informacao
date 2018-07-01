#!/usr/bin/python
# -*- encoding: utf-8 -*-
# https://www.dlitz.net/software/pycrypto/api/current/

from Crypto.PublicKey import RSA
from base64 import b64encode
from base64 import b64decode
from Crypto.Random import random
import sys

keyfile = sys.argv[1]
filein = sys.argv[2]
fileout = filein + ".enc"

# Carrega a chave publica para cifragem
with open(keyfile, 'r') as f:
    key = RSA.importKey(f.read())

# Maior numero de bytes que pode ser cifrado pela chave publica
messageblocksize = key.size() / 8

fin = open(filein, 'rb')
fout = open(fileout, 'wb')

m = fin.read(messageblocksize)
while m:
    c, = key.encrypt(m, 0)
    fout.write(c)
    m = fin.read(messageblocksize)

fout.close()
fin.close()
