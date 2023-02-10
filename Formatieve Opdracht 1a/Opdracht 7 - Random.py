import random
random_getal = random.randint(1, 10)
input_getal = input("Raad welk getal ik in mijn gedachte heb:")

while True:
    if int(input_getal) == int(random_getal):
        print(f"Wow, je hebt het goed geraden! Het juiste getal is inderdaad {input_getal}.")
        break
    else:
        input_getal = input(f"Helaas. {input_getal} is niet correct. Probeer het nogmaals:")