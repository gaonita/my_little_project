def what_range(number):
    if number in range(0,11):
        print(number,"is in range 0-10")
    elif number in range(11,21):
        print(number,"is range 11-20")
    else:
        print(number,"is range infinite!")

print(what_range(200))
