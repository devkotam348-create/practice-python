# ###1. write a recurdive function to print first n natural numbers
# def natural_numbers(n):
#    if n > 0:
#        natural_numbers(n-1)
#        print(n, end = " ")

# natural_numbers(5)

# ##2. wirite a recurdive funtion to print fist N natural numbers in reverse order
# def reverse_numbers(n):
#     i = n
#     if n > 0:
#       print(n, end= " ")
#       reverse_numbers(n-1)
    
        

# reverse_numbers(5)

# ##3. Write a recursive fundtion to print first N odd natural numbers
# def odd_numbers(n):
#   if n > 0:
#     odd_numbers(n-1)
#     print(2*n -1)
  
# odd_numbers(5)

# ##4 write a recursive function to print N even natural numbers
# def even_numbers(n):
#   if n > 0:
#     even_numbers(n-1)
#     print(2*n)

        
# even_numbers(5)

##5. write a recursive function to print first N odd natural numbers in reverse order
def odd_numbers(n):
  if n > 0:
    print(2*n -1)
    odd_numbers(n-1)
    

odd_numbers(5)

###6. worite a recursive function to print N even natural numbers in reverse order.
def even_numbers(n):
 if n > 0:
    print(2*n)
    even_numbers(n-1)
   

        
even_numbers(5)

