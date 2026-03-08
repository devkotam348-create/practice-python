##Project: Smart Calculator
# Develop a Smart Calculator in Python that leverages Natural Languages Processing(NLP) techiniques to interpret and execute mathematical operation
# based on user input provided in simpl;e text written in general english.

# Projects Description:
# The goal of this project is to create an intelligent calculator that understands user commands in natural language and performs the corresponging mathematical operations.
# The smarts calculator should be capable of interpreting a varietyu of expressions and provide accurate results.

# Key Features:
#     - Supproted Operations:
#         -Support a range of mathematical operations, including addition, subtraction, multiplication, division, exponentiation, square root, lcm, hcf, factorial etc.
#     - Expression Evaluation:
#         - Evaluate complex mathematical expressions provided in natural language and return the result.
#     - User-Friendly interaction:
#         - Design an intuitive user interface that accepts text input and displays the calculated results.
#     - Error Handling:
#         - Implement robust error handling to address invalid inputs or ambiguous expressions.
        
# Example User inputs:
#     - calculate the sum of 5 and 8
#     - subtract 10 form 25
#     - what is the result of 3 multiplied by 7 
#     - square root of 144

import math
def add(numbers):
   return numbers[0] + numbers[1]
    

def subtract(numbers):
    return numbers[0] - numbers[1]
    

def multiplication(numbers):
    return numbers[0] * numbers[1]
    

def division(numbers):
    return numbers[0] / numbers[1]
    
def exponentiation(numbers):
    return numbers[0]**2
   
def square_root(numbers):
    return math.sqrt(numbers[0])

def gcd(numbers):
    return math.gcd(numbers[0],numbers[1])

def lcm(numbers):
    return math.lcm(numbers[0], numbers[1])

def factorial(numbers):
    return math.factorial(numbers[0])



def extract_number(text):
    numbers = []
    result = text.split()
    for words in result:
        if words.isdigit():
            numbers.append(int (words))
    return numbers

def sorry():
    print("The instruction you provided is beyond my limit")
            
def end():
    print('Thank you for using claculator')
    input("press any key to exit")
    exit()
operations0 ={'close': end, 'end':end, 'exit':end, 'quit':end, 'finish':end }
operations1 ={'root':square_root, 'factorial':factorial, 'square':exponentiation}
operations2 ={'add':add, 'sum':add, 'plus':add, 'addition':add, 
             'difference':subtract, 'minus':subtract, 'subtraction':subtract, 'subtract':subtract,
             'multiply':multiplication, 'multiplication':multiplication, 'product':multiplication,
             'divide':division,'division':division, 'hcf':gcd, 'gcd':gcd, 'lcm':lcm }

def main():
    print('--welcome to smart calculator--')
    print('--If you want to exit the calculator prese type exit or close or end or quit or finish---')
    while True:
        print()
        text = input('Enter the operation you want to perform::::').lower()
        for words in text.split():
            if words in operations2.keys():
                try:
                    num = extract_number(text)
                    result = operations2[words](num)
                    print(f'The result is {result}')
                    break
                except Exception as e:
                    print("something is wrong here",e)
            elif words in operations1.keys():
                try:
                    num = extract_number(text)
                    result = operations1[words](num)
                    print(f'The result is {result}')
                    break
                except Exception as e:
                    print('There is something wrong here',e)
                    
            
            elif words in operations0.keys():
                operations0[words]()
                
        else:
            sorry()
                
                    
if __name__== '__main__':
    main()
                    
        
        
        
    