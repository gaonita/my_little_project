def animal(animal_list):
    animal = {}
    counter = 0
    for i in animal_list:
        counter += 1
        animal[counter]=i
    return animal

animal_name = ["cat","dog","Lion"]

print(animal(animal_name))