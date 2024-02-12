shop_list = []

action = 0

while True:
    print("""\nOptions: 
    1. Add item to the shopping list
    2. View shopping list
    3. Remove item from the shopping list
    4. Quit""")
    choice = int(input("Enter the number of your choice: "))
    if choice == 1:
        item = input("Enter the item you want to add: ").capitalize()
        shop_list.append(item)
        print(f"{item} has been added to your shoppinglist.")

    elif choice == 2:
        print("Your shoppingl ist: ")
        for viewlist in shop_list:
            print(f"{viewlist}")

    elif choice == 3: 
        remove = (input("Enter the item you want to remove: ")).capitalize()
        shop_list.remove(remove)    
        print(f"{remove} has been removed from your shopping list.")  

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Input error.")