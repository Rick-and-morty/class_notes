# input 1 = "programming is fun"
# input 2 = "m"
# output = [6, 7]

"""sentence = "programming is fun"
letter = "m"
output = []
current_location = 0
# better options print(sentence.index(letter))
for current_letter in sentence:

    if current_letter == letter:
        output.append(current_location)
    current_location += 1

print(output)"""

# enumerate
sentence = "i decided to learn how to program and it was a good decision"
letter = " "
output = []

# better options print(sentence.index(letter))
for current_location, current_letter in enumerate(sentence):
    if current_letter == letter:
        output.append(current_location)

print(output)
