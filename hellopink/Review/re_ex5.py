#Add a try-except statment to the body of this function which handles a possible IndexError,
# which could occur if the index provided exceeds the length of the list. print an error message if this happens.
#
# def print_list_element(thelist, index):
#     try:
#         thelist[index]
#     except (IndexError):
#         print("Oops")
#     print (thelist[index])
#
# mange=["mango",'maker','mange']
# print_list_element(mange,4)

#print or Return ??????

#12 This function adds an element to a list inside a dic of lists.
# Rewrite it to use a try-except statement which handles a possible KeyError
# if the list with the name provided doesn't exist in the dictionary yet, instead of checking beforehand
#whether it does.
#
def add_to_list_in_dict(thedict, listname, element):
    try:
        thedict[listname]
    except KeyError:
        print("There is no such list!")
    if listname in thedict:
        l = thedict[listname]
        print ("{0} already has {1} elements.".format(listname, len(l)))
    else:
        thedict[listname] = []
        print ("Created %s." % listname)
    thedict[listname].append(element)
    print ("Added {0} to {1}.".format(element, listname))


färg = ['en blå','en grön','en rosa']
magnus = {"färg":färg}

add_to_list_in_dict(magnus,'A','abc')
print(magnus)
