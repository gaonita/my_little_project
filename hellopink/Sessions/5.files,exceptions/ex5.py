#1 program to read an entire txt file
# with open('test.txt',"r") as text_file:
#     read_data = text_file.read()
#     print(read_data)


# #2 program to read first n lines of a file
# with open("test.txt","r") as text_file:
#     print(text_file.readline())



#3 append text to a file and display the text
# with open("test.txt","w") as text_file:
#     text_file.write("Hello\n")
#     text_file.write("Hi\n")
#     text_file.write("Line3\n")
#     print(text_file)

# #5 program to read a file line by line store it into a variable(reading all lines into a list)
# with open("test.txt","r") as text_file:
#     lines = text_file.readlines()
#     print(lines)


#6 program to count the number of lines in a text file
# with open("test.txt","r") as text_file:
#     lines = text_file.readlines()
#     count = 0
#     for line in lines:
#         count +=1
#         print(count,line)

#7 Write a Python program to write a list to a file
# with open("test1.txt","w") as text_file:
#     lines = ["line1\n"
#              "line2\n"]
#     text_file.writelines(lines)

#9 Write a Python program to assess if a file is closed or not
# with open("test.txt","r") as f:
#     read_data = f.read()
# print(f.closed)

# try:
#     x= int(input("Number: "))
# except(ValueError):
#     print("Oops!")

#11 Add a try-except statement to the body of this function which handles a possible indexError,
# which could occur if the index provided exceeds the length of the list.
#Print an error message if this happens:

# def print_list_element(thelist, index) :
#     try:
#         return thelist[index]
#     except (IndexError,NameError):
#         return "Oops"
#
# name_list = ["anton","Violeta","Kalle","Hesper"]
# print(print_list_element(name_list,1))

#12 This function adds an element to a list inside a dic of lists.
# Rewrite it to use a try-except statement which handles a possible KeyError
# if the list with the name provided doesn't exist in the dictionary yet, instead of checking beforehand
#whether it does.
#
def add_to_list_in_dict(thedict, listname, element):
    if listname in thedict:
        l = thedict[listname]
        return ("{0} already has {1} elements.".format(listname, len(l)))
    # else:
    #     thedict[listname] = []
    #     print ("Created %s." % listname)
    # thedict[listname].append(element)
    # print ("Added {0} to {1}.".format(element, listname))
    try:
        listname in thedict
        l = thedict[listname]
    except KeyError:
        print("This list doesn't exist in the dictionary!")
        thedict[listname] = []
        print("Created %s." % listname)
        thedict[listname].append(element)
        print("Added {0} to {1}.".format(element, listname))

test_list = ['a','b','c','d']
test_dict = {'my_little_list': test_list}
add_to_list_in_dict(test_dict,'a','1')


