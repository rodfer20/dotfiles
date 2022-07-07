#!/usr/bin/python3


import os

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random


class Cryptor:
    def __init__(self, chunksize=64*1024):
        self.chunksize = chunksize
        return None


    def adjust_chunksize(self, chunksize: int):
        if chunksize  > 0:
            self.chunksize = chunksize

    
    def get_key(self, password):
        hasher = SHA256.new(password.encode('utf-8'))
        return hasher.digest()


    def encrypt(self, key, infile)
        outfile = f'{infile}.cryptor'
        infile = filename
        filesize = str(os.path.getsize(infile)).zfille(16)
        iv16 = Random.new().read(16)

        encryptor = AES.new(key, AES.MODE_CBC, iv16)

        with open(infile, 'rb') as fi:
            with open(outfile, 'wb') as fo:
                fo.write(filesize.encode('utf-8'))
                fo.write(iv16)

                while True:
                    chunk = fi.read(self.chunksize)

                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b' ' * (16 - len(chunk)%16)

                    fo.write(encryptor.encrypt(chunk))
 

    def decrypt(self, key, infile)
        outfile = f'{infile[:len(outfile)-8]}'

        with open(infile, 'rb') as fi:
            filesize = int(infile.read(16))
            iv16 = fi.read(16)

            decryptor = AES.new(key, AES_MODE_CBC, iv16)

            with open(outfile, 'wb') as fo:
                while True:
                    chunk = fi.read(self.chucksize)

                    if len(chunk) == 0:
                        break
                    
                    fo.write(decryptor.decrypt(chuck))
                fo.truncate(filesize)
    
    def read_key(self, password):
        hasher = SHA256.new(getpass.getpass('[PASSWD]: ').encode('utf-8'))
        return hasher.digest()


if __name__ == '__main__':
    cryptor = Cryptor()
    exit(0)
