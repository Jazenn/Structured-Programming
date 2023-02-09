input_1 = input("Voer hier uw eerste zin in:")
input_2 = input("Voer hier uw tweede zin in:")

teller_1 = 0
teller_2 = 0

while True:
    if teller_1 >= len(input_1):
        if teller_2 >= len(input_2):
            print("De twee ingevoerde zinnen zijn identiek!")
            break
        else:
            print(f"Het eerste verschil zit op index: {teller_2}")
            break
    elif teller_2 >= len(input_2):
        if teller_1 >= len(input_1):
            print("De twee ingevoerde zinnen zijn identiek!")
            break
        else:
            print(f"Het eerste verschil zit op index: {teller_1}")
            break
    elif input_1[teller_1] != input_2[teller_2]:
        print(f"Het eerste verschil zit op index: {teller_1}")
        break
    else:
        teller_1 += 1
        teller_2 += 1
