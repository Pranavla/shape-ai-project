


import hashlib

print(hashlib.md5(b'Pranav'))



import binascii

name = hashlib.pbkdf2_hmac('md5', b'Pranav', b'acd', 1000)
binascii.hexlify(name)
print(name)