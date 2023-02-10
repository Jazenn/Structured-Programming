with open("Opdracht 8 - Tekstbestand", 'r') as textfile:
    inhoud = textfile.readlines()
    print(inhoud)

for regel in inhoud:
    if regel == '' or regel == '\n':
        continue
    with open("Opdracht 8 - Nieuw Tekstbestand", 'a') as new_textfile:
        new_textfile.write(regel.strip())
        new_textfile.write("\n")