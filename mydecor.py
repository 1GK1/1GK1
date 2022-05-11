def tester(func):
    def wrapper(*args):
        all_integers = True

        for value in args:
            if not isinstance(value, int):
                all_integers = False

        if all_integers:
            print(f"Good. {len(args)} integers can be added")
            print("The result is: ")
            func(*args)
        else:
            print("Sorry I cannot add those values...")

    return wrapper


@tester
def add_two(*args):
    print(sum(args))


add_two(32, 1, 4)

