print("Welcome to the Tip Calculator.")

total_bill = input("What was the total bill? $")

percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

people = input("How many people to split the bill?")

each_person_contri = (float(total_bill) + (float(total_bill)*(float(percentage_tip) / 100))) / 7

print("Each person should pay: $",round(each_person_contri,2))