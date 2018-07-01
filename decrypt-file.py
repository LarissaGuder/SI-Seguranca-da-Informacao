#!/usr/bin/python
# -*- encoding: utf-8 -*-
# https://www.dlitz.net/software/pycrypto/api/current/

from Crypto.PublicKey import RSA
from base64 import b64encode
from base64 import b64decode
import sys


keyfile = sys.argv[1]
filein = sys.argv[2]
fileout = filein[:-4]

# Carrega chave privada para decifragem
with open(keyfile, 'r') as f:
    key = RSA.importKey(f.read())

# Tamanho do bloco de dados cifrado
cipherblocksize = (key.size() + 1) / 8

fin = open(filein, 'rb')
fout = open(fileout, 'wb')

c = fin.read(cipherblocksize)
while c:
    m = key.decrypt(c)
    fout.write(m)
    c = fin.read(cipherblocksize)

fout.close()
fin.close()
