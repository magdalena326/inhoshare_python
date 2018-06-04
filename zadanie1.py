ADMIN_USERNAME = "piotr"
imie = input("podaj imie:")
if imie == ADMIN_USERNAME:
    print(f"Witaj, {imie}")
elif imie != ADMIN_USERNAME:
    print("Witaj")
