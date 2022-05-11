def func1(name):
    print('Func1')
    name = name * 3

    def inner(name):
        print('Inner func2')
        print(name)

    return inner(name)


func1('kaljs')