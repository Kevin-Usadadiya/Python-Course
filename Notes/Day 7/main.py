import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["mouse", "aligator", "apple"];
chosen_word = random.choice(word_list);

display = []
for i in chosen_word:
    display.append(' _ ')

print("\n\n\n\n-------The Hangman Project--------\n")
print(display)
print("")

lives = 6
lost = 0
str = " "

while display != list(chosen_word):
        guess = input("Guess a Letter :  ").lower()
        print(" ")
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
                lost+=1
                print(stages[lives])
                print(f'Lost {lost} Life')
                lives-=1
        if(lives == 0):
                print("You lose SORRY!!")
                break;

        if(display == list(chosen_word)):
            print("You Won!!!")
            print("\n\n\n\n\n")
        print("Your word --> " + str.join(display))
        print(" ")


