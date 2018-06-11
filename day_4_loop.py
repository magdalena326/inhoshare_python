MAX_BEERS=99
MIN_BEERS=0

current_amount_of_beers = MAX_BEERS

while current_amount_of_beers > MIN_BEERS:
    print("Zostalo {} piw".format(current_amount_of_beers))
    current_amount_of_beers -= 1

