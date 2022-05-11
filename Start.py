class Demo:

    counter = 0
    kind = 'car'

    def __init__(self, value, size, price):
        self.value = value
        self.size = size
        self.price = price
        Demo.counter += 1

    def start(self):
        print('Car starts')

    class_var = 'class variable'


d1 = Demo(value=100, size=3, price=900)
d2 = Demo(value=100, size=3, price=900)
d3 = Demo(value=100, size=3, price=900)

for item in d1, d2, d3:
    if item.kind == 'car':
        item.start()
    print(item.counter)