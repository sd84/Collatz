def collatz(value):
    result = value
    while result != 1:
        if result % 2 == 0:
            result //= 2
            print(result)
        else:
            result = 3 * result + 1
            print(result)
