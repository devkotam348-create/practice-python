##write a python function to filter out words from the text starting from the same alphabet and store them in a list. Now create a dict with the alphabets as key- values
## and list of words starting from that alphabets as data values. take as an argument and return dict object (TSRS)

def words(s):
    dif = []
    diff = {}

    for word in s.split():
        dif.append(word)

    for ch in dif:
        key = ch[0]
        if key in diff:
            diff[key].append(ch)
        else:
            diff[key] = [ch]

    return diff

def main():
    
    s = input("Enter the sentence you want to enter::")
    print (f"The new dict will be {words(s)}")

main()


