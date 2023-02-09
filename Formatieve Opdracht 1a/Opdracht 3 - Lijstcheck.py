import random

def lijst_genereren():
    lijst_getallen = []
    for i in range(0, 30):
        lijst_getallen.append(random.randint(0, 10))
    return lijst_getallen


def count(x):
    counter = 0
    lijst_getallen = lijst_genereren().copy()
    print(lijst_getallen)

    for getal in lijst_getallen:
        if getal == x:
            counter += 1

    return counter


print(count(3))
