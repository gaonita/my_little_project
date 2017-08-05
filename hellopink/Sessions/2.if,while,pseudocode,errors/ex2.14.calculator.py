while True:
    print("0.Quit\n1.Add two numbers\n2.Subtract two numbers\n3.Multiply two numbers\n4.Divide two numbers")
    response = int(input("Which operation do you want to do?"))
    if response == 0:
       exit()
    elif response == 1:
        a = int(input("choose first number"))
        b = int(input("choose second number"))
        print(a+b)
    elif response == 2:
        a = int(input("choose first number"))
        b = int(input("choose second number"))
        print(a-b)
    elif response == 3:
        a = int(input("choose first number"))
        b = int(input("choose second number"))
        print(a*b)
    elif response == 4:
        a = int(input("choose first number"))
        b = int(input("choose second number"))
        print(a/b)
    else:
        print()