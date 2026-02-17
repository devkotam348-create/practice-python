#write a rcursive fundtion to print first N narural numbers

def natural(n):
   
   if n == 0:
      return 
   
   natural(n-1)
   print (n)
        

n = int(input("Enter the number::"))
natural(n)