# Author:                        Date:
# Sources:

# Get input from the user 
while True:
    letter = input("Enter a letter: ")
    if letter.isalpha() == False or len(letter) > 1:
        print("Please enter a single letter.")
    else:
        letter = letter.upper()
        break

# Write your code here.
# Create a string of all letters from A to the input letter
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
end_index = letters.index(letter)

# Print the pattern
for i in range(end_index + 1):
    print(letters[:end_index - i + 1]) 