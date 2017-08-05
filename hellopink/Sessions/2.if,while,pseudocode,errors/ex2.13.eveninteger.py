while True:
    response = int(input("number?"))
    if response %2 == 0:
       print(response)
    elif response == 99:
        exit()
    else:
        print()