##define a decoarator to display 'Happy New Year' message at the beginning 
def happy(func):
    def greeting():
        print ('Happy New Year')
        func()
        
    return greeting

@happy
def fun():
    print ('hello')

fun()