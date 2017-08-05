#a
def function_a(departure, destination,duration,overnight):
    trip_dict ={}
    trip_dict["departure"] = departure
    trip_dict["destination"] = destination
    trip_dict["duration"] = duration
    trip_dict["overnight"] = bool(overnight)
    return trip_dict

#b
def function_b(the_list):
    list_of_dictionaries =[]
    for i in range(0,len(the_list)-1,3):
        trip_dict = function_a(the_list[i], the_list[i+3], the_list[i+1], the_list[i+2])
        list_of_dictionaries.append(trip_dict)
    return list_of_dictionaries
trip_list = ['sthlm', 10, True, 'oslo', 11, True, 'copenhagen', 15, False, 'krakow']

#c
def function_c(dictionaries):
    total = 0
    for dictionary in dictionaries:
        hours = dictionary['duration']
        if dictionary['overnight'] == True:
            total= total + 10
        total = total + hours
    return total
#d
def function_d(dictionaries):
    dictionaries = (function_b(trip_list))
    for dictionary in dictionaries:
        a = dictionary['departure']
        b = dictionary['destination']
        c = dictionary['duration']
        if dictionary['overnight'] == True:
            c = str((int(c) + 10)) + " hours including sleep"
        else:
            c = str(int(c)) + " hours"
        print( a, "->", b,",", "will take:", c)
    print("The whole trip will take:", function_c(dictionaries))

function_d(function_b)

#[] {} (1, 2, 3, "hej")

