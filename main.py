import random


def Generator(n):
    return [random.randint(0, n) for i in range(n)]

n = int(input("Введите размер списка: "))
res = Generator(n)
print("Сгенерированный список: ", res)