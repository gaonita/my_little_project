# for i in range(0,-6,-1):
#     print(i)

# team = ["Ale","Kalle","Violeta","Anton","Hesper","Gaon","Johan"]
# another_team = ["Moa","Nikolaj","Olle"]
# bigteam = team + another_team
# bigteam.append("Sara")
#
# for person in bigteam:
#     if person in team:
#         print(person,"is in cool team.")
#     elif person in another_team:
#         print(person, "is from another team.")
#     else:
#         print(person,"is my friend!")


you = {"Reason1":"good heart","Reason2":"smart","Reason3":"voice"}
andyou ={"Reason1":"funny","Reason2":"cute","Reason3":"sweet"}
Reason = [you,andyou]

for i in Reason:
    print("1st reason why I love you:",i["Reason1"])
    print("2nd reason why I love you:",i["Reason2"])
    print("3rd reason why I love you:",i["Reason3"])
