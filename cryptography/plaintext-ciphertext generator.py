import subprocess
import os
import time

dictionary ={}

pairs = 2**47

start = time.time()

for i in range(0,pairs):
    plaintext = os.urandom(8).hex()

    ciphertext = subprocess.run(["encrypt.exe" ,plaintext], capture_output=True).stdout

    ciphertext = ciphertext.decode('UTF-8').strip()

    dictionary[plaintext] = ciphertext

    duration = time.time() - start

    if i % 100 == 0:
        print(duration, i/duration)

f = open("pairs.txt", "w")
f.write(str(dictionary))
f.close()