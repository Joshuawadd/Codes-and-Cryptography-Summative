import sys

w = 2**16
l = 2**8

# read the .tex file, and modify the lines
with open('test.tex') as fin:
    text = fin.read()



encode = []

i=0
while i < len(text):
    #print("hey",text[i])
    if i == 0:
        code = [0,0, ord(text[i])]
        print(code)
        encode.extend(code)
        i+=1
    else:
        window_end = i
        if i > w:
            window_start = i - w
        else:
            window_start = 0
        window = text[window_start:window_end] 
        j = i+1
        look_ahead = ""
        long_look_ahead = ""
        d = 0
        matching_found = True
        while matching_found:
            look_ahead = text[i:j]
            index = window.rfind(look_ahead)
            #print(window, look_ahead, index)
            if index != -1:
                long_look_ahead = look_ahead
                j+=1
                #print(index)
                d = index
                if j > len(text):
                    #print("hey")
                    matching_found = False

            else:
                matching_found = False
        #print(j)
        #print(d)
        if len(long_look_ahead) != 0:
            next_char_index = i+len(long_look_ahead)
            a = i-d
        else:
            next_char_index = i
            a=0

        if next_char_index == len(text):
            next_char = '-' 
        else:
            next_char = text[next_char_index]

        next_char = str.encode(next_char)

        code = [a,len(long_look_ahead), ord(next_char)]
        encode.extend(code)
        i+=len(long_look_ahead)
        i+=1
        print(code)

        #for item in code:
         #   print(bytearray(item))
        
        #print(bytes(code))



    

#print(text)

fin.close()

#byte_encode = bytearray(encode)
print(encode)
output = bytearray(encode)
print(output)
print(output.decode())

# write back the new document
with open('test.lz', 'wb') as fout:
    fout.write(output)