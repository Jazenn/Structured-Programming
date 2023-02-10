def cyclisch_verschuiven(ch, n):
    binary_number = ''.join(format(ord(i), '08b') for i in ch)
    print(binary_number)

    if n > 0:
        return binary_number[n:] + binary_number[:n]
    elif n < 0:
        return binary_number[n:] + binary_number[:n]
    else:
        return binary_number

print(cyclisch_verschuiven("DIT IS EEN ZIN", -3))