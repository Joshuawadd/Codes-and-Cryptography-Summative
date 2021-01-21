import sys
import os

testFile = os.path.splitext(sys.argv[1])[0]
encodedFile = testFile + ".lz"
decodedFile = testFile + "-decoded.tex"

with open(encodedFile, 'rb') as fin:
    code = fin.read()

# print(code)
i = 1
list = []
triples = []
for i, a in enumerate(code):
    # print(a)
    if i % 4 == 0:
        b = a
        # i+=1
    else:
        if i % 4 == 1:
            # print(b*256,a)
            a = (b*256)+a
            # print(a)
        list.append(a)
        if i == len(code) - 1:
            triples.append(list)
        elif i % 4 == 3:
            # if
            triples.append(list)
            list = []
            #i = 1

text = ""
hello = "hello"
new_text = ""
for i, item in enumerate(triples):
    d = item[0]
    l = item[1]
    if len(item) == 3:
        m = chr(item[2])
        # print(str.encode(m))
    if l:
        right_string = 0-d+l
        if right_string == 0:
            right_string = None
        left_string = 0-d
        if len(item) == 3:
            new_text = text[left_string:right_string] + m
        else:
            new_text = text[left_string:right_string]
    else:
        new_text = m
    text = text + new_text
    #print(new_text, l,d,m)

# print(text)

fin.close()

with open(decodedFile, 'w', newline='') as fout:
    fout.write(text)

fout.close()
