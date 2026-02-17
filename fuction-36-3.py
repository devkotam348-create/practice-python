##write a python function to find numbers in a given text, store numbers in a list and return list.(TSRS)

def num(s):

    li = []

    for i in s:
        if  i.isdigit():
            li.append(int(i))

    return li


def main():
    
    s = "mahe3ndr456"

    print(f"the number in the text are {num(s)}")


main()
