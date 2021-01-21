with open("four_2.txt", "r") as f:
    six_2 = []
    for item in f:
        x = item.splitlines()
        six_2.extend(x)

with open("four.txt", "r") as f:
    six = []
    for item in f:
        x = item.splitlines()
        six.extend(x)

words_length = []

for word in six_2:
    if word not in six:
        words_length.append(word)

with open("four_3.txt", "w") as f:
    for item in words_length:
        f.write(item + "\n")
