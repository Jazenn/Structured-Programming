import random

lijst_getallen = [random.randrange(0, 100) for x in range(random.randint(3, 7))]
matrix_lijsten = []
for x in range(random.randint(3, 7)):
    matrix_lijsten.append([random.randrange(0, 100) for x in range(random.randint(3, 8))])
    x += 1

def gemiddelde_cijfer(lijst):
    print(lijst)
    totaal = 0

    for getal in lijst:
        totaal += getal

    return f"{float(totaal / len(lijst)):.2f}"


def lijst_gemiddelden(matrix):
    print(matrix)
    lijst_gemiddelde = []
    totaal = 0
    for lijst in matrix:
        for getal in lijst:
            totaal += getal
        lijst_gemiddelde.append(float(f"{totaal / len(lijst):.2f}"))
        totaal = 0

    return lijst_gemiddelde


print(lijst_gemiddelden(matrix_lijsten))
print(gemiddelde_cijfer(lijst_getallen))
