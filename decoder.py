import sys
import os

testFile        = os.path.splitext(sys.argv[1])[0]
encodedFile     = testFile + ".lz"
decodedFile     = testFile + "-decoded.tex"

with open(encodedFile, 'rb') as fin:
    code = fin.read()

#print(code)
i=1
list = []
triples = []
for a in code:
    #print(a)
    if i==1:
        b=a
        i+=1
    else:
        if i==2:
            #print(b*256,a)
            a = (b*256)+a
            #print(a)
        list.append(a)
        if i == 4:
            triples.append(list)
            list = []
            i = 1
        else:
            i+=1

text = ""
hello = "hello"
new_text = ""
print(hello[-1:-1])
for item in triples:
    d = item[0]
    l = item[1]
    m = item[2]
    if l:
        right_string = 0-d+l
        if right_string == 0:
            right_string = None
        left_string = 0-d
        new_text = text[left_string:right_string] + chr(m)
    else:
        new_text = chr(m)
    if len(text) < 100:
        print(text, new_text)
    text = text + new_text

#print(text)

fin.close()

with open(decodedFile, 'w') as fout:
    fout.write(text)

fout.close()