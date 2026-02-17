##write a python fucntion to count words in string::

def words(s):

    count = 0
    in_words = False

    for ch in s:
        if ch != " " and not in_words:
            count += 1
            in_words = True

        elif ch == " ":
            in_words = False

    return count

def main():
    s = input("Enter the string::")
    print(f"The number of words in the string is {words(s)}")
            
main()