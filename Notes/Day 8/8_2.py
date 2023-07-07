#Prime number checker
number = int(input("Enter a number: "))
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime == True:
        print("It is a prime Number")
    else:
        print("It is not a prime Number")

prime_checker(number)
