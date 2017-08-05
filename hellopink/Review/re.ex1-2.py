# a = input("What is your favourite food?")
# b = input("What is your second favourite food?")
# print("Thank you!\n" "You like", a,",", b, "and me 💕💕💕")

# cost = input("how much does it cost?")
# a = float(cost) + float(cost)*0.15
# b = float(cost) + int(cost)*0.2
# print("total cost with little tip:",a,"\ntotal cost with little more tip:", b)


correct_answer = "you"
counter = 0
while counter < 10:
    counter +=1
    print("Trial",counter)
    answer = input("Who do you love?").strip()
    if answer != correct_answer:
        print("Wrong😭! try again.")
        if counter == 10:
            print("😵You lose😵")
    elif answer == correct_answer:
        print("CORRECT! You love me!💕💕💕")
        break

# while True:
#     x = input("number?")
#     if int(x)%2 == 0:
#         print(x)
#     elif int(x) == 99:
#         exit()
#     else:
#         print()
#
# while True:
#     print("--Calculator Menu --\n""0.Quit\n""1.Add two numbers\n""2.Subtract two numbers\n""3.Multiply two numbers\n""4.Divide two numbers")
#     try:
#         a = int(input("Choose one"))
#     except (ValueError):
#         print("Please type NUMBERS!")
#     a = int(input("Choose one"))
#     if a == 0:
#         exit()
#     elif a == 1:
#         n1 = input("type first number")
#         n2 = input("type second number")
#         print(int(n1) + int(n2))
#     elif a == 2:
#         n1 = input("type first number")
#         n2 = input("type second number")
#         print(int(n1) - int(n2))
#     elif a == 3:
#         n1 = input("type first number")
#         n2 = input("type second number")
#         print(int(n1) * int(n2))
#     elif a == 4:
#         n1 = input("type first number")
#         n2 = input("type second number")
#         print(int(n1) / int(n2))
#     else:
#         pass