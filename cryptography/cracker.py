import subprocess
import os
import time
import string
import itertools

letters = string.ascii_lowercase

with open("four.txt", "r") as f:
    four = []
    for item in f:
        x = item.splitlines()
        four.extend(x)

with open("five.txt", "r") as f:
    five = []
    for item in f:
        x = item.splitlines()
        five.extend(x)

with open("six.txt", "r") as f:
    six = []
    for item in f:
        x = item.splitlines()
        six.extend(x)

test_ciphertext1 = "903408ec4d951acf"
test_ciphertext2 = "aeb47ca88390c475"

# plaintext = four[0] + "." + four[1] + "." + six[0]
# hex_plaintext = plaintext.encode("utf-8").hex()

# print(plaintext)

# print(hex_plaintext)

# ciphertext = subprocess.run(["encrypt.exe" ,hex_plaintext], capture_output=True).stdout

# ciphertext = ciphertext.decode('UTF-8').strip()

# print(ciphertext)

plaintext_string = ""

found = False









def encode1(word_length):

    global plaintext_string
    global found
    global counter

    start = time.time()

    counter = 0

    letter_list =[]

    do_encoding = False

    if word_length == "six":
        word_list = six
        letter = 1
        counter_num = 26
        perform = 1950
        loop = 1
    
    if word_length == "five":
        word_list = five
        letter = 2
        counter_num = 676
        perform = 1352
        loop = 1
    
    if word_length == "four":
        word_list = four
        letter = 3
        counter_num = 17576
        perform = 2000
        loop = 9

    for item in itertools.product(letters, repeat=letter):
        letter_list.append(''.join(item))

    for j, item in enumerate(word_list):
        
        for num in letter_list:
            plaintext_string = plaintext_string + item + "." + num


        

        if word_length == "four":
            n = 8
            four_list = [plaintext_string[i:i+n] for i in range(0, len(plaintext_string), n)]

        for l in range(0,loop):
            if word_length == "four":
                if l == (loop-1):
                    counter = counter + 1576
                    do_encoding = True
                else:
                    counter += counter_num
                    if counter % perform == 0:
                        do_encoding = True
                    else:
                        do_encoding = False
                plaintext = four_list[l]
            else:
                plaintext = plaintext_string
                counter += counter_num
                if counter % perform == 0:
                    do_encoding = True
                else:
                    do_encoding = False

            if do_encoding or j==len(word_list)-1:
                #print(plaintext)

                hex_plaintext = plaintext.encode("utf-8").hex()

                # print(hex_plaintext)
                ciphertext = subprocess.run(
                    ["encrypt.exe", hex_plaintext], capture_output=True).stdout
                ciphertext = ciphertext.decode('UTF-8').strip()

                n = 8
                cipher_text_list = [ciphertext[i:i+n]
                                    for i in range(0, len(ciphertext), n)]
                plain_text_list = [plaintext[i:i+n]
                                for i in range(0, len(plaintext), n)]

                # print(ciphertext)

                for i, cipher in enumerate(cipher_text_list):
                    if ciphertext == test_ciphertext1:
                        found = True
                        f = open("cracked.txt", "w")
                        f.write(plain_text_list[i] + "\n")
                        f.close()
                        print(plain_text_list[i])
                        return True

                duration = time.time() - start
                if counter % (perform*10) == 0:
                    print(duration, counter, counter/duration)
                    print(plain_text_list[0])

                plaintext_string = ""
    
    if not found:
        return False


six_test = encode1("six")
if not six_test:
    five_test = encode1("five")
    if not five_test:
        four_test = encode1("four")

if not found:
    print("not found")


# four_file = open("four.txt", "r", newline='')
# five_file = open("five.txt", "r", newline='')
# six_file = open("six.txt", "r", newline='')

# four = four_file.readlines()
# five = five_file.readlines()
# six = six_file.readlines()

# print(four)
# print(five)
# print(six)
