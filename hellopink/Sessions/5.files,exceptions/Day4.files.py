"""
with open('mixie.txt',"r") as text_file:
    read_data = text_file.read()
print(read_data)

text_file.closed


file = open("mixie.txt","r")
file.close()
print(file.closed)


print("\nReading characters from the file.")

with open("mixie.txt","r") as text_file:
    print(text_file.read(1))
    print(text_file.read(5))

with open("mixie.txt","r") as text_file:
    print(text_file.read(100))

with open("mixie.txt","r") as text_file:
    lines= text_file.readlines()
    for line in lines:
        print(line)


with open("mixie.txt","r") as text_file:
    for line in text_file:
        print(line)

print("\nCreating a file.")
with open("mixe.txt", "w") as text_file:
 text_file.write("Line 1\n")


with open("mixe.txt", "w") as text_file:
    lines=  ["Line 1\n",
             "Line 2\n"]
    text_file.writelines(lines)

"""

