a = int(input("Podaj gorny zakres przedzialu: "))

suma_parzystych = 0
suma_nieparzystych = 0
#Przedzialy rozpoczete od 1 i 2, aby nie rozpatrywac 0
for parzysta in range(1, a+1, 2):
    suma_nieparzystych +=1
    print("Liczba nieparzystych to {}".format(suma_nieparzystych))
for nieparzysta in range(2, a+1, 2):
    suma_parzystych +=1
    print("Liczba parzystych to {}".format(suma_parzystych))
