
animal_list = ["cow", "dog", "cat", "rabbit"]

def animal_dictionary(list):
    counter = 0
    dictionary = {}
    for animal in list:
        counter += 1
        dictionary[counter] = animal
    return dictionary

my_animal_dictionary= animal_dictionary(animal_list)
print(my_animal_dictionary)
