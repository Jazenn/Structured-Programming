def palindroom(woord):
    if len(woord) <= 1:
        print(f"Dit woord is een palindroom!")
    elif woord[0] != woord[-1]:
        print(f"Dit woord is helaas geen palindroom.")
    else:
        return palindroom(woord[1:-1])


palindroom("koekwaus")
