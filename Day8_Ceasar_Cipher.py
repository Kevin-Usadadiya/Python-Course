from art import logo
print(logo)

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]

def ceaser(text,shift,direction):
    encoded_text = ''
    decoded_text = ''
    for char in text:
        if char in letters:
            position = letters.index(char)
            new_position = position + shift
            old_position = position - shift
            if direction == "encode":
                encoded_text += letters[new_position]
            elif direction == "decode":
                decoded_text += letters[old_position]
        else:
            if direction == "encode":
                encoded_text += char
            elif direction == "decode":
                decoded_text += char
    if direction == "encode":
        print(f"The Encoded message is {encoded_text}")
    elif direction == "decode":
        print(f"The Decoded message is {decoded_text}")



should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrpyt, type 'decode' to decrpyt: \n")
    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    shift %= 26  # Solution if user enter a shift number greater than 44 because we have total length in letters = 44;
    ceaser(text,shift,direction)

    result = input("\nType 'yes' if you want to go again.Other type 'no'\n")
    if result == 'no':
        should_continue = False
        print("Goodbye")

