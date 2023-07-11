import replit #⚠️This will only work on replit not any other IDE.
print("Welcome to Secret Auction Program.")
biders = {}

name = input("What is your name?: ")
bid = int(input("Whats your bid? : $ "))
biders[name] = bid;
question = input("Are there any other biders around? Type 'yes' or 'no' ")

if question == 'no':
    replit.clear() #⚠️This will only work on replit not any other IDE.
    print(f"Highest bider is {name} and he bidded {bid}")

while question != 'no':
    replit.clear()
    name = input("What is your name?: ")
    bid = input("Whats your bid? : $ ")
    biders[name] = bid
    question = input("Are there any other biders around? Type 'yes' or 'no' ")
    if question == 'yes':
        continue
    else:
        highest_bider = 0
        is_tie = False
        for name in biders:
            if int(biders[name]) >= int(highest_bider):
              if int(biders[name]) == int(highest_bider):
                   is_tie = True
              else:
                  highest_bider = biders[name]
                  highest_bider_name = name
        if is_tie == True:
          print("There a tie between highest bid")
        else:
          print(f"Highest bider is {highest_bider_name} and he bidded {highest_bider}")

