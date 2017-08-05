
response = "p"
counter = 0
while counter <10:
    counter += 1
    print(counter)
    response = input("word?")
    if response != "p":
        print("wrong!")
    elif response == "p":
        print("Correct!")
        break