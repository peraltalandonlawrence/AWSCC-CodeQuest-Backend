import json
import os

def menu():
    menu = ["\t1 - Add Website, Username and Password",
            "\t2 - View",
            "\t3 - Search",
            "\t4 - Delete",
            "\t5 - Update",
            "\t6 - Close"
            ]
    
    for i in menu:
        print(i)

def inputs(_input):
    global running

    if _input == '1':
        add()
    elif _input == '2':
        view()
    elif _input == '3':
        website = input("Please enter the website: ")
        search(website)
    elif _input == '4':
        existing = False
        while not existing:
            website = input("Please enter the website: ")
            existing = is_existing(website)
        delete(website)
    elif _input == '5':
        existing = False
        while not existing:
            website = input("Please enter the website: ")
            existing = is_existing(website)
        update(website)
    elif _input == '6':
        running = False

def is_existing(website):
    with open('Day15_collection.json', 'r') as f:
        data = json.load(f)
        if website in data:
            return True
        return False
    
def add():
    website = input("Please enter the website: ")
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")

    new_data = {
        website: [{
            'email': email,
            'password': password
        }]
    }
    if not os.path.exists('Day15_collection.json'):
        with open('Day15_collection.json', 'w') as f:
            json.dump({}, f)
                
    with open('Day15_collection.json', 'r') as f:
        data = json.load(f)

    if website in data:
        data[website].append({'email': email, 'password': password})
    else:
        data.update(new_data)

    with open('Day15_collection.json', 'w') as f:
        json.dump(data, f, indent=4)

    os.system('cls')
    print("Successfully Added!")

def view():
    os.system('cls')
    with open('Day15_collection.json', 'r') as f:
        data = json.load(f)
        for key, val in data.items():
            print(f"Website: {key}")
            for i in range(len(val)):
                print(f"    Email: {val[i]['email']}")
                print(f"   Password: {val[i]['password']}\n")

def search(website):
    with open('Day15_collection.json', 'r') as f:
        data = json.load(f)
        for key, val in data.items():
            if key == website:
                print(f"Website: {key}")
                for i in range(len(val)):
                    print(f"    {i+1} Email: {val[i]['email']}")
                    print(f"      Password: {val[i]['password']}\n")
                return True
            
        print("No websites found.")
        return

def delete(website):
    with open('Day15_collection.json', 'r') as f:
        data = json.load(f)
        search(website)

        valid_idx = False
        while not valid_idx:
            num = int(input("Please enter the number to be deleted: "))
            valid_idx = 0 <= num-1 < len(data[website])
    
        data[website].pop(num-1)

        if len(data[website]) == 0:
            data.pop(website)

    with open('Day15_collection.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    print("The data in the chosen number has been deleted.")

def update(website):
    with open('Day15_collection.json', 'r') as f:
        data = json.load(f)
        search(website)

        valid_idx = False
        while not valid_idx:
            num = int(input("Please enter the number to be updated: "))
            valid_idx = 0 <= num-1 < len(data[website])

        to_update = input("'email' or 'password': ").lower()
        new_val = input(f"Enter your new {to_update}: ")
        data[website][num-1][to_update] = new_val

    with open('Day15_collection.json', 'w') as f:
        json.dump(data, f, indent=4)

    print("The data in the chosen number has been updated.")

running = True

while running:
    print("********PASSWORD MANAGER********")
    print()
    menu()
    userinput = input("\nChoose the process you want to execute: ")
    inputs(userinput)