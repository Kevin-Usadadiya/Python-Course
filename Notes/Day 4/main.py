# Randomisation:-
import random, my_module

random_integer = random.randint(1,10)

print(random_integer)

print(my_module.pi) # Making our own module.

# random_float = random.random() #Returns number from [0.0 to 1.0)
# print(random_float)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your Love Score is {love_score}")

# Lists:-

states_of_india = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttarakhand","Uttar Pradesh","West Bengal"]

print(states_of_india[0])           

print(states_of_india[-1]) # prints last state

states_of_india[2] = "Assssam" #updates list
print(states_of_india[2])

# states_of_india.append("Kevland is joining the States of India")

states_of_india.extend(["Kevland","Angelaland"])

print(states_of_india) # prints whole list

number_of_states = len(states_of_india)

# print(states_of_india[number_of_states]) # List Index Out of Range Error
print(states_of_india[number_of_states - 1]) 


# Nested Lists:-

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes","Tomato","Celery"]

fruits = ["Strawberries","Nectarines", "Apples", "Grapes"]
vegetables = ["Spinach", "Kale","Tomato","Celery"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[0])




# Reference link :- askpython.com

# random vs Pseudorandom-number-generator
# Refernce link :- https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators

#Reference link for Lists: https://docs.python.org/3/tutorial/datastructures.html