import sys
import os

testFile        = os.path.splitext(sys.argv[1])[0]
inputFile       = testFile + ".tex"
encodedFile     = testFile + ".lz"

w = 2**16 -1
l = 2**8 -1

# read the .tex file, and modify the lines
with open(inputFile,'r',newline='') as fin:
    text = fin.read()


test = 0
encode = []

q=1

i=0
end = False
while i < len(text):
    #print("hey",text[i])
    if i == 0:
        code = [0,0, ord(text[i])]
        #print(code)
        encode.extend(code)
        i+=1
    else:
        window_end = i
        if i >= w:
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
            a = len(window) -d
            #print("hey",a,i,d,len(window))
        else:
            next_char_index = i
            a=0

        if next_char_index != len(text):
            next_char = text[next_char_index]
            #print(next_char, str.encode(next_char))
            next_char = str.encode(next_char)
            code = [a,len(long_look_ahead), ord(next_char)]
        else:
            code = [a,len(long_look_ahead)]

        encode.extend(code)
        i+=len(long_look_ahead)
        i+=1

        if a > test:
            test = a

        #print(code)
        q+=1

        #for item in code:
         #   print(bytearray(item))
        
        #print(bytes(code))



    

#print(text)


#print(q*4)

#byte_encode = bytearray(encode)
#print(encode)
#output = bytearray(encode)
#print(output)
#print(output.decode())

# write back the new document
with open(encodedFile, 'wb') as fout:
    i=2
    byte = bytearray()
    for item in encode:
        if i==2:
            byte = byte + item.to_bytes(2,'big')
            i=0
        else:
            byte = byte + item.to_bytes(1,'big')
            i+=1

    fout.write(byte)
