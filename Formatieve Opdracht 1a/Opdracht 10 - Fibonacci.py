def fibonacci_recursief(n):
    if n <= 1:
        return n

    return fibonacci_recursief(n - 1) + fibonacci_recursief(n - 2)


print(fibonacci_recursief(15))

