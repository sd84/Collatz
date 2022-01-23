from Collatz import collatz


def main():
    try:
        collatz(int(input("Enter your value: ")))
    except ValueError:
        print("Wrong incoming value type! ")


if __name__ == "__main__":
    main()
