#for the program to work, use the relative path of the text file
with open('submissions\\Day11_names.txt', 'r') as file:
    names = file.readlines()

names.sort()

#check the text file because it will be arranged already. leave a new line after the last listed name
with open('submissions\\Day11_names.txt', 'w') as file:
    file.writelines(names)
    print("The names have been arranged in an alphabetical order.")