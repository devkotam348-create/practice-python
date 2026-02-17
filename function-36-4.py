##write a python function to find largest sorted subsequence in a give list.retrun the largest subsequence as a list(TSRS)

def lar(s):

    lis = []
    
    for i in range(len(s)):
        if s[i] not in lis and s[i] < s[i+1]:
            lis.append(s[i])

    return lis

def main():

    s = [10, 5, 8, 3, 9, 4, 12]
    
    print(f"The largest sorted sebsequence is {lar(s)}")

main()