def range_function(i):
    if i in range(0,11):
        print (i, "is in range 0-10")
    elif i in range(10,21):
        print(i,"is in range 11-20")
    else:
        print (i,"is in range 21 to infinite")
    return print()

my_range = range_function(30)
print(my_range)