beers = range(99, 0, -1)
message = ("{beers_before} beczek na polce stalo, jedna spadla, \n"
           "{beers_after} zostalo?")

for beer in beers:
    print(message.format(beers_before=beers, beers_after=beer - 1))
