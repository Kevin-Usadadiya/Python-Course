import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', "$", "%", "^", "&", "*", "(", ")"]

print("Welcome to Password Generator!")

nr_letters = int(
    input("Enter the number of Letters you want in your passcode: \n "))
nr_numbers = int(
    input("Enter the number of Numbers you want in your passcode: \n"))
nr_symbols = int(
    input("Enter the number of Symbols you want in your passcode: \n"))

# Easy Level

password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

# print(password)

# Hard level

passw = ''.join(random.sample(password, len(password)))
print(f'Your password is : ${passw}')

# Here in hard level we have used random.sample
# sample() is an inbuilt function of random module in Python that returns a particular length list of items chosen from the sequence i.e. list, tuple, string or set.

# It has two parameters : 1. sequence
#                         2. length as you want.

# It will displayed in array form so we have used ''.join() method to concatenate items of the array into string.