ADMIN_USERNAME = "Piotr"
name = input("podaj imie:")

name_capitalized = name.lower().capitalize()

if name_capitalized == ADMIN_USERNAME:
    print(f"Witaj, {name_capitalized}")
elif name_capitalized != ADMIN_USERNAME:
    print("Witaj")
