# Reading the input from the user
num = input("Enter a number that is greater than 99:")

# Making sure the input is a number greater than 99
valid = False
while not valid:
    if num.isnumeric():
        if int(num) > 99:
            valid = True
        else:
            num = input("Please enter a number greater than 99:")
    else:
        num = input("Please enter a number not a word nor a character:")

# Printing the third digit from the number
print("The third digit for the given number {0} is: {1}".format(num, num[-3]))
