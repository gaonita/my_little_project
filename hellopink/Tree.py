def my_happy_function(y):
    x=0
    # for a in range (0, y):
    #     stars = a * 2 + 1
    #     print((' ' * (y - a)) + ('*' * (stars)))
    # for a in range(0, y):
    #     stars = a * 2 + 1
    #     print((' ' * (y - a)) + ('*' * (stars)))

    for i in range(0, y):
        x = x + 2
        y = y - 1
        if i in range(0,y+2,2):
            print('  ' * (y) + '✨'+'💚'* int(x)+'✨'+'                '+'🎈')
        elif i in range(1,y+4,2):
            print('  ' * (y) + '✨' + '🌈' * int(x) + '✨'+'      '+'🐬')
        else:
            print('  ' * (y)+'✨' + '🌸' * int(int(x)/2)+'🌳'*int(int(x)/2)+'✨')

def my_cute_function_1(y):
     x= 0
     for i in range(0, y):
         x = x + 2
         y = y -1
         if i == y+1:
             print('  ' * (y) + '✨'+'🐰💕'* int(x/2)+'✨'+'             '+'🎁')
         else:
             print('  ' * y +'✨'+ '💚💙' * int(x/2)+'✨')

def my_unhealthy_function_(y):
    x=0
    for i in range(0, y):
        x = x + 2
        y = y - 1
        if i in range(0,y+2,2):
            print('  ' * (y) + '🍬'+'🍟'* int(x)+'🍬'+'                '+'🍭')
        elif i in range(1,y+4,2):
            print('  ' * (y) + '✨' + '🍩' * int(x) + '✨'+'      '+'🍰')
        else:
            print('  ' * y + '✨' + '🍕🍫' * int(x / 2) + '✨')

def my_little_function_3(y):
    for i in range(0,y-2):
        if i ==0 or  y-3:
            print('  '*int(y/2+2) + '🐻'*int(y-2))
        # else:
        #     print('  '*int(y/2) + '🐻' + '  '*int(y-1) +'🐻')

def apple_tree_1(y):
    x=0
    for i in range(0, y):
        x = x + 2
        y = y - 1
        if i in range(0, y + 2, 2):
            print('  ' * (y) + '✨' + '🍓' * int(x) + '✨' + '             ' + '🐝')
        elif i in range(1, y + 4, 2):
            print('  ' * (y) + '✨' + '🍋' * int(x) + '✨' + '      ' + '🦋')
        else:
            print('  ' * (y) + '✨' + '🍎' * int(int(x) / 2) + '🍏' * int(int(x) / 2) + '✨')

def apple_tree_2(y):
    x = 0
    for i in range(0, y):
        x = x + 2
        y = y - 1
        if i in range(0, y + 2, 2):
            print('  ' * (y) + '✨' + '🍊' * int(x) + '✨' + '             ' + '🐝')
        elif i in range(1, y + 4, 2):
            print('  ' * (y) + '✨' + '🍒' * int(x) + '✨' + '      ' + '🦋')
        else:
            print('  ' * (y) + '✨' + '🍇' * int(int(x) / 2) + '🍅' * int(int(x) / 2) + '✨')
q = 0
while True:
    if q < 1 or q > 3:
        print('\n----TRÄD MENU----\n''1.FRUKT TRÄD\n''2.HAPPY TRÄD\n''3.UNHEALTHY TRÄD\n------------------')
        try:
            q = int(input('Hej🌳Vilken träd vill du se? Choose a number on the menu above!:'))
            if q < 1 or q > 3:
                raise ValueError
        except (ValueError):
            print("😡⛔No Christian⛔😡, I said a number on the menu!")
            continue
        #q = int(input('Hej🌳Vilken träd vill du se? Choose a number on the menu above!:'))


    try:
        y = int(input("what is your lucky 'even' number between 4-12?"))
        if y > 13 or y<4 :
            raise ValueError
    except:
        print("😡⛔No Christian⛔😡, I said a number between 4 and 12!")
        continue
        #y = int(input("what is your lucky 'even' number between 4-12?"))

    if q ==1:
        apple_tree_1(y)
        apple_tree_2(y)
        my_little_function_3(y)
    elif q ==2:
        my_happy_function(y)
        my_cute_function_1(y)
        my_little_function_3(y)
    elif q ==3:
        my_unhealthy_function_(y)
        my_little_function_3(y)

    q = 0

