import random
import sys
from random import uniform


class Apple:
    number_of_apples = 0
    weight_of_apples = 0

    def __init__(self):
        Apple.number_of_apples += 1
        Apple.weight_of_apples += random.uniform(0.2, 0.4)
        # Apple.check_number_and_weight(self)

    # def check_number_and_weight(self):
    #     if Apple.number_of_apples == 1000:
    #         print("Maximum number of apples!")
    #     if Apple.weight_of_apples > 300:
    #         print("Maximum weight of apples!")


apples = ["apple_" + str(x) for x in range(1000)]
print(apples)


while Apple.number_of_apples < 1000 and Apple.weight_of_apples < 300:
    for apple in apples:
        print(apple)
        apple = Apple()
        print(apple)

print()
print('Results:')
print(f'Number of apples: {Apple.number_of_apples}')
print(f'Weight of apples: {round(Apple.weight_of_apples, 2)}')

