##A file contains N lines, each line consist of a name and age seperated by comma. wirte a function to read this file and store data in a dict objcect with 
## name as keys and age as value. Assuming the names are unique.

def read_file(filename):
    store = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n')
            name, age = line.split(',')
            store[name] = int(age)
            
    return store


print(read_file('name.txt'))
                
        