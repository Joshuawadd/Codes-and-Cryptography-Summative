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

first_half = "tile.bil"

# plaintext = four[0] + "." + four[1] + "." + six[0]
# hex_plaintext = plaintext.encode("utf-8").hex()

# print(plaintext)

# print(hex_plaintext)

# ciphertext = subprocess.run(["encrypt.exe" ,hex_plaintext], capture_output=True).stdout

# ciphertext = ciphertext.decode('UTF-8').strip()

# print(ciphertext)

found = False


def encode1(word_length):

    plaintext_string = ""
    global found

    start = time.time()

    counter = 0
    counter_2 = 0

    letter_list = []

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
        perform = 17576
        loop = 9

    for item in itertools.product(letters, repeat=letter):
        letter_list.append(''.join(item))

    # print(letter_list)

    for j, item in enumerate(word_list):

        for num in letter_list:
            plaintext_string = plaintext_string + item + "." + num

        if word_length == "four":
            n = 16000
            four_list = [plaintext_string[i:i+n]
                         for i in range(0, len(plaintext_string), n)]

            # print(four_list)

        for l in range(0, loop):
            if word_length == "four":
                if l == (loop-1):
                    counter = counter + 1576
                    do_encoding = True
                else:
                    counter += 2000
                    do_encoding = True
                plaintext = four_list[l]
            else:
                plaintext = plaintext_string
                counter += counter_num
                if counter % perform == 0:
                    do_encoding = True
                else:
                    do_encoding = False

            # print(counter)

            if do_encoding or j == len(word_list)-1:
                # print(plaintext)

                #print("yay", l)

                hex_plaintext = plaintext.encode("utf-8").hex()

                # print(hex_plaintext)
                ciphertext = subprocess.run(
                    ["encrypt.exe", hex_plaintext], capture_output=True).stdout
                ciphertext = ciphertext.decode('UTF-8').strip()

                # print(plaintext)

                n = 16
                m = 8
                cipher_text_list = [ciphertext[i:i+n]
                                    for i in range(0, len(ciphertext), n)]
                plain_text_list = [plaintext[i:i+m]
                                   for i in range(0, len(plaintext), m)]

                # print(plain_text_list)

                # print(ciphertext)

                for i, cipher in enumerate(cipher_text_list):
                    counter_2 += 1
                    #print(cipher, test_ciphertext1, cipher_text_list[0])
                    if cipher == test_ciphertext1:
                        found = True
                        f = open("cracked.txt", "w")
                        f.write(plain_text_list[i] + "\n")
                        f.close()
                        print("First half is :" + plain_text_list[i])
                        duration = time.time() - start
                        return True, plain_text_list[i]

                duration = time.time() - start
                if counter % (perform*10) == 0:
                    print("%.2f" % (duration/60), counter,
                          counter_2, counter/duration)
                    print(plain_text_list[-1])
                    # print(cipher_text_list[0])

                plaintext_string = ""

    if not found:
        return False, None


def encode2(word_length1, word_length2, first_half):
    plaintext = ""
    global found
    global overall_count

    start = time.time()

    counter = 0
    counter_2 = 0

    letter_list = []

    do_encoding = False

    if word_length1 == "six":
        word_list1 = six
        letter = 1
        counter_num = 26
        perform = 1950
        loop = 1

    if word_length1 == "five":
        word_list1 = five
        letter = 2
        counter_num = 676
        perform = 1352
        loop = 1

    if word_length1 == "four":
        word_list1 = four
        letter = 3
        counter_num = 17576
        perform = 17576
        loop = 9

    if word_length2 == "six":
        word_list2 = six
        letter = 3
        counter_num = 26
        perform = 1950
        loop = 1

    if word_length2 == "five":
        word_list2 = five
        letter = 2
        counter_num = 676
        perform = 1352
        loop = 1

    if word_length2 == "four":
        word_list2 = four
        letter = 1
        counter_num = 17576
        perform = 17576
        loop = 9

    first_letters = first_half.split(".")[1]

    # print(letter_list)

    for j, item in enumerate(word_list1):

        for word in word_list2:
            if word[:3] == first_letters:
                plaintext = plaintext + word[-letter:] + "." + item
                counter+=1
                counter_2+=1

        # if word_length == "four":
        #     if l == (loop-1):
        #         counter = counter + 1576
        #         do_encoding = True
        #     else:
        #         counter += 2000
        #         do_encoding = True
        #     plaintext = four_list[l]
        # else:
        #     plaintext = plaintext_string
        #     counter += counter_num
        #     if counter % perform == 0:
        #         do_encoding = True
        #     else:
        #         do_encoding = False

        # print(counter)
        perform = counter_2

        if counter_2>2000 or j == len(word_list1)-1:
            #print(plaintext)
            counter_2 = 0

            #print("yay", l)

            hex_plaintext = plaintext.encode("utf-8").hex()

            # print(hex_plaintext)
            ciphertext = subprocess.run(
                ["encrypt.exe", hex_plaintext], capture_output=True).stdout
            ciphertext = ciphertext.decode('UTF-8').strip()

            # print(plaintext)

            n = 16
            m = 8
            cipher_text_list = [ciphertext[i:i+n]
                                for i in range(0, len(ciphertext), n)]
            plain_text_list = [plaintext[i:i+m]
                                for i in range(0, len(plaintext), m)]

            #print(plain_text_list)

            # print(ciphertext)

            for i, cipher in enumerate(cipher_text_list):
                #print(cipher, test_ciphertext1, cipher_text_list[0])
                if cipher == test_ciphertext2:
                    found = True
                    f = open("cracked.txt", "w")
                    f.write(first_half + plain_text_list[i] + "\n")
                    f.close()
                    print("Decoded word is:" , first_half + plain_text_list[i])
                    duration = time.time() - start
                    print(counter, duration)
                    duration = time.time() - start
                    overall_count += counter
                    return True, plain_text_list[i]

            duration = time.time() - start
            if counter % (perform*10) == 0:
                print("%.2f" % (duration/60), counter, counter_2, counter/duration)
                print(plain_text_list[-1])
                # print(cipher_text_list[0])

            plaintext = ""

    if not found:
        overall_count += counter
        return False, None


# six_test, first_half = encode1("six")
# if not six_test:
#     five_test, first_half = encode1("five")
#     if not five_test:
#         four_test, first_half = encode1("four")

start2 = time.time()
overall_count = 0
six_test2, second_half = encode2("six", "four", first_half)
if not six_test2:
    five_test2, second_half = encode2("five", "five", first_half)
    if not five_test2:
        four_test2, second_half = encode2("four", "six", first_half)

print(time.time() - start2, overall_count)

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
