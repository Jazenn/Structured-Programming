def fizzbuzz():
    for getal in range(1, 101):
        if getal % 3 == 0 and getal % 5 == 0:
            print("fizzbuzz")
        elif getal % 3 == 0:
            print('fizz')
        elif getal % 5 == 0:
            print('buzz')
        else:
            print(getal)


fizzbuzz()