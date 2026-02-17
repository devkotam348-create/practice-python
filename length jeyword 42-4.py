#write a fucntion which take variable length arguments to receive strigns. return the list of max length string or strings if multiple length have same strings.

def multi(*t):
    max_len = 0
    for i in t:
        if len(i) > max_len:
            max_len = len(i)

    stri = []

    for i in t:
        
        if len(i) == max_len:
            stri.append(i)
    return stri


def large_st(*t):
    max_len = max(len(i) for i in t )


r = ("cat", "tiger", "lion", "horse")

print(f"The list of max length's string or strings are as follow {multi(*r)}")

