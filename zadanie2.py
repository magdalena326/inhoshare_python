number = input("Podaj liczbe: ")
if number.isdigit():
    number = int(number)
    if number % 2:
        print("Nieparzysta")
    else:
        print("Parzysta")
else:
    print("Musisz podac liczbe")


