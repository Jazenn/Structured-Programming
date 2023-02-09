ster = '*'
teller = 0
input_lengte = input('Geef hier de lengte van de piramide weer:')

for piramide_begin in range(0, int(input_lengte)):
    teller += 1
    string = teller * ster
    print(string)

for piramide_eind in range(0, int(input_lengte)):
    teller -= 1
    string = teller * ster
    print(string)