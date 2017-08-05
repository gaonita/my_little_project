#
# #1
# print(" * "*8)
# print(" *                    *" )
# print(" *                    *" )
# print(" *                    *" )
# print(" *                    *" )
# print(" *                    *" )
# print(" *                    *" )
# print(" * "*8)
# print()
#
# #2
# print("* "*8)
# for i in range(0,6):
#     print("*             *")
# print("* "*8)
#
# #3
# print()
# for i in range(0,8):
#     if i == 0 or i== 7:
#         print("* "*8)
#     else:
#         print("* "+"  "*6+"*")
#
# print()
# #4
# a=int(input("How many stars on vertical?"))
# b=int(input("How many stars on horizontal?"))
#
# for i in range(0,a):
#     if i == 0 or i == a:
#         print("* " * b)
#     else:
#         print("* " * b)
#

#5
for i in range(0,8):
    if i == 0:
        print(" "*8+"*")
    elif i == 1:
        print(" "*7+"*"+"*")
    elif i == 2:
        print(" "*6+"*"+" "+"*")
    elif i == 3:
        print(" "*5+"*"+" "*2+"*")
    elif i == 4:
        print(" "*4+"*"+" "*3+"*")
    elif i == 5:
        print(" "*3+"*"+" "*4+"*")
    elif i == 6:
        print(" "*2+"*"+" "*5+"*")
    elif i == 7:
        print("*" * 8)

"""

def my_function(number):
    return number*2
def my_otherfunction(number):
    return (number*2)
a= my_function(4)
b= my_otherfunction(8)
print(a,"is half of",b)
"""