if __name__ == '__main__':
    people = [input("enter name::").split() for i in range(int(input("enter how many name::")))]
    print(*name_format(people), sep='\n')



