##define decorators to display 'Good Bye ' message at the end 

def greetings(func):
    def pyth():
        print('hi you are welcome')
        func()
        print('Good Bye')
    return pyth

@greetings
def main():
    print('Hello')

main()