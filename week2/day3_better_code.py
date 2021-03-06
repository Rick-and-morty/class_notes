# inventory tracker RPG


def add_item_to_inventory(player):
    item_name = input('what is the item name? ')
    item_quantity = int(input("how many? "))
    if item_name in player["inventory"].keys():
        player["inventory"][item_name]["quantity"] += item_quantity
    else:
        player["inventory"][item_name] = {"quantity": item_quantity}


def inspect_inventory(player):
    for item in player["inventory"].keys():
        quantity = player["inventory"][item]["quantity"]
        print("{} - {}".format(item, quantity))


def player_input(player, choice):
    if choice == "a":
        add_item_to_inventory(player)
    elif choice == 'i':
        inspect_inventory(player)


def make_character():
    player = {"inventory": {"red potion": {'quantity': 20}}}
    player_name = input("welcome traveler! what is your name? ")
    player["name"] = player_name
    return player

###########################################

player = make_character()

while True:
    choice = input("would you like to (i)nspect your inventory, or (a)dd to your inventory?\n>")
    player_input(player, choice)
