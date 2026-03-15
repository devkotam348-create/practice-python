def wrapper(f):
    def fun(l):
        # complete the function
        x = sorted([num[-10:] for num in l])
        for num in x:
            print('+91' + ' '+ num[:5] + ' '+ num[5:])
        
        
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


