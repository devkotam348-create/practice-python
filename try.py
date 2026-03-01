# # def write_to_file(filename, text):
# #     f = open(filename,"w")
# #     f.write(text)
# #     f.close()
# # write_to_file("user.txt","mahendra devkota")

# # def appen_to_file(filename, text):
# #     f = open(filename,"a")
# #     f.write(text)
# #     f.close()
    
# # def read_files(filename):
# #     try:
# #         f = open(filename,"r")
# #         text = f.read()
# #         print(text)
# #     except FileNotFoundError:
# #         print("file not found")
# #     else:
# #         f.close()           
# # appen_to_file("user.txt","\njohn")
# # appen_to_file("user.txt","\nallex")

# read_files("user.txt")

def write_note(filename, text):
    with open(filename,"a") as f:
        f.write(text + "\n")

def read_note(filename):
    try:
        with open(filename,"r") as f:
            notes = []
            for lines in f:
                clean_lines = lines.strip()
                notes.append(clean_lines)
        return notes
            
    except FileNotFoundError:
        print("file not found")
        
        
note = input("Enter the notes::")
write_note("name.txt", note)
all_notes =read_note("name.txt")
print(all_notes)