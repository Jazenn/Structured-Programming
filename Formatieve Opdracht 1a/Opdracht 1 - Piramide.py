ster = '*'
spatie = ' '

def piramide_for_loops(input_lengte):
    teller = 0
    # input_lengte = input('Geef hier de lengte van de piramide weer:')

    for piramide_begin in range(0, int(input_lengte)):
        teller += 1
        string = teller * ster
        print(string)

    for piramide_eind in range(0, int(input_lengte)):
        teller -= 1
        string = teller * ster
        print(string)


def piramide_while_loops(input_lengte):
    # input_lengte = input("Geef hier de lengte van de piramide weer:")
    teller = 0

    while True:
        if teller >= int(input_lengte):
            break
        teller += 1
        string = teller * ster
        print(string)

    while True:
        if teller <= 0:
            break
        teller -= 1
        string = teller * ster
        print(string)


def omgekeerde_piramide(input_lengte):
    teller = 0

    while True:
        if teller >= int(input_lengte):
            break
        teller += 1

        string = (int(input_lengte) - teller) * spatie + teller * ster
        print(string)

    while True:
        teller -= 1
        if teller <= 0:
            break

        string = (int(input_lengte) - teller) * spatie + teller * ster
        print(string)


piramide_for_loops(5)
piramide_while_loops(5)
omgekeerde_piramide(5)

