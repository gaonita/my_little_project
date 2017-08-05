# def triangle(y):
#     x=0
#     for a in range (0,y):
#         stars = a * 2 + 1
#         print((' ' * ( y- a)) + ('*' * (stars)))
#
# triangle(5)

y=int(input('number'))
for i in range(0,y):
    stars = i*2+1
    #stars_1 = stars -((i-1)*2+1)-1
    if i > int(int(y)/2)-1:
        stars_1 = (i-int(y/2))*2+1
        #print(' ' * (y-i) + ('*' * stars_1) + ' ' * (((i - 1) * 2 + 1)) + '*' * stars_1)
        print(' ' * (y-i) + ('*' * stars_1) + ' ' * (2*y-2*i-1) + '*' * stars_1)
    else:
            print(' '*(y-i)+ '*'*stars)