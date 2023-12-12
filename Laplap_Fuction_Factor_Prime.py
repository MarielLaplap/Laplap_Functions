def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_number():
    while True:
        start = int(input("Enter a number [start]: "))

        if start < 0:
            print("Enter a non-negative number.")
            print()
            continue

        if start == 0:
            print("Program terminated.\n")
            break

        end = int(input("Enter a number [end]: "))

        if end <= start:
            print("Enter a number greater than", start)
            print()
            continue

        print("Prime numbers between", start, "and", end, "are:")
        for num in range(start, end + 1):
            if is_prime(num):
                print(num, end=" ")

        print("\n")


def find_smallest_factor(n):
    if n < 2:
        print("Invalid input. Enter a number greater than or equal to 2.")
        return

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"The smallest factor other than 1 for {n} is {i}.")
            return

    print(f"{n} is a prime number, and its only factor is 1.")


def smallest_factor():
    while True:
        try:
            num = int(input("Enter an integer (greater than or equal to 2): "))
            find_smallest_factor(num)
            print()

            if num < 2:
                print("Invalid input. Enter a number greater than 2.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


while True:
    print("[1] prime nummber        [2] smallest factor")
    print("[0] to exit\n")
    user_pick = int(input("Enter a number: "))

    if user_pick == 1:
        prime_number()
    elif user_pick == 2:
        smallest_factor()
    elif user_pick == 0:
        break
    else:
        print("Invalid choice. Try again!")

