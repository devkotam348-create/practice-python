##1.write a function to write a given string in a given file

def write_in_file(filename,text):
    with open(filename, "w") as f:
        f.write(text)

##2. write a function to read from a given file and display it on the screen.
def read_data(filename):
    with open(filename,"r") as f:
       text = f.read()
       print(text)

##3. write a function to copy one file data to another file.
def copy_content(orginal_file,copied_file):
    try:
        with open(orginal_file, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print('file does not exist')
    else:
        with open(copied_file, 'w') as f:
            
            f.write(text)
###4. write a function to read and store all the numbers found in a given text file into a list
def store_numbers(filename):
    numbers = []
  
    with open(filename, "r") as f:
        for line in f:
            for word in line.split():
                if word.isdigit():
                    numbers.append(int(word))
        return numbers

print(store_numbers('name.txt'))


        
       
        
        
# filename = input("Enter the file name::")
# text = input("Enter the text")
# write_in_file(filename,text)
# read_data('name.txt')
# copy_content('name.txt', 'copy.txt')

