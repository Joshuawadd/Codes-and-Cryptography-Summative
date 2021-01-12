import sys

w = 2**16
l = 2**8

# read the .tex file, and modify the lines
with open('test.tex') as f:
    text = f.read()



encode = ""

i=0
while i < len(text):
    #print("hey",text[i])
    if i == 0:
        code = [0,0,text[i]]
        print(code)
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

        code = [a,len(long_look_ahead), next_char]
        i+=len(long_look_ahead)
        i+=1
        print(code)

        size = 0
        for item in code:
            size += sys.getsizeof(str(item))


    

#print(text)

f.close()

# # write back the new document
# with open('test.tex', 'w') as fout:
#     for i in range(len(texdoc)):
#         fout.write(texdoc[i])