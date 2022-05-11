from time import time

def f1(func):
    # print(func)
    def wrapper(*args, **kwargs):
        # pass
        print("Started")
        func(*args, **kwargs)
        print("Ended")
        # return val

    return wrapper


@f1
def f2(a, b=9):
    print(a, b)


t1 = time()
for i in range(100000):
    a = i
    b = a * a
t2 = time()


print(t1)
print(t2)
print(f'{round     (      (t2 - t1) * 1000     , 2   )    }  ms')

# delta = (t2 - t1) * 1000
# print(round(delta, 2))

# print(round(23.323523452, 2))