               ####project: Typing test######
##Probem statement###
# Develop a command line application in Python that serves as a typing test. The program should present a predefined
# passage of text to the user and accurately measure their typing speed and accuracy.

# Key Requirements
# -Text passage: The program must use a static, multi-line passage of text that is challenging but not overly
# long.this passage should be clearly displayed to the user at the start of the test.
# -User input and timing: The program will start a timer as soon as the user begins typing.It will capture the 
# user's input character by the character and compare it aainst the provided text. The timer will stop when the user
# has completed typing the entire passage.
# -performance Metrics: Upon the completion, the application must calculate and display two key performance metrics:
# -Typing speed: Measure in words per minute(WPM) calculated by divinding the total number of correctly
# typed words by the time taken in minutes. A word i defined as five characters(including spaces)
# -Accuracy: Displayed as a percentage claculated by determining the ratio  of correctly typed characters to the 
# total number of characters in the original text.

# The application should be built usin gonly standard Python libraries. The user interface will be entirely text-based
# within the command line

import time

texts = {"1": "The quick brown fox jumps over the lazy dog.",
         "2": "The quick brown fox jumps over the lazy dog and then quietly walks through the buzzing zoo filled with exotic animals.",
         "3":"Every morning when the sun slowly rises above the quiet city, a young man walks through the peaceful streets with a cup of warm coffee in his hand, thinking about his dreams, his future, and the many things he still wants to learn in life, because he believes that with patience, discipline, and daily practice anyone can improve their skills, build confidence, and slowly move closer to their goals no matter how difficult the journey may sometimes feel."
         }

choose = input("Enter  \n1 for short \n2 for medium \n3 for long :::")
while choose not in texts:
    print('Please enter the number among \n1 for short \n2 for medium \n3 for long')
    choose = input('Enter the number again::')
print(f"Please type the sentence you saw below::\n{texts[choose]}")
orginal = texts[choose]

start = time.time()
typed = input()
end = time.time()
taken_time = (end -start)/ 60


correct = 0
for a ,b in zip(orginal, typed):
    if a == b:
        correct += 1

accuracy = correct/len(orginal) * 100
        
wpm = correct/5/taken_time

print(f"your speed is {wpm} word per minute and you have typed {correct} character with {accuracy}% accuracy")
    