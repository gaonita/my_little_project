#function a. creating a dictionary
def function_a(depart, destination, hours, overnight):
    plan = {}
    plan ["Departure"] = str(depart)
    plan ["Destination"] = str(destination)
    plan ["Duration"] = str(hours)
    plan ["Overnight"] = bool(overnight)
    return plan
#function b.
def function_b(plan_list):
    travel_list = []
    for i in range(0, len(plan_list) - 1, 3):
        travel_list.append(function_a(plan_list[i], plan_list[i + 3], plan_list[i + 1], plan_list[i + 2]))
    return travel_list
my_list = ['sthlm', 10, True, 'oslo', 11, True,'copenhagen',15,False,'krakow']
my_travel_list = function_b(my_list)

#function c.
def funcion_c(all):
    total = 0
    for j in range(0, len(all)):
        overnight = all[int(j)]["Overnight"]
        duration = int(all[int(j)]["Duration"])
        if overnight == True:
            total = total + ((int(duration)+10))
        else:
            total = total + duration
    return total

#function d. : takes function_b(list of dictionary)
#def function_d(travel):
travel = function_b(my_list)
for l in range(0,len(travel)):
       a = travel[int(l)]["Departure"]
       b = travel[int(l)]["Destination"]
       c = travel[int(l)]["Duration"]
       d = travel[int(l)]["Overnight"]
       if d == True:
        c = int(c) + 10,"hours including sleep->"
       else:
          c = c , "hours"
       print(a,"->",b,",will take: ",c,)
print("The whole trip will take:", funcion_c(function_b(my_list)))
       
