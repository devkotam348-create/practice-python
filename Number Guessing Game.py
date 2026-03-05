# ## Problem Statement##
# #develop a command-line Python application that allows the user to play a number guessing game against the computer.
# key requirememts:
#     -Random Number Generation: The program should generate a random number within a given range(e.g, 1 to 100). This number will be hidden from the user and 
#     serve as the target.
    
#     -User interaction: The program should prompt the user to guess the number. After each guess, the program should provide hints:
        
#         -'too low' if the gues is smaller thatn the target number.
#         _'too high' if the guess is larger than the target number.

# winning condition: The game ends when thye user correctly guesses the number. The program should display a congratulatory messagte along with the number of 
# 'attempts taken.

# Thye user interface will be entirely text-based within the command line.

import random

secret = random.randint(1,100)
attempts = 0
guess_number = 0

while guess_number != secret:
    try:
        guess_number = int(input('Enter the number you wnat to guess::'))
        attempts += 1
        if guess_number > secret:
            print('too high')
        elif guess_number < secret:
            print('too low')
    except ValueError:
        print("Please enter valid integer number")
        
print(f'congratulation ! in {attempts} attempts you crack the number')
    
