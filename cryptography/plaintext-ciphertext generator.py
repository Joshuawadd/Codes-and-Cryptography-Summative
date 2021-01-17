import subprocess
import os

dictionary ={}

for i in range(0,100):
    plaintext = os.urandom(8).hex()

    ciphertext = subprocess.run(["encrypt.exe" ,plaintext], capture_output=True).stdout

    ciphertext = ciphertext.decode('UTF-8').strip()

    dictionary[plaintext] = ciphertext

f = open("pairs.txt", "w")
f.write(str(dictionary))
f.close()