"""
from math import pi

def circle_circumference(radius):
    #Return circle circumference
    circumference = 2 * pi * radius
    return circumference

    print(circle_circumference(5))

#circumference = circle_circumference(100)
#print(circumference)



#Positional parameters
def birthday_wishes1(name, age):
    print("Happy birthday,"+name+"! You're"+ str(age)+ "today.\n")

birthday_wishes1("Carol",30)
birthday_wishes1("a","Carol")
birthday_wishes1(name="Carol", age=30)
birthday_wishes1(age=30,name="Carol")



#Parameters with default values
def birthday_wishes2(name="Julia",age="25"):
    print("Happy birthday,"+name+"! You're"+str(age)+"today.\n")

birthday_wishes2()
birthday_wishes2(name="Klara")
birthday_wishes2(age=27)
birthday_wishes2(name="Klara", age=27)
birthday_wishes2("Klara",27)
birthday_wishes2("Klara")

"""
value = 10 #global variable

#capsule
def read_global():
    print("From inside the scope of read_global(), value is: ", value)
read_global()

#global scope
print("In the global scope, value is: ", value)

#local variable
def shadow_global():
    value = -10 #same variable name as global variable name. This is value.
    print("From inside the scope of shadow_global(), value is: ", value)

shadow_global()

print("In the global scope, value is: ",value)

def change_global():
    global value #This is how you ask for permission to change a global value
    value= -10
    print("From inside the scope of change_global(), value is: ", value)

change_global()
print("In the global scope, value is: ",value)