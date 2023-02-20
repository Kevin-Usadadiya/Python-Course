
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random
your_input = (int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")))
if(your_input == 0):
   print(rock)
elif(your_input == 1):
  print(paper)
else:
  print(scissors)
  
print("Computer chose: \n")
computer_input = random.randint(0,2)
print(computer_input)
if(computer_input == 0):
    print(rock)
    if(your_input == 0):
        print("Its a Tie")
    elif(your_input == 1):
        print("You won")
    else:
        print("You lose")
    

elif(computer_input == 1):
    print(paper)
    if(your_input == 1):
        print("Its a tie")
    elif(your_input == 2):
        print("You Won")
    else:
        print("You Lose")
    
else:
    print(scissors)
    if(your_input == 2):
        print("Its a tie")
    elif(your_input == 0):
        print("you Won")
    else:
        print("You lose")
    


    
  