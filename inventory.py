inventory = {
    "sword": 1,
    "shield": 1,
    "potion": 1,
}


def buy(element):
    res = inventory.get(element)
    if res == 1:
        print("Item bought")
        inventory[element] = 0
        print(inventory)
    else:
        print("Item not available")


def restock(element):
    if element not in inventory:
        print("Invalid item")
        return
    print("Item restocked")
    inventory[element] = 1
    print(inventory)


again = True
while again:
    option = input("buy or restock\noption: ").strip().lower()
    if option == "buy":
        element = input("sword, shield, potion\nwhat do you want: ").strip().lower()
        buy(element)
    elif option == "restock":
        element = input("sword, shield, potion\noption: ").strip().lower()
        restock(element)
    else:
        print("Invalid input. Please enter buy or restock")

    again = input("Do you want to continue? (y/n): ").strip().lower() == "y"