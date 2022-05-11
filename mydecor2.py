def tester(param):
    def wrapper(func):
        def internal_wrapper(*args):
            all_integers = True

            for value in args:
                if not isinstance(value, int):
                    all_integers = False

            if all_integers:
                print(f"Good. {len(args)} integers can be added")
                print("The result is: ", end='')
                func(*args)
            else:
                print("Sorry I cannot add those values...")
        return internal_wrapper
    return wrapper


@tester('decorator parameter')
def add_two(*args):
    print(sum(args))


# add_two(32, 3232, 'l')
add_two(32, 32, 23)
#