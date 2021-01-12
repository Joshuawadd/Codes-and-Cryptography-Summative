with open('test.lz', 'rb') as fin:
    code = fin.read()

print(code)
i=1
list = []
triples = []
for a in code:
    list.append(a)
    if i == 3:
        triples.append(list)
        list = []
        i = 1
    else:
        i+=1
        
print(triples)