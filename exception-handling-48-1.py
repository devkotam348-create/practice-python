### Define python function to calculate factorial of a number.Handlle all possible expection 

def factorial(num):
    if num < 0:
          raise ValueError("Negative numbers are not allowed")
    
    if num == 1 or num == 0:
        return 1
    
    fact = num * factorial(num-1)
    return fact
    


try:
    num = int(input('Enter the number for the factorial::'))
except ValueError:
    print('Plese enter the correct value(decimal number and alphabets will not accepted)')
else:
    try:
        result = factorial(num)
        print(f'The factorial of {num} is {result}')
    except ValueError:
        print('Negative numbers are not allowed')
    except RecursionError:
        print('Too large')
        
print('Program continue.....')