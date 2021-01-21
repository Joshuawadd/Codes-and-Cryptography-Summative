import sys
import os
import struct

testFile = os.path.splitext(sys.argv[1])[0]
encodedFile = testFile + ".lz"
decodedFile = testFile + "-decoded.tex"

tokens = []
count = 0

# open file and read each set of 2 bytes as an int and add to list
with open(encodedFile, 'rb') as fin:
    byte = fin.read(2)
    while byte != b'':
        count += 1
        tokens.append(int.from_bytes(byte, "big"))
        byte = fin.read(2)

dictionary = {i: chr(i) for i in range(256)}
text = ""
last_token = None
position = 256

# create string by adding the characters the the tokens correspond to in the dictionary.
# build the dictionary up dynamically as it reads each token
for i, token in enumerate(tokens):
    text = text + dictionary[token]
    if i != len(tokens)-1:
        dictionary[position] = dictionary[token]
        dictionary[position] = dictionary[position] + \
            dictionary[tokens[i+1]][0]
        position += 1

# write string out to file
with open(decodedFile, 'w', newline='') as fout:
    fout.write(text)
