print("Welcome to the popular children's game, FizzBuzz!")
print("\nFizz will be for the number divisible by 3.")
print("Buzz will be for the number divisible by 5.")
print("FizzBuzz will be for the number divisible by both 3 and 5.")

limit = int(input ("\n\nPlease input the limit for the range of numbers to be printed out: "))
print("")

for num in range (1, limit +1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz!")
    elif num % 3 == 0:     
        print("Fizz") 
    elif num % 5 == 0:
        print("Buzz")  
    else:
        print(num)   
    
print("\n\nThank you for using the system!")