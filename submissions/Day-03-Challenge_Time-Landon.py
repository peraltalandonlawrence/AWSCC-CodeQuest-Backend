name = input("Please enter your name: ")
print(f"\n\n\t\tHello, {name}! Welcome to your Summer Adventure!")
print("Embark on a thrilling summer adventure game where each choice leads to self-improvement \n\t\tand  joy of endless possibilities under the sun.")

choice = input("\n\nWould you like to start your one of a kind Summer Advenure? (Yes or No): ")

if (choice == "Yes" or choice == "yes"):
    print("\n\n\t\t\tGreat! Lets us start! \n\n")

    task = input("Would you like to play or study this summer? (Play or Study): ")
    if (task == "Play" or task == "play"):
        game = input("What game would you like to play? ")
        print(f"\n\nA month has passed since you've been playing {game} daily.")

        con10 = input(f"\n\nWould you still like to play {game} for another month? (Yes or No):")
        if (con10 == "Yes" or con10 == "yes"):
            print(f"\n\nCongratulations! You have become a master in playing {game}. Keep it up!")

        else:
            print(f"\n\nA month has passed and you did not become a master of playing {game}. Make sure to do better next year.")

    else:
        subject = input("What subject would you like to study? ")
        print(f"\n\nA month has passed since you've been studying {subject} daily.")

        con10 = input(f"\n\nWould you still like to study {subject} for another month? (Yes or No): ")
        if (con10 == "Yes" or con10 == "yes"):
            print(f"\n\nCongratulations! You have become a genius in the subject {subject}. Keep it up!")

        else:
            print(f"\n\nA month has passed and you did not become a genius in the subject {subject}. Make sure to do better next year.")


else:
    print("\n\n\t\tAwww... See you next time!")