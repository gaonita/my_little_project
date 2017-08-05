"""
for i in range(50,0,-5):
    print("i =", i)

word = "index"
print(word[0])

for i in "index":
    print(i)

for i in range(0,18,3):
    print("i=",i)

for i in range(0,-6,-1):
    print("i=",i)

animals=["cat","dog","fish","cow","pig","fox"]
print(animals[1:])
print(len(animals))

farm_animals =["sheep","cow","pig"]
wild_animals =["fox","wolf","eagle"]
all_animals= farm_animals + wild_animals
print(all_animals)
del all_animals[-1]
print(all_animals)

all_animals.append("horses")
print(all_animals)

all_animals[-1]="horse"
print(all_animals)

all_animals[0]="lamb"
print(all_animals)

for animal in all_animals:
    print(animal)

letter_list = ["a","b"]
number_list = ["1","2"]
all_list = [letter_list,number_list]
print(all_list[0])


members = ["Matilda","Sofie","Marie","Linsey","Ida-marie","Åsa","Raiha","Lorena","Gaon","Cristina","Ala","Moa","Angelica"]
teachers = ["Sara","Liza","Mariana","Nadia"]
friend = ["Elena"]
all = [members,teachers,friend]

for a in range(0,len(all)):
    for person in all[a]:
        if a == 0:
           print(person+ " is a participant")
        elif a == 1:
            print(person+ " is a teacher")
        else:
            print(person+ " is a friend")
"""
animal_info = {"sheep":"stubborn", "cow":"gives milk"}
animal_info["wolf"]="wants to eat cow"
del animal_info["wolf"]

for key in animal_info:
    print(animal_info[key])

#for key, value in animal_info.items():
 #   print(key, "has info:", value)