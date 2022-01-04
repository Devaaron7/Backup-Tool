list_a = ["Apples", "Apricots", "Asian Pears"]

list_b = ["Banana", "Bearberry", "Blueberry"]

list_c = ["Cherry", "Carob Fruit", "Calabash Fruit"]



list_of_fruits = []

print(list_of_fruits)

list_of_fruits.append(list_a)
list_of_fruits.append(list_b)
list_of_fruits.append(list_c)

print(list_of_fruits)


for every_fruit_list in list_of_fruits:
    for fruit_list in every_fruit_list:
        print(fruit_list)