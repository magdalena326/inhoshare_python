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



