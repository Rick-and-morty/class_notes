
for _ in range(5):
    print("i am looping")

turns = 0
while turns < 5:
    print("while looping")
    turns = turns + 1

choice = ""
while choice != "n":
    print(choice)
    choice = input("do you want to keep looking? [Y/n] ")
