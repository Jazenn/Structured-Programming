import random


def lijst_genereren():
    lijst_getallen = []
    for i in range(0, 30):
        lijst_getallen.append(random.randint(-10, 10))
    return lijst_getallen


def lijst_1en_0en():
    lijst_getallen = []
    for i in range(0, 30):
        lijst_getallen.append(random.randint(0, 1))
    return lijst_getallen


def count(x):
    counter = 0
    lijst_getallen = lijst_genereren().copy()
    print(lijst_getallen)

    for getal in lijst_getallen:
        if getal == x:
            counter += 1

    return counter


def grootste_verschil():
    lijst_getallen = lijst_genereren().copy()
    print(lijst_getallen)
    verschil_getallen = 0
    verschil_grootste = 0
    counter = 1

    for getal in lijst_getallen:
        if counter >= len(lijst_getallen):
            break
        verschil_getallen = getal - lijst_getallen[counter]
        if abs(verschil_getallen) >= verschil_grootste:
            verschil_grootste = abs(verschil_getallen)
        counter += 1

    return verschil_grootste


def lijst_controleren():
    lijst_getallen = lijst_1en_0en().copy()
    print(lijst_getallen)

    if lijst_getallen.count(1) > lijst_getallen.count(0):
        if lijst_getallen.count(0) <= 12:
            return True
    return False


print(count(3))
print(grootste_verschil())
print(lijst_controleren())
