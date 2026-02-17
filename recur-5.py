#write a recursiv fucntion to print mysirg N times on the screen

def my(n):

    if n == 0:
        return 
        
    my(n-1)
    print("mysirg")

r = int(input("Enter how many times you want to print my sirg::"))
my(r)
    
