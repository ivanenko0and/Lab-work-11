
"""
Дан двійковий файл f, компоненти якого є дійсними числами.
Знайти суму, добуток, суму квадратів і квадрат добутку компонентів файлу f, а також останню компоненту файлу.
Результати записати у файл g.

Виконав Іваненко Андрій Вадимович
"""

import random
import pickle


answer = '1'
while answer == '1':

    # Запис послідовності з випадкових дійсних чисел у двійковий файл f.txt
    pickle.dump([random.uniform(-100, 100) for i in range(random.randint(1, 10))], open('f.txt', 'bw'))

    numbers = pickle.load(open('f.txt', 'br'))  # numbers - послідовність чисел, записаних у файлі f.txt

    num_sum, num_product, square_sum = 0, 1, 0
    """ num_sum - сума послідовності чисел.
        num_product - добуток послідовності чисел.
        square_sum - сума квадратів послідовності чисел. """

    print("Файл f.txt містить такі дані:")
    for i in numbers:
        print(i)  # Виведення послідовності чисел

        num_sum += i  # Знаходження значень num_sum, num_product і square_sum
        num_product *= i
        square_sum += i**2

    product_square = num_product**2
    last_num = numbers.pop()
    """ product_square - квадрат добутку послідовності чисел.
        last_num - останнє число послідовності. """

    g = open('g.txt', 'w')  # Запис отриманих даних у файл g.txt
    g.write(f"Сума чисел: {num_sum}\nДобуток чисел: {num_product}\nСума квідратів чисел: {square_sum}\n"
            f"Квадрат добутку чисел: {product_square}\nОстаннє число: {last_num}")
    g.close()

    g = open('g.txt', 'r')  # Виведення даних файлу g.txt
    print(g.read())
    g.close()

    answer = input("Введіть '1' для повторення:")

