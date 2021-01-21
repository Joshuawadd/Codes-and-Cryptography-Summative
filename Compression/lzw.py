import sys
import os
import struct

testFile = os.path.splitext(sys.argv[1])[0]
inputFile = testFile + ".tex"
encodedFile = testFile + ".lz"

# initialise dictionary
dictionary = {chr(i): i for i in range(256)}

with open(inputFile, 'r', newline='') as fin:
    text = fin.read()

i = 0
position = 256

max_dict_size = 2**16

tokens = []
start = time.time()
string = ""

while i < len(text):
    j = i+1
    matching_found = True

    while matching_found:
        look_ahead = text[i:j]
        # check if string is in dictionary
        if look_ahead in dictionary:
            token = dictionary[look_ahead]
            string = look_ahead
            j += 1
            if j > len(text):
                matching_found = False
        else:
            matching_found = False
            if(len(dictionary) < max_dict_size):
                # add string to dictionary if not full
                dictionary[look_ahead] = position
                position += 1

    tokens.append(token)
    # append token to list
    i = i + len(string)

# convert each token in list to bytes and write to file
with open(encodedFile, 'wb') as fout:
    byte = bytearray()
    for item in tokens:
        byte = byte + item.to_bytes(2, 'big')
    fout.write(byte)
