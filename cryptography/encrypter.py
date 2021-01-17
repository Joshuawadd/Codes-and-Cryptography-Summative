from des import DesKey
from os import urandom
import time
from multiprocessing import Pool
import threading

key_found = False

test_plaintext = "0123456789abcdef"
test_ciphertext = "a80f2c74f235484e"

ciphertext = "903408ec4d951acfaeb47ca88390c475"
counter = 0

bytes_plaintext = bytes.fromhex(test_plaintext)

start = time.time()

while not key_found:
    
    key = urandom(8)
    key0 = DesKey(key)

    a = key0.encrypt(bytes_plaintext)

    if a.hex() == test_ciphertext:
        key_found = True
        print ("Brute force took %.2f" % duration)
        print("Completed " + str(counter) + " attempts.")
    
    #print(a.hex(), counter, counter.to_bytes(8, byteorder = 'big'))
    
    counter += 1
    

    duration = time.time() - start

    if counter % 2**16 == 0:
        print(duration, counter)


plaintext = key0.decrypt(bytes.fromhex(ciphertext))

print(plaintext)

f = open("cracked.txt", "w")
f.write(plaintext + "\n")
f.write(key)
f.close()

#print(a.hex())