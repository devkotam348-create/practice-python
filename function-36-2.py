###write a function to count frequecy of each element of the list and store list elements in the dict object as keys and element freqenncy as data values (TSRS)

def freq(s):

   num = {}

   for i in s:
       if i in num:
         num[i] += 1
       else:
          num[i] = 1

   return num


def main():
   
   s = [1,2,3,4,1,4,3,5,6,1]

   print(f"The number and it frequency are as folllow {freq(s)}")

main()