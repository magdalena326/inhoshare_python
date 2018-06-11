names = ["pawel", "michal", "anna", "kasia", "tomek"]
dlugos_listy = len(names)
print(dlugos_listy)
first_name = names[0]
print(first_name)
names.append("agnieszka")
print(names)
print("Ostatni element listy to", names[-1])

name_to_find = "julia"
julia_count = names.count(name_to_find)
print("Liczba osob o imieniu ", name_to_find, julia_count)

name_to_find = "michal"
print("Liczba osob o imieniu ", name_to_find, names.count("michal"))

to_find = names.index(name_to_find)
print("index of", name_to_find, to_find)

if name_to_find in names:
    print(name_to_find, "znajduje sie w liscie")
else:
    print(name_to_find, "nie znajduje sie w liscie")

new_list = names[1:3]
print(new_list)

for name in names:
    print(name)

#listy złożone

import copy

chemia = ["mydlo", "pasta", "krem", "lakier", "farba"]
owoce = ["truskawki", "maliny"]
zakupy_czerwiec = [chemia, owoce]
#print("Zakupy czerwiec:", zakupy_czerwiec)

zakupy_lipiec = copy.deepcopy(zakupy_czerwiec)
#print("Zakupy lipiec: ", zakupy_lipiec)
print(zakupy_lipiec)
print(zakupy_czerwiec)


for kategoria_zakupow in zakupy_czerwiec:
    for towar in kategoria_zakupow:
        print(towar)
    print()

zakupy_lipiec[1].append("jablka")
print(zakupy_lipiec)


my_list = [[1, 2, 3], [4, 5, 6]]
new_list = my_list[1][0:2]
print(new_list)

print("Names", names)
add_names = ["piotr", "kasia"]
names.extend(add_names)
print("Add names", names)

add_more_names = ["ula"]
names_extended = names + add_more_names
print("Names extended", names_extended)

name_to_remove = "anna"
names_extended.remove(name_to_remove)
print("After removal", names)

removed_name = names_extended.pop(-1)
print(removed_name)

########################################

duplicates = [1, 2, 5, 1, 4, 7, 7, 7]
without_duplicates = []
for element in duplicates:
    if element not in without_duplicates:
        without_duplicates.append(element)
print("Without duplicates", without_duplicates)

